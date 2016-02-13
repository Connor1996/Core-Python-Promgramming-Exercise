from socket import *

port = getservbyname('daytime', 'udp')
addr = ('127.0.0.1', port)
conn = socket(AF_INET, SOCK_STREAM)
conn.sendto("something", addr)
data, addr = conn.recvfrom(1024)
if data:
    print data
conn.close()