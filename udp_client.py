import socket
import time
address = ("192.168.100.133",31500)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg = "this is test message"
start = time.time()
s.sendto(msg,address)
s.close()
end = time.time()
print end-start

