import time


def timeit(func, *args, **kargs):
    try:
        start = time.clock()
        func(*args, **kargs)
        end = time.clock()
    except Exception, diag:
        return str(diag)
    else:
        return end - start


def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '_' * 20
        for eachVal in vals:
            retval = timeit(eachFunc, eachVal)
            if retval:
                print '%s(%s) = ' % (eachFunc.__name__, eachVal), retval
            else:
                print '%s(%s) = FAILED: ' % (eachFunc.__name__, eachVal), retval


if __name__ == '__main__':
    test()
