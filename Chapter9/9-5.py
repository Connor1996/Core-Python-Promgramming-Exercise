def diff(str1, str2):
    for i in range(len(str1)):
        if (str1[i] != str2[i]) or (i >= len(str2)):
            return i + 1


def filecmp(file1, file2):
    j = 0
    for i, eachLine in enumerate(file1):
        string = file2.next()
        if eachLine != string:
            return (i + 1, diff(eachLine, string))


if __name__ == '__main__':
    f1 = raw_input('Enter the first file: ')
    f2 = raw_input('Enter the second file: ')
    try:
        file1 = open(f1)
    	file2 = open(f2)
    except IOError, e:
        print e
    else:
        result = filecmp(file1, file2)
        if not result:
            print 'the same'
        else:
        	print result
        file1.close()
        file2.close()
