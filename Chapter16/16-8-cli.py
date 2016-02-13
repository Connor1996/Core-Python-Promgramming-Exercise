from socket import *

HOST = '127.0.0.1'
PORT = 50007
ADDR = (HOST, PORT)

client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    client.send(data)
    data = client.recv(1024)
    if not data:
        break
    print data

client.close()