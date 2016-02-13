import os
import time
import shelve


class UserData(object):

    """docstring for UserData"""

    def __init__(self, dbfile):
        self_db = {}
        if os.path.exists(dbfile):
            self_db = shelve.open(dbfile, 'r')
        self_dbfile = dbfile

    def __del__(self):
        data = shelve.open(self_dbfile, 'c')
        data.updata(self_db)
        data.close()

    def updata(self, name, passwd):
        self_db[name] = [passwd, time.time()]

    def delete(self, name):
        del self_db[name]

    def login(self, name, passwd):
        if self_db[name][0] == passwd:
            self_db[name][1] = time.time()
            return True
        return False

    def listall():
        for name in self_db:
            print name, self_db[name][0], time.ctime(self_db[name][1])

