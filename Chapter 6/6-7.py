# -*- coding: utf-8 -*-
#!/usr/bin/env python

#输入一个数字
num_str = raw_input('Enter a number: ')

#将数字转化为字符串
num_num = int(num_str)

#生成一个从1到num_num的列表
fac_list = range(1, num_num+1)
print "BEFORE:", fac_list

#初始化i
i = 0

#遍历列表
while i < len(fac_list):

	#判断是否能被整除
	if num_num % fac_list[i] == 0:
		del fac_list[i]
	else:
		#循环迭代器加一
		i = i + 1

#输出不能整除num_num的数字
print "AFTER:", fac_list
