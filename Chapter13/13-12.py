class Message(object):

    def __init__(self, info='', isbroad=False, to='', froms=''):
        self.info = info
        self.isbroad = isbroad
        self.to = to
        self.froms = froms

    def __str__(self):
        if self.isbroad:
            msg = '%s says to everyone: %s' % (self.froms, self.info)
        else:
            msg = '%s says to %s: %s' % (self.froms, self.to, self.info)
        return msg


class User(object):

    def __init__(self, name='', sex=True, age=18):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return '%s %s %s' % (self.name, self.sex, self.age)

    def say(self, room, info, to=''):
        if to == '':
            msg = Message(info, True, '', self.name)
        else:
            msg = Message(info, False, to, self.name)
        room.receive(msg)

    def hear(self, msg):
        print msg

    def createroom(self, name):
        return Room(name)


class Room(object):

    def __init__(self, name):
        self.name = name
        self.userlist = []

    def add(self, user):
        self.userlist.append(user)

    def receive(self, msg):
        if msg.isbroad:
            print msg
        else:
            for user in self.userlist:
                if user.name == msg.to:
                    user.hear(msg)

if __name__ == '__main__':
    user1 = User('Tom', True, 16)
    user2 = User('Lily', False, 15)
    user3 = User('Lucy', False)

    room = user1.createroom('chatting room')
    room.add(user1)
    room.add(user2)
    room.add(user3)

    user1.say(room, 'Hi, Lily', 'Lily')
    user2.say(room, 'Hello, Tom', 'Tom')
    user3.say(room, 'Hey, you two')
