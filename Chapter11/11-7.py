def my_zip(list1, list2):
    assert len(list1) == len(list2)
    return map(None, list1, list2)

if __name__ == '__main__':
    print my_zip([1, 2, 3], ['abc', 'def', 'ghi'])