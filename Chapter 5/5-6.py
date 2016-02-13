def calculate(a, s, b):
    if s == '*':
        return a * b
    elif s == '+':
        return a + b
    elif s == '-':
        return a - b
    elif s == '/':
        return a // b
    elif s == '%':
        return a % b
    elif s == '**':
        return a ** b
    else:
        return 0

if __name__ == '__main__':
    ss = raw_input('enter a calculation: ')
    if len(ss) == 3:
        print calculate(float(ss[0]), ss[1], float(ss[2]))
    else:
        print calculate(float(ss[0]), ss[1:3], float(ss[3]))


