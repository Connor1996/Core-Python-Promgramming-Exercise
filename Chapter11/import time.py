import time

def timeit(f):
    def counter(*args, **kargs):
        start = time.clock()
        ret = f(*args, **kargs)
        end = time.clock()
        print 'function:', f.__name__
        print 'spend time:', end - start
        print 'return value:', ret
        print
        return ret
    return counter

@timeit
def fac1(n):
    total = 1
    for i in xrange(1, n+1):
        total *= i
    return total

@timeit
def fac2(n):
    return reduce(lambda x, y: x * y, xrange(1, n+1))

def fac3(n):
    if n == 1:
        return 1
    else:
        total =  fac3(n-1) * n
    return total

if __name__ == '__main__':
    fac1(100)
    fac2(100)
    fac3(100)