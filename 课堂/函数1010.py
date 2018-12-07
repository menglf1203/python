# /usr/bin/env python
# -*- coding:utf-8 -*-


# def quchong(a):
#     for i in a:
#         b=a.count(i)
#         for j in range(b-1):
#             a.remove(i)
#     # a.sort()
#     print(a)


# def quchong(a):
#     c=[]
#     for i in a:
#         if i not in c:
#             c.append(i)
#     # c.sort()
#     print(c)




# quchong([4,4,4,234,456,6,6,6,6,34,6,243,243])

#函数的作用域
# a=8      #全局变量，后面可以被覆盖
# def aaaa(b=2):
#     if b<10:
#         global a  #如果不加global就是一个局部变量
#         a=5      #将a局部变量变成全局变量
#         print(a)
#     return a     #将结果返回给调用者
# aaaa()    #只是来调用函数的，本身结果为空
# print(aaaa()+1)   #如果不用return调用a,这就会报错
#这个会执行两次，aaaa()会执行一次，+1会在执行一次。


#函数名=lambda：表达式


# print(__name__)            #在本文件执行是__main__，在另一个文件执行是day1010
# aa=lambda:3+4
# if __name__=='__main__':   #在这个文件中执行是会显示的，在另一个文件中不会显示的
#     print('hello')
#     print('klalal')
#     jia = lambda aa=3, bb=3: aa + bb

# aa=lambda x,y:x*y       #必须参数
# bb=lambda x=5,y=5:x-y   #默认参数
# print(aa(6,6))
# print(bb())


# jia=lambda aa=3,bb=3:aa+bb


# jian=lambda aa,bb:aa-bb
# cheng=lambda aa,bb:aa*bb
# chu=lambda aa,bb:aa/bb
# a=input('请输入两个数')
# if '+' in a:
#     a=a.split('+')
#     print(jia(int(a[0]),int(a[1])))
# if '-' in a:
#     a = a.split('-')
#     print(jian(int(a[0]),int(a[1])))
# if '*' in a:
#     a = a.split('*')
#     print(cheng(int(a[0]),int(a[1])))
# if '/' in a:
#     a = a.split('/')
#     print(chu(int(a[0]),int(a[1])))




# a=[]       #普通的添加列表
# for i in range(10):
#     a.append(i)
#
# b=[x-1 for x in range(10) if x>5] #列表推导式
#
# print(a)
# print(b)


# a=['{}*{}={}'.format(j,i,i*j) for i in range(1,10) for j in range(1,i+1)]
# print(a)


# a=[12,123,456,6577,32,21]
# print(max(a))
# print(min(a))


#
# print(hex(a))    #改成十六进制
# print(oct(a))    #改成八进制
# print(bin(a))    #改成二进制
# print(int(0o1111))   #也可以手动填写


# a=divmod(18,4)
# print(a)
# print(type(a))
# b,c=divmod(18,4)
# print(b,c)


# #十进制转十六进制
# n=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# a=int(input('请输入'))
# c=''
# while True:
#     b=a%16
#     c+=n[b]
#     a//=16
#     if a==0:
#         break
# print(c[::-1])


#因数
# for i in range(1,1000):
#     a=0
#     for j in range(1,i):
#         if i%j==0:
#             a+=j
#     if a==i:
#         print(i)

# a=input('请输入四位数')
# c=set()
# for i in range(4):
#     for j in range(4):
#         for q in range(4):
#             if int(a[i])!=int(a[j]) and int(a[i])!=int(a[q]) and int(a[q])!=int(a[j]):
#                 c.add('{}{}{}'.format(a[i],a[j],a[q]))
# print(c)


#打印列表中的第一大和第二大的数
# a=[23,454,234,234,454,23,3425,3425]
# # b=[]
# c=len(a)
# t=0
# for j in range(0,c):
#     for q in range(j+1,c):
#         if a[j]>a[q]:
#             t=a[j]
#             a[j]=a[q]
#             a[q]=t
# for q in a:
#     if a[-1]==q:
#         print(q)
#     s = a.count(a[-1])
#     if a[c - s - 1] == q:
#         print(q)



# a=[23,454,234,234,454,23,3425,3425]
# b=[]
# c=len(a)
# t=0
# for j in range(0,c):
#     for q in range(j,c):
#         if a[j]>a[q]:
#             t=a[j]
#             a[j]=a[q]
#             a[q]=t
# for q in a:
#   if max(a)==q:
#         print(q)
# for j in a:
#   s = a.count(a[-1])
#   if a[c - s - 1] == j:
#          print(j)

#
# a=input(">>>")
# l=a.split(",")
# b=[]
# t=0
# for e,r in enumerate(l):
#     l[e]=int(r)
# c=len(l)
# for j in range(0,c):
#     for q in range(j,c):
#         if l[j]>l[q]:
#             t=l[j]
#             l[j]=l[q]
#             l[q]=t
# for q in l:
#   if max(l)==q:
#         print(q)
# for j in l:
#   s = l.count(l[-1])
#   if l[c - s - 1] == j:
#          print(j)
#
def jiujiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print('{}*{}={}\t'.format(j,i,i*j),end='')
        print()
