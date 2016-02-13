is_leap = lambda num: (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0)

if __name__ == '__main__':
    print filter(is_leap, [2000, 1984, 1996, 1986, 1991])