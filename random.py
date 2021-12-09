import numpy as np
import random
import matplotlib.pyplot as plt
import timeit
import re

random_dict = dict()
numpy_dict = dict()
for i in [1, 3, 5, 7]:
    random_time = 0
    numpy_time = 0
    for j in range(1, i+1):
        random_time_step = timeit.Timer("random.uniform(0, 1)", setup='import random').timeit()
        numpy_time_step = timeit.Timer("np.random.uniform(0, 1)", setup='import numpy as np').timeit()
        random_time = random_time + random_time_step
        numpy_time = numpy_time + numpy_time_step
    random_dict[i] = random_time
    numpy_dict[i] = numpy_time

plt.bar(random_dict.keys(), random_dict.values(), width=0.5, color='y')
plt.xlabel('Number of integers')
plt.ylabel('Time')
plt.title('Histogram of calculation time for random')
plt.grid(True)
plt.xticks([i for i in [1, 3, 5, 7]])
plt.show()

plt.bar(numpy_dict.keys(), numpy_dict.values(), width=0.5, color='y')
plt.xlabel('Number of integers')
plt.ylabel('Time')
plt.title('Histogram of calculation time for numpy')
plt.grid(True)
plt.xticks([i for i in [1, 3, 5, 7]])
plt.show()

# Task 3

print("type n of steps in random walk")


def random_walk(n):
    coord = [[0 for i in range(0, n)], [0 for i in range(0, n)]]
    i = 1
    x = 0
    y = 0
    while i < n:
        command = np.random.randint(4)
        if command == 0:
            coord[0][i] = x
            coord[1][i] = y + 1
            y = y + 1
        if command == 1:
            coord[0][i] = x
            coord[1][i] = y - 1
            y = y - 1
        if command == 2:
            coord[0][i] = x + 1
            coord[1][i] = y
            x = x + 1
        if command == 0:
            coord[0][i] = x - 1
            coord[1][i] = y
            x = x - 1
        i = i + 1
    return(coord)


n = int(input())
coord = random_walk(n)

plt.scatter(coord[0], coord[1])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random walk')
plt.grid(True)
plt.xticks([i for i in range(-(n+1), n+1)])
plt.yticks([i for i in range(-(n+1), n+1)])
plt.show()

# Task 5

print("type text")
text = input()
pattern5 = r'\w+'
words = list(re.findall(pattern5, text, re.IGNORECASE))
words_list = []
for w in words:
    w1 = w[1:len(w)-1]
    w1_rand = ''.join(random.sample(w1, len(w1)))
    w_rand = w[0] + w1_rand + w[len(w)-1]
    words_list.append(w_rand)
print(*words_list)
