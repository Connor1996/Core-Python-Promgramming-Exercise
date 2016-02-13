from socket import *

HOST = ''
PORT = 50007
ADDR = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
while True:
    print 'Waiting for connection...'
    conn, addr = server.accept()
    print 'Conneted by', addr

    while True:
        data = raw_input('> ')
        if not data:
            break
        conn.send(data)
        data = conn.recv(1024)
        if not data:
            break
        print data

    conn.close()

server.close()