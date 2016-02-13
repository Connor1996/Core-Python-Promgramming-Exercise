from socket import *

HOST = raw_input('HOST: ')
if HOST == '':
    HOST = '127.0.0.1'
PORT = raw_input('PORT: ')
if PORT == '':
    PORT = 21568
else:
    PORT = eval(PORT)
BUFSIZ = 1024
ADDR = (HOST, PORT)
print ADDR

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data

tcpCliSock.close()
