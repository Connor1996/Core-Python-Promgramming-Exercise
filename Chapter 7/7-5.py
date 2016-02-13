#!/usr/bin/env python
import time
import string

db_passwd = {}
db_time = {}


def login():
    words = string.letters + string.digits
    while True:
        name = raw_input('login: ')
        for eachChar in name:
            if eachChar not in words:
                print 'invalid word(%s) for name' % eachChar
                break
        else:
            break
    pwd = raw_input('passwd: ')
    if db_passwd.has_key(name):
        if db_passwd[name] == pwd:
            print 'welcome back', name
            nowTime = time.time()
            if nowTime - db_time[name] < 4 * 60 * 60:
                print 'You already logged in at: %s' % db_time[name]
            db_time[name] = nowTime
        else:
            print 'login incorrect'
    else:
        answer = raw_input("Are you a new user? Y/N ").lower()
        if answer == 'y':
            db_passwd[name] = pwd
            db_time[name] = time.time()
        else:
            "invalid user's name"


def administrate():
    menu = '''
(D)elete a user
(L)ist all the user's name and password
Enter choice: '''
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(menu).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'dlq':
                print 'invalid option, try again'
            else:
                chosen = True
        if choice == 'q':
            done = True
        if choice == 'd':
            user = raw_input('Enter the name of user that you want to delete')
            while True:
                if db_passwd.has_key(user):
                    del db_passwd[user]
                    del db_time[user]
                    break
                else:
                    print "invalid user's name, try again"
        if choice == 'l':
            print db_passwd


def showmenu():
    prompt = '''
(L)ogin
(A)dministrate
(Q)uit
Enter choice: '''

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'laq':
                print 'invalid option, try again'
            else:
                chosen = True
        if choice == 'q':
            done = True
        if choice == 'a':
            administrate()
        if choice == 'l':
            login()

if __name__ == '__main__':
    showmenu()
