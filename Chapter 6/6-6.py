import string

def myStrip(str):
	str1 = ''
	str2 = ''
	for i in range(0, len(str)):
		if str[i] != ' ':
			str1 = str[i:]
			break
		else:
			pass
	for i in range(len(str1)-1, 0, -1):
		if str1[i] != ' ':
			str2 = str1[:i+1]
			break
		else:
			pass
	return str2

if __name__ == '__main__':
	str = raw_input('enter a string: ')
	print myStrip(str)