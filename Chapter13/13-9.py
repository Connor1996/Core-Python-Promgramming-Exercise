class Queue(object):

    """docstring for Queue"""

    def __init__(self):
        self.__ls = []

    def enqueue(self, obj):
        self.__ls.append(obj)

    def dequeue(self):
        if not isempty():
            self.__ls.pop(0)

    def isempty(self):
        return len(self.__ls) == 0
