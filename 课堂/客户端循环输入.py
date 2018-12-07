# /usr/bin/env python
# -*- coding:utf-8 -*-

import socket

# udp的客户端
# 创建socket 封装协议
soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 发送请求
a=('192.168.0.40',3001)

while True:
    reg=input('>>>')
    soc.sendto(reg.encode('utf-8'),a)
    # 接收响应
    msg=soc.recv(1024)
    print(msg.decode('utf-8'))
    if reg=='end':
        break

