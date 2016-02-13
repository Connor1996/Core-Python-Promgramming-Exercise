import string

num1 = []
num2 = []

myInput = raw_input()

for i in myInput:
	num1.append(int(i))
	num1.append(i)

num1.sort()
num1.reverse()
num2.sort()
num2.reverse()

print num1
print num2