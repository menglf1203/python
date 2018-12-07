# /usr/bin/env python
# -*- coding='utf-8' -*-
#
# 基于tcp的socket
import socket
# socket
# 创建socket,封装协议  (IPv4协议      tcp协议  )
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定ip和端口号   bind 接受的参数是元组
a = ('0.0.0.0',3001)     # 127的只有自己能访问，如果是自己的IP地址，都可以访问
s.bind(a)
# 监听端口号  # 数字是最大等待数
s.listen(10)    # 里面填写随意一个数字，最好不要太大
while True:
    # 接收请求
    a,b = s.accept()  # 会产生两个结果 第一个结果a是客户端的连接信息，b是客户端的ip地址和端口号
    print(a)
    print(b)
    # 接收数据
    msg = a.recv(1024)   # 1024代表每次接收最大的字节数   512或者1024
    print(msg.decode('utf-8'))   # decode 解码
    # 发送响应
    reg = 'hello!'
    a.send (reg.encode('utf-8'))   # encode 编码




# 基于udp的socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
a = ('192.168.0.40',3001)
s.bind(a)
while True:
    a,b = s.recvfrom(1024)  # 接收数据
    # 会产生两个结果 第一个结果a是客户端发送的请求数据，b是客户端的ip地址和端口号
    print(a)
    print(a.decode('utf-8'))   # decode 解码
    print(b)
    # 发送响应数据
    msg = 'hello!'
    s.sendto(msg.encode('utf-8'),b)   # encode 编码
