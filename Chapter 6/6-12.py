import string

def findchr(string, char):
	for i, j in enumerate(string):
		if j == char:
			return i
	else:
		return -1

def rfindchr(string, char):
	myString = string[::-1]
	for i, j in enumerate(mystring):
		if j == char:
			return len(string) - i - 1
	else:
		return -1

def subchr(string, origchar, newchar):
	newString = ''
	for i in string:
		if i == origchar:
			newString += newchar
		else:
			newString += i

	return newString



