def sequential_map(*args):
    n = len(args)
    n = n - 1
    list_x = args[n]
    res_list = []
    for x in list_x:
        i = n - 1
        res = 0
        while i >= 0:
            res = args[i](x)
            x = res
            i = i - 1
        res_list.append(res)
    return(res_list)


def consensus_filter(*args):
    n = len(args)
    n = n - 1
    list_x = args[n]
    res_list = []
    var_list = []
    for x in list_x:
        i = n - 1
        res = 0
        while i >= 0:
            res = args[i](x)
            i = i - 1
            if res is True:
                res_list.append(res)
        if len(res_list) == n:
            var_list.append(x)
    return(var_list)


def conditional_reduce(fun1, fun2, l):
    res_list = []
    for i in range(1, len(l)):
        i2 = l[i]
        i1 = l[i-1]
        res2 = fun2(i1, i2)
        res1 = fun1(res2)
        if res1 != False:
            res_list.append(res2)
    print(*res_list)


def multiple_partial(*args, **kwargs):
    func_list = []
    for arg in args:
        func_list.append(arg(**kwargs))
    return func_list
