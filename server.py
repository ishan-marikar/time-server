import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
while 1:
    s.sendto(str(time.time()), ('255.255.255.255',55555))
    time.sleep(10-(time.time() % 10))