import string


class Time60(object):

    'Time60 - track hours and minutes'

    def __init__(self, hr=0, min=0):
        'Time60 constructor - takes hours and minutes'
        if isinstance(hr, basestring):
            t = hr.split(':')
            self.hr = int(t[0])
            self.min = int(t[1])
        else:
            self.hr = hr
            self.min = min

    def __str__(self):
        'Time60 - string representation'
        return '%02d:%02d' % (self.hr, self.min)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, str(self))

    def add60(self, other):
        hr = self.hr + other.hr
        min = self.min + other.min
        carry = min // 60
        min %= 60
        hr += carry
        return (hr, min)

    def __add__(self, other):
        'Time60 - overloading the addition operator'
        return self.__class__(*self.add60(other))

    def __iadd__(self, other):
        'Time60 - overloading in-place addition'
        (self.hr, self.min) = self.add60(other)
        return self

if __name__ == '__main__':
    print Time60()
    print Time60(12,5)
    print Time60(*(10, 30))
    print Time60(**{'hr': 10, 'min': 30})
    print Time60('10:30')
    print `Time60('10:10')`
    print Time60(10, 30) + Time60(8, 45)