import string


def delspace(filename):
    func = lambda string: string.strip()
    with open(filename, 'r+') as f:
        Is = map(func, f)
        f.seek(0)
        f.write(''.join(Is))

if __name__ == '__main__':
    delspace('test.txt')