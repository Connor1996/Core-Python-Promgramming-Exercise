
list1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

num = raw_input('Enter a number: ')

for i in range(len(num)):
	print "%s" % list1[eval(num[i])-1],
	if i != len(num)-1:
		print "%s" %'-',

