import threading
import time
from random import randint


def create(filename, value, total, maxlen):
    assert 0 <= value <= 255
    ls = [chr(randint(0, 255)) for i in xrange(maxlen - total)]
    ch = chr(value)
    for i in xrange(total - ls.count(ch)):
        ls.insert(randint(0, len(ls) - 1), ch)
    for i in xrange(maxlen - len(ls)):
        ls.insert(randint(0, len(ls) - 1), chr(randint(0, value - 1)))
    with open(filename, 'w') as f:
        f.write(''.join(ls))
    f.close()


def timeit(func, *args, **kargs):
    begin = time.clock()
    print value, 'occures:', func(*args, **kargs)
    end = time.clock()
    print end - begin


def singlethreading(filename, value):
    count = 0
    for i in range(10):
        with open(filename, 'r') as f:
            for item in f:
                count += item.count(chr(value))
    return count


def multiplethreading(filename, value):
    count = [0]
    def read(value):
        with open(filename, 'r') as f:
            for item in f:
                count[0] += item.count(chr(value))

    threads = []
    for i in range(10):
        t = threading.Thread(target=read, args=(value,))
        threads.append(t)
    for i in range(10):
        threads[i].start()
    for i in range(10):
        threads[i].join()
    return count[0]

if __name__ == '__main__':
    filename = raw_input('Filename: ')
    value = input('Value: ')
    total = input('Total: ')
    maxlen = input('Maxlen: ')
    create(filename, value, total, maxlen)
    print 'Creat File Success.'

    print 'Singe Threading...'
    timeit(singlethreading, filename, value)
    print 'Multiple Threading...'
    timeit(multiplethreading, filename, value)
