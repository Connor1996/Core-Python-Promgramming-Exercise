def score(num):
	if 90 <= num <= 100:
		return 'A'
	elif 80 <= num <= 89:
		return 'B'
	elif 70 <= num <= 79:
		return 'C'
	elif 60 <= num <= 69:
		return 'D'
	else: 	
		return 'F'

if __name__ == '__main__':
	num = input('enter a score: ')
	print score(num)