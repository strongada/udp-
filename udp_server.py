import socket
caddress = "192.168.100.239"
address = ("192.168.100.133",31500)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(address)

while True:
    data,addr = s.recvfrom(2048)
    if addr[0] == caddress:
       print "received:",data,"from",addr
