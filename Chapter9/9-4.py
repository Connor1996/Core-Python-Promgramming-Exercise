F = raw_input('Enter a file name: ')
with open(F) as f:
	for i, eachLine in enumerate(f):
		if (i + 1) % 25 == 0:
			raw_input('Press any key to continue...')
		print eachLine,
