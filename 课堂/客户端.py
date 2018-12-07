# /usr/bin/env python
# -*- coding:utf-8 -*_

import socket
# tcp的客户端
# 创建socket 封装协议
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接服务器
soc.connect(('192.168.0.40',3001))
# 发送请求
aaa='你好啊！'
soc.send(aaa.encode('utf-8'))
# 接收响应
msg=soc.recv(1024)
print(msg.decode('utf-8'))



# udp的客户端
# 创建socket 封装协议
soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 发送请求
a=('192.168.0.40',3001)
reg='你好啊！'
soc.sendto(reg.encode('utf-8'),a)
# 接收响应
msg=soc.recv(1024)
print(msg.decode('utf-8'))