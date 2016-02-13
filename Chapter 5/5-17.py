import random

if __name__ == '__main__':
	N = random.randint(1, 100)
	list = []
	for i in range(N):
		n = random.randint(0, 2 ** 32 - 1)
		list.append(n)
	list.sort()
	print list
