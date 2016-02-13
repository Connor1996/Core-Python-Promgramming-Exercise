def max2(a, b):
    return a if cmp(a, b) > 0 else b


def min2(a, b):
    return a if cmp(a, b) < 0 else b

def my_max(*data):
    max = data[0]
    for item in data[1:]:
        max = max2(max, item)
    return max

def my_min(*data):
    min = data[0]
    for item in data[1:]:
        min = min2(min, item)
    return min


if __name__ == '__main__':
    print max2('82', '1233')
    print min2('82', '1233')
    print max2(82, 1233)
    print min2(82, 1233)
    print my_max('12', '0123', '90')
    print my_min('12', '0123', '90')
    print my_max(1, 9, 4)
    print my_min(1, 9, 4)