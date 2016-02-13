import operator

def average(numlist):
    total = reduce(operator.add, numlist)
    return float(total) / len(numlist)

if __name__ == '__main__':
    print average([i for i in range(1, 11)])