class User(object):

    def __init__(self):
        self.ls = []

    def append(self, cart):
        self.ls.append(cart)

    def delete(self, cart):
        self.ls.remove(cart)


class Item(object):

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart(object):

    def __init__(self):
        self.ls = {}

    def append(self, item, count):
        if item not in self.ls:
            self.ls[item] = count
        else:
            self.ls[item] += count

    def delete(self, item, count):
        if (item in self.ls) and (self.ls[item] >= count):
            self.ls[item] -= count
        if self.ls[item] == 0:
            self.ls.pop(item)
