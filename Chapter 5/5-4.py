# -*- coding: utf-8 -*-

def year(num):
	if (num % 4 == 0 and num % 100 != 0) or (num % 4 and num % 100):
		return '这是闰年'
	else:
		return '这不是闰年'

if __name__ == '__main__':
	num = input('enter a year: ')
	print year(num)