F = raw_input('Enter a file name: ')
with open(F) as f:
	print len(f.readlines())