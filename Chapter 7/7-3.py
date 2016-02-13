import string

dict = {'a': 1, 'c': 3, 'd': 4, 'b': 2}

dict_key = sorted(dict.items(), key=lambda value: value[0])

for i, j in dict_key:
    print "%s:%d" % (i, j)

dict_value = sorted(dict.items(), key=lambda value: value[1])

for i, j in dict_value:
    print "%s:%d" % (i, j)
