import time
import random

# Task 1
# 1. Напишите простой декоратор, подменивающий возвращаемое значение декорируемой
# функции на время её выполнения (Example_1). Для измерения времени воспользуйтесь
# модулем time. (3 балла)


def decorator1(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        return (end - start)
    return wrapper


print('')
print('That shows how the 1st decorator works (measures time of function)')


@decorator1
def time_f():
    return 'Hi'


print(time_f())


# Task 2
# 2. Напишите декоратор, позволяющий логировать запуски функций, распечатывая входные данные
# и тип возвращаемых значений (Example_2). Для получения имени класса в виде строки можно
#  воспользоваться атрибутом __name__. (7 баллов)

def decorator2(func):
    def wrapper(*args, **kwargs):
        func()
        func_return = func.__annotations__
        saved_args = locals()
        saved_args['class'] = __name__
        saved_args['undeclared_return'] = type(func())
        return saved_args
    return wrapper


print('')
print('That shows how the second decorator works (logging)')


@decorator2
def func1(*args, **kwargs):
    return 'It is an error'


print(func1(5, 6, 'arg'))

# Task 3
# 3. Сделайте декоратор - русскую рулетку, который сделает так, чтобы декорируемая
# функция с заданной вероятностью заменяла возвращаемое значение на переданное декоратору
# (Example_3). (7 баллов)


def decorator3(inp, prob):
    def wrapper(func):
        analog = lambda: inp
        func_list = ['func', 'analog']
        actual_func = random.choices(func_list, weights=[1-prob, prob])
        call = ''.join(actual_func)
        return eval(call)
    return wrapper


print('')
print('That is probability-based decorator')
print('It prints hi or bye with probability 0.5')


@decorator3(inp='Bye', prob=0.5)
def rand_greet():
    return 'Hi'


print(rand_greet())
