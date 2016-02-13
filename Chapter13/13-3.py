class MoneyFmt(object):

    def __init__(self, value=0.0):
        self.value = float(value)

    def updata(self, value=None):
        self.value = float(value)

    def __str__(self):
        pre = '$' if self.value >= 0 else '-$'
        return pre + str(round(abs(self.value), 2))

    def __nonzero__(self):
        return self.value > 0.5

    def __repr__(self):
        return self.value

if __name__ == '__main__':
    money = MoneyFmt(1234567.8901)
    print money
