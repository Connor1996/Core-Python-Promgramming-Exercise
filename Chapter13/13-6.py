from math import sqrt

class Point(object):

    """docstring for Point"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)


class Line(object):

    """docstring for Line"""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def __str__(self):
        return '(%s, %s)' % (str(self.p1), str(self.p2))

    __repr__ = __str__

    def slope(self):
        try:
            k = float(self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        except ZeroDivisionError:
            k = None
        return k

    def length(self):
        return sqrt((self.p2.y - self.p1.y) ** 2 + (self.p2.x - self.p1.x) ** 2)


if __name__ == '__main__':
    l = Line(2, 3, 4, 6)
    print l.length()
    print l.slope()