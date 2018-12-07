# /usr/bin/env python
# -*- coding:utf-8 -*-
# import pymysql

#连接数据库
# a=pymysql.connect(host='192.168.0.173',
#                 port=3306,user='root',
#                 password='123456',charset='utf8')

# 创建游标
# b=a.cursor()   #指挥者
# b.execute('show databases;')    #执行sql语句,一个只能写一个
# b.execute('use test_1;')
# b.execute('show tables;')
# b.execute('show tables;')
# b.execute('select * from biao;')
# print(b.fetchmany(1))       # 默认读取第一个，可以写数字自定义读取内容(元组)
# print(b.fetchall())        # 读取上一句sql语句的结果(元组)
                           # 如果fetchall在下面，那剩下的结果都会被读取
# print(b.fetchone())        # 每次只读取一个结果，本身有迭代功能
# print(b.fetchone())
# print(b.fetchone())
# print(b.fetchone())
# print(b.fetchone())
# b.execute('create database test_1;')
# b.execute('use test_1;')
# b.execute('create table biao(姓名 varchar(30),年龄 int,班级 varchar(10));')
# list1=['小明',1,'大班']
# for i in range(30):
#     b.execute('insert into biao values("{}",{},"{}");'.format(list1[0],list1[1]+i,list1[2]))
#     a.commit()
# b.execute('insert into biao1 values("小明",10,"大班");')




# import pymysql                 #使用模块
# a=pymysql.connect(host='192.168.0.173',     #连接数据库
#                 port=3306,user='root',
#                 password='123456',charset='utf8')
#
# b=a.cursor()   #指挥者
# b.execute('use test_1;')
# b.execute('desc biao;')          #表头读取到txt中
# bb=b.fetchall()
# with open('a.txt', 'w', encoding='utf-8') as f:
#     f.write('{},{},{}'.format(bb[0][0],bb[1][0],bb[2][0]))
# b=a.cursor()
# b.execute('select * from biao')  #内容读取到txt文件中
# a=b.fetchall()
# for i in a:
#     with open('a.txt','a+',encoding='utf-8') as f:
#         f.write('\n'+'{},{},{}'.format(i[0],i[1],i[2]))
# print('over')

#用数据库命令创建表

# def sjk():
#     import pymysql
#     a=pymysql.connect(host='192.168.43.54',
#                       port=3306,user='root',
#                       password='123456',charset='utf8')
#     b=a.cursor()
#     print('请输入正确的命令')
#     while True:
#         yj=[]
#         b.execute('show databases;')
#         b.execute('use test_1;')
#         sr=input('>>>')
#         if sr=='exit':
#             break
#         else:
#             yj.append(sr)
#             for i in yj:
#                 b.execute('%s'%(i))
#             print(b.fetchall())
# sjk()



# b=a.cursor()
# b.execute('show databases;')
# b.execute('use test_1;')
# b.execute('create table biao1(姓名 varchar(20),年龄 int,性别 char(10),成绩 int);')
# list=['小明',10,'男',20]
# b.execute('insert into biao1 values("{}",{},"{}",{});'.format(list[0],list[1],list[2],list[3]))
# b.execute('select * from biao1;')
# c=b.fetchall()
# print(c)
# for i in c:
#     with open('a.txt','a',encoding='utf-8') as f:
#         f.write('{},{},{}'.format(i[0],i[1],i[2]))

#
# import pymysql
# a=pymysql.connect(host='192.168.0.181',port=3306,
#                   user='root',password='123456',
#                   charset='utf8')
#
# b=a.cursor()
# b.execute('show databases;')
# b.execute('use test_1;')
# # b.execute('insert into biao values("小花",12,"小班")')
# # b.execute('delete from biao where 姓名="小花";')
# # b.execute('update biao set 姓名="小花" where 年龄=30;')
# b.execute('desc biao;')
# c=b.fetchall()
# with open(r'C:\Users\meng\Desktop\a.txt','a',encoding='utf-8') as f:
#     f.write('{},{},{}\n'.format(c[0][0],c[1][0],c[2][0]))
#
#
# b.execute('select * from biao;')
# for i in b.fetchall():
#     with open(r'C:\Users\meng\Desktop\a.txt','a',encoding='utf-8') as f:
#         f.write('{},{},{}\n'.format(i[0],i[1],i[2]))
# print('over')




