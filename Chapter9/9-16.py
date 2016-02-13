import string
from os import linesep

def nearest(string):
    index = -1
    if not string[80].isspace():
        index = string.rfind(' ', 0, 79)
    return index


def wrap(filename):
    f = open(filename)
    Is = [item for item in f]
    for i, item in enumerate(Is):
        if len(item) > 80:
            index = nearest(item)
            if index == -1:
                tail = item[80:]
                Is[i] = item[:80]
            else:
                tail = item[index:]
                Is[i] = item[:index]
            if i + 1 < len(Is):
                Is[i + 1] = tail.strip() + Is[i + 1]
            else:
                Is.append(tail)
    string = linesep.join(Is)
    with open(filename, 'w') as f:
        f.write(string)

if __name__ == '__main__':
    filename = raw_input('file name: ')
    wrap(filename)
