from socket import *

HOST = 'www.baidu.com'
PORT = 80
ADDR = (HOST, PORT)

print 'Creating socket ...'
client = socket(AF_INET, SOCK_STREAM)
print 'Done.'

print 'Connecting to ...'
client.connect(ADDR)
print 'Done.'

client.send('GET /index.html HTTP/1.0\n\n')
print 'Request has already sent.'
print '-' * 40
data = client.recv(4096)
print data

client.close()