def zhishu(a,b):
    for i in range(a,b):
        for j in range(2,i+1):
            if i%j==0:
                if i==j:
                    print(i)
                else:
                    break

def jiecheng(a):
    b=0
    for i in range(1,a+1):
        c = 1
        for j in range(1,i+1):
            c*=j
        b+=c
    print(b)

def sanjiao(a):
    a.sort()
    if a[0]+a[1]>a[2]:
        if a[0]**2+a[1]**2==a[2]**2:
            print('zhijiao')
        elif a[0]**2+a[1]**2<a[2]**2:
            print('dunjiao')
        else:
            print('ruijiao')
    else:
        print('bushi')

def quchong(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)

    print(b)
    bb=len(b)
    tt=0
    for j in range(bb):
        for h in range(bb):
            if b[j]<b[h]:
                tt=b[j]
                b[j]=b[h]
                b[h]=tt
    print(b)

def huiwen():
    a=input('>>>')
    b=len(a)//2
    for i in range(b+1):
        if a[i]!=a[-i-1]:
            print('bushi')
            break
        else:
            if i==b:
                print('shi')
def xuanze():
    a = input('>>>').split(',')
    b=len(a)
    tt=0
    for i in range(b):
        for j in range(i+1,b):
            if a[i]>a[j]:
                tt=a[i]
                a[i]=a[j]
                a[j]=tt
    print(a)
import random

def sanci():
    a=random.randrange(1,10)
    for i in range(3):
        b = int(input('>>>'))
        if b==a:
            print('你真棒！')
            break
        elif b<a:
            print('小了！')
            continue
        else:
            print('大了！')
            continue

def shuixianhua():
    for i in range(100,1000):
        if (i//100)**3+(i//10%10)**3+(i%10)**3==i:
            print(i)

def diyida():
    a=input('>>>').split(',')
    b=max(a)
    bb=a.count(b)
    for i in range(bb):
        print(b)
        a.remove(b)
    c=max(a)
    cc=a.count(c)
    for j in range(cc):
        print(c)


def strbianint():
    a=input('>>>')
    b=a[::-1]
    aa=0
    for i,j in enumerate(b):
        for h in range(10):
            if h==int(i):
                aa+=int(j)*10**h
    print(aa)

def sanweishu():
    a=input('>>>')
    b=set()
    for i in a:
        for j in a:
            for h in a:
                if int(i)!=int(j) and int(j)!=int(h) and int(i)!=int(h):
                    b.add('{}{}{}'.format(i,j,h))
    print(b)

def nuo():
    a=[1,2,3,4,4]
    b=a[0]
    c=len(a)
    for i in range(c-1):
        a[i]=a[i+1]
    a[-1]=b
    print(a)

def shiliu():
    a=int(input('>>>'))
    b=''
    aaa=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    while True:
        aa=a%16
        a //= 16
        b+=aaa[aa]
        if a==0:
            break
    print(b[::-1])


def yinshu():
    for i in range(2,1000):
        a=0
        for j in range(1,i):
            if i%j==0:
                a+=j
        if a==i:
            print(i)

def zuida():
    a=[123,5,4,56,45,4]
    b=max(a)
    bb=a.index(b)
    a[bb], a[-1] = a[-1], a[bb]
    c=min(a)
    cc=a.index(c)
    a[0],a[cc]=a[cc],a[0]
    print(a)


def jiaru():
    a=[4,8,22,98,465]
    b=int(input('>>>'))
    for i in a:
        if b<i:
            c=a.index(i)
            a[c]=b
            break
    if b>a[-1]:
        a.append(b)
    print(a)

import paramiko

# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh123.connect(hostname='192.168.0.43',port=22,username='root',password='123456')
# a,b,c=ssh123.exec_command('ls -al')
# print(b.read().decode())
# ssh123.close()

# ssh123=paramiko.Transport(('192.168.0.43',22))
# ssh123.connect(username='root',password='123456')
# sftp123=paramiko.SFTPClient.from_transport(ssh123)
#
# import smtplib
# import email.mime.text
# import email.mime.multipart
#
# sender='meng1203@126.com'
# recver='1461633952@qq.com'
# server='smtp.126.com'
# passwd='meng123823'
#
# yj=email.mime.multipart.MIMEMultipart()
# yj['from']=sender
# yj['to']=recver
# yj['subject']='2018年11月1日'
# text="""
# 重温仙剑奇侠传
# 很早看过的
# 再看一遍啦
#
# """
# text=email.mime.text.MIMEText(text)
# yj.attach(text)
#
# smtp123=smtplib.SMTP_SSL(server,465)
# smtp123.login(sender,passwd)
# smtp123.sendmail(sender,recver,yj.as_string())
# smtp123.close()





