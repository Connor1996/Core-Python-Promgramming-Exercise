import string

dict1 = {'a':1, 'b':2, 'c':3}
myDict = {}

for key in dict1.keys():
	myDict.setdefault(dict1[key], key)

print myDict