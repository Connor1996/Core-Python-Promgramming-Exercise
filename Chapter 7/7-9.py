# -*- coding: utf-8 -*-
import string

def tr(srcstr, dststr, string, flag):
	dict = {}
	str = ''
	if len(srcstr) == len(dststr):
		if flag == 'y':
			for i, j in zip(srcstr, dststr):
				dict.setdefault(i, j)
			for i in string:
				if i in srcstr:
					str += dict[i]
				else:
					str += i
		else:
			for i, j in zip(srcstr.lower(), dststr):
				dict.setdefault(i, j)
			for i in string:
				if i.lower() in srcstr:
					str += dict[i]
				else:
					str += i
	else:
		if flag == 'y':
			for i, j in zip(srcstr[:len(dststr)], dststr):
				dict.setdefault(i, j)
			for i in string:
				if i in dict:
					str += dict[i]
				elif i not in srcstr:
					str += i
		else:
			for i, j in zip(srcstr[:len(dststr)], dststr):
				dict.setdefault(i, j)
			for i in string:
				if i.lower() in dict:
					str += dict[i]
				elif i not in srcstr:
					str += i
	return str

if __name__ == '__main__':
	srcstr = raw_input('Enter a srcstr: ')
	dststr = raw_input('Enter a dststr: ')
	string = raw_input('Enter a string: ')
	print '是否区分大小写? Y/N '
	flag = raw_input()
	print tr(srcstr, dststr, string, flag)