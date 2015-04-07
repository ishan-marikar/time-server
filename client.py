import socket
import time
import os
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',55555))
while 1:
    l = s.recv(100)
    t = float(l)
    d = t - time.time()
    if (abs(d) > 1):
        os.system('echo sudo date %s' % time.strftime('%m%d%H%M%Y.%S', time.localtime(t)))
    else:
        print(l,t,d)