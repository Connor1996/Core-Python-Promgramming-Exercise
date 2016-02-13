import string

str1 = raw_input('enter the first string: ')
str2 = raw_input('enter the second string: ')

# output string
for i in str1:
	print i,
print
for i in str1[::-1]:
	print i,
print
for i in str2:
	print i,
print
for i in str2[::-1]:
	print i,

# compare the two strings
for i, j in zip(str1, str2):
	if i != j:
		print 'no'
		break
else:
	print 'yes'

# check the string whether is palindorom or not
if cmp(str1, str1[::-1]):
	print 'it is a palindorom'
else:
	print 'it is not a palindorom'

# construct a palindorom and output
print str2 + str2[::-1]