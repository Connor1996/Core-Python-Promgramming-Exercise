def importAs(name):
    return __import__(name)

if __name__ == '__main__':
    sys = importAs('sys')
    print sys.path