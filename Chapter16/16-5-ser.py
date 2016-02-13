from socket import *
from time import ctime
import os

HOST = ''
PORT = 50007
server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

while True:
    print 'Waiting for connection...'
    conn, addr = server.accept()
    print 'Connected by', addr

    while True:
        data = conn.recv(1024)
        if data == 'date':
            data = ctime()
        elif data == 'os':
            data = os.name
        elif data == 'ls':
            data = str(os.listdir(os.curdir))
        else:
            break
        conn.send(data)
    conn.close()
