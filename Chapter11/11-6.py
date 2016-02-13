def printf(fmt, *varlist):
    print fmt % varlist

if __name__ == '__main__':
    printf("%d-%d-%s", 2016, 2, '5')