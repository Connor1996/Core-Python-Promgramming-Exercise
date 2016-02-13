# -*- coding: utf-8 -*-
import string


def test(start, end):
    print "%-8s%-8s%-8s%-8s%-8s" % ("DEC","BIN","OCT","HEX","ASCII")
    print '-' * 40
    len2 = len(str(bin(end)))

    for i in range(start, end + 1):
        print "%-8d%-8s%-8o%-8x%-8s" % (i, '0' * (len2 - len(str(bin(i)))) + bin(i)[2:], i, i, chr(i))

if __name__ == '__main__':
    print '-' * 15
    start = input("\t输入起始值: ")
    end = input("\t输入结束值: ")
    test(start, end)
