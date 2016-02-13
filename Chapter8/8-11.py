import string

if __name__ == '__main__':
    count = 1
    nameList = []
    n = input('Enter total number of names: ')
    for i in range(n):
        print 'Please enter name %d: ' % i,
        name = raw_input()
        if ',' in name:
            nameList.append(name)
        else:
            print 'Wrong format...should be Last, First.'
            print 'You have done this %d time(s) alredy. Fixing input...' % count
            count += 1
            name = name.split()
            nameList.append(name[1] + ', ' + name[0])
    print 'The sorted list (by last name) is:'
    for i in sorted(nameList):
        print "\t%s" % i
