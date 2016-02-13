class Stack(object):
    """docstring for Stack"""
    def __init__(self):
        self.__Is = []

    def push(self, obj):
        self.__Is.append(obj)

    def pop(self):
        if not isEmpty():
            return self.__Is.pop()

    def isEmpty(self):
        return len(self.__Is) == 0

    def peek(self):
        return self.__Is[len(self.__Is) - 1]


