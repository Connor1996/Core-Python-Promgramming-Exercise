try:
	f = open('test.txt')
except IOError, e:
	print e
else:
	for eachLine in f:
		if eachLine.startswith('#'):
			continue
		elif '#' in eachLine:
			index = eachLine.find('#')
			print eachLine[:index]
		else:
			print eachLine,
	f.close()