#!/usr/bin/env python
#--coding:utf-8--

import threading,time
import socket
#创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址端口
s.bind(("127.0.0.1",9999))
#监听端口,传入的参数指定等待连接的最大数量
s.listen(5)
print("Waiting for connection...")

#sock参数为sock对象
def tcplink(sock,addr):
    print("Accept new connection from %s:%s..." % addr)
    sock.send("Welcome!")
    while True:
        data = sock.recv(1024)
        time.sleep(5)
        if data == "exit" or not data:
            break
        sock.send("Hello,%s!" % data)
    sock.close()
    print("connection from %s:%s closed." % addr)

while True:
    #接受一个新连接
    sock,addr = s.accept()
    #创建新线程来处理tcp连接
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
