import time


def timeit(func):
    def counter(*args, **kargs):
        start = time.clock()
        ret = func(*args, **kargs)
        end = time.clock()
        print 'function: ', func.__name__
        print 'spendtime: ', end - start
        print 'return value: ', ret
        return ret
    return counter

@timeit
def fun1(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


@timeit
def fun2(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


@timeit
def fun3(n):
    if n == 1:
        return 1
    else:
        return fun3(n - 1) * n

if __name__ == '__main__':
    fun1(10)
    fun2(10)
    fun3(10)
