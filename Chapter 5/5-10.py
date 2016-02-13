from __future__ import division

def change(num):
	return (num - 32) * (5 / 9)

if __name__ == '__main__':
	num = input('enter a num: ')
	print change(num)