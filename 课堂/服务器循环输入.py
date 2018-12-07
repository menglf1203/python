# /usr/bin/env python
# -*- coding:utf-8 -*-

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
a = ('192.168.0.40',3001)
s.bind(a)
while True:
    a,b = s.recvfrom(1024)  # 接收数据  会产生两个结果 第一个结果a是客户端发送的请求数据，b是客户端的ip地址和端口号
    c=a.decode('utf-8')   # decode 解码
    print(c)
    # 发送响应数据
    aaa=input('>>>')
    msg = '{}'.format(aaa)
    s.sendto(msg.encode('utf-8'),b)   # encode 编码





