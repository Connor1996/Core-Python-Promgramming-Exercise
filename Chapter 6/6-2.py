import string
import keyword

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test? ')

if myInput in keyword.kwlist:
	print 'okay as a keyword'
else:
	if len(myInput) >= 1:
		if myInput[0] not in alphas:
			print '''invaild: first symbol must be alphabetic'''
		else:
			for otherChar in myInput[1:]:
				if otherChar not in alphas + nums:
					print '''invalid: remaining symbols must be alphabetic'''
					break
			else:
				print 'okay as an identifier'
