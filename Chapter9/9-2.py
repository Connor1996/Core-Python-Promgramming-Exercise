N = input("Enter a number: ")
F = raw_input('Enter a file name: ')

f = open(F)
for i, eachLine in enumerate(f):
	print eachLine,
	if i == N - 1:
		break