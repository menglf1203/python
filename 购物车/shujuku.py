# /usr/bin/env python
# -*- coding:utf-8 -*-
#
# 用数据库命令创建表
#
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
#
#
#
# 从txt文件导入数据库中
#
# import pymysql
#
# a=pymysql.connect(host='192.168.0.145',port=3306,
#                   user='root',password='123456',
#                   charset='utf8')
# b=a.cursor()
#
# b.execute('use test_1;')
# with open(r'C:\Users\meng\Desktop\python\a.txt','r+',encoding='utf-8') as f:
#     aa=f.readline()
#     a=aa.split(',')
#     b.execute('create table biao_1({} char(20),{} int,{} char(10));'.format(a[0],a[1],a[2]))
#     aa = f.readlines()
#     for i in aa:
#         a=i.replace('\n','').split(",")
#         b.execute('insert into biao_1 values("{}","{}","{}");'.format(a[0], a[1], a[2]))
#
# b.execute('select * from biao_1;')
# x=b.fetchall()
# for i in x:
#     print(i)
#
#
# 或者txt到数据库
# #
# a=pymysql.connect(host='192.168.0.193',port=3306,user='root',password='123456',charset='utf8')
# b=a.cursor()
# b.execute('use test_1;')
#
# with open('a.txt','r',encoding='utf-8') as f:
#     bb=f.readline().split(',')
#     b.execute('create table biao_3({} char(10),{} int,{} char(10));'.format(bb[0],bb[1],bb[2]))
#     for i in range(1,31):
#         bb=f.readline()
#         bb=bb.replace('\n','')
#         bb=bb.split(',')
#         b.execute('insert into biao_3 values("{}","{}","{}");'.format(bb[0],bb[1],bb[2]))
# a.commit()
# b.execute('select * from biao_3;')
# c=b.fetchall()
# print(c)
#
#
#
# 从数据库导入txt中
#
# import pymysql
# a=pymysql.connect(host='192.168.0.145',port=3306,
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
#
#
# 将数据库的文件写入到excel表格中
#
# import xlwt
# import pymysql
#
# a=pymysql.connect(host='192.168.0.193',port=3306,user='root',password='123456',charset='utf8')
# b=a.cursor()
#
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet_1')
#
# b.execute('use test_1;')
# b.execute('desc biao;')
# c=b.fetchall()
# for i in range(3):
#     sheet.write(0,i,'{}'.format(c[i][0]))
#
#
# b.execute('select * from biao;')
# c=b.fetchall()
# aa=1
# for i in c:
#     sheet.write(aa,0,'{}'.format(i[0]))
#     sheet.write(aa,1,'{}'.format(i[1]))
#     sheet.write(aa,2,'{}'.format(i[2]))
#     aa+=1
#
# f.save('test1.xls')
# print('over')
#
#
# txt文件中导入到表格
# import xlwt
#
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet_1')
#
# with open(r'C:\Users\meng\Desktop\python\a.txt','r',encoding='utf-8') as x:
#     a=x.read()
#     aa=a.split('\n')
#     bb=0
#     for i in aa:
#         i=i.split(',')
#         sheet.write(bb,0,'{}'.format(i[0]))
#         sheet.write(bb,1,'{}'.format(i[1]))
#         sheet.write(bb,2,'{}'.format(i[2]))
#         bb+=1
# f.save('test.xls')
# print('over')
#
#
# 从excel到数据库
# import pymysql
# import xlrd
#
# aa=pymysql.connect(host='192.168.0.193',port=3306,user='root',password='123456',charset='utf8')
# bb=aa.cursor()
# bb.execute('use test_1;')
#
#
# a=xlrd.open_workbook(r'C:\Users\meng\Desktop\python\test_1.xls')
# sheet=a.nsheets         # 获取有多少个标签页
# sheet=a.sheets()[0]
# b=sheet.row_values(0)
# bb.execute('create table biao_2({} char(10),{} int,{} char(10));'.format(b[0],b[1],b[2]))
# b=sheet.nrows
# for i in range(1,b):
#     b=sheet.row_values(i)
#     bb.execute('insert into biao_2 values("{}","{}","{}");'.format(b[0],b[1],b[2]))
# bb.execute('select * from biao_2;')
# cc=bb.fetchall()
# print(cc)
#
#   删除biao_2
# aa=pymysql.connect(host='192.168.0.193',port=3306,user='root',password='123456',charset='utf8')
# bb=aa.cursor()
# bb.execute('use test_1;')
# bb.execute('drop table biao_2;')
# bb.execute('show tables;')
# cc=bb.fetchall()
# print(cc)
#
#
# 类似xshell，可以无限输入linux命令的
# import paramiko
#
# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname='192.168.0.193',port=22,username='root',password='123456')
#
#
# while True:
#     aa=input('>>>')
#     a,b,c=ssh123.exec_command('{}'.format(aa))
#     print(b.read().decode())
#     if aa=='exit':
#         ssh123.close()  # 断开连接
#         break
#
#
#
# 表格到txt
#
# a=xlrd.open_workbook('test_1.xls')
# sheet=a.sheet_by_name('sheet1')
# b=sheet.row_values(0)
# with open('a.txt','w',encoding='utf-8') as f:
#     f.write('{},{},{}\n'.format(b[0],b[1],b[2]))
# b=sheet.nrows
# for i in range(1,b):
#     c=sheet.row_values(i)
#     with open('a.txt', 'a', encoding='utf-8') as f:
#         f.write('{},{},{}\n'.format(c[0], c[1], c[2]))
#
#
#
# txt到表格
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet1')
# with open('a.txt','r',encoding='utf-8') as x:
#     neirong=x.readline()
#     for i in range(3):
#         sheet.write(0,i,'{}'.format(neirong.split(',')[i]))
#     for i in range(1,30):
#         b=x.readline().split('\n')[0]
#         sheet.write(i, 0, '{}'.format(b.split(',')[0]))
#         sheet.write(i, 1, '{}'.format(b.split(',')[1]))
#         sheet.write(i, 2, '{}'.format(b.split(',')[2]))
# f.save('test_2.xls')
#
#
# 创建十个文件夹，每个文件夹都有文件，每个文件中都有数据，最后在删除
#
# import os
# os.chdir(r'C:\Users\meng\Desktop\aaa')
# for i in range(10):
#     os.mkdir(r'C:\Users\meng\Desktop\aaa\{}'.format(i))
#     with open(r'C:\Users\meng\Desktop\aaa\{}\{}.txt'.format(i,i),'w',encoding='utf-8') as f:
#         f.write('{}'.format(i))
# for i in range(10):
#     os.remove(r'C:\Users\meng\Desktop\aaa\{}\{}.txt'.format(i,i))
#     os.rmdir(r'C:\Users\meng\Desktop\aaa\{}'.format(i))
# print('over')
#
# 判断一个目录下有多少txt文件
#
# import os
# aa=0
# os.chdir(r'C:\Users\meng\Desktop\python')
# a=os.listdir(r'C:\Users\meng\Desktop\python')
# for i in a:
#     b=os.path.splitext(r'C:\Users\meng\Desktop\python\{}'.format(i))
#     if b[1]=='.txt':
#         aa+=1
#
# print(aa)
#
#
# 判断一个文件夹下有多少目录和文件
# import os
# aa=0
# bb=0
# os.chdir(r'C:\Users\meng\Desktop\python')
# a=os.listdir(r'C:\Users\meng\Desktop\python')
# for i in a:
#     if os.path.isdir(i):
#         aa+=1
#     elif os.path.isfile(i):
#         bb+=1
#
# print('目录:{},普通文件:{}'.format(aa,bb))
#



# 输入一个现在化日期（年月日），输出：今年是否为闰年，今天星期几，今天是一年中的第几天
#
# a=input('>>>')
# a=a.split(',')
# aa=time.strptime('{} {} {}'.format(a[0],a[1],a[2]),'%Y %m %d')
# if int(a[0])%100==0:
#     if int(a[0])%400==0:
#         print('闰年,星期{},是一年中的第{}天'.format(aa[-3]+1,aa[-2]))
#     else:
#         print('平年,星期{},是一年中的第{}天'.format(aa[-3]+1,aa[-2]))
# elif int(a[0])%100!=0 and int(a[0])%4==0:
#     print('闰年,星期{},是一年中的第{}天'.format(aa[-3]+1,aa[-2]))
# else:
#     print('平年,星期{},是一年中的第{}天'.format(aa[-3]+1,aa[-2]))


# 输入日期(年月日)，输出日期的前一天
# 计算平年闰年的二月份前一天时间不好算，可以按时间戳去计算一天的秒数(时间戳)是86400
# a=input('>>>')
# a=a.split(',')
# aa=time.strptime('{} {} {}'.format(a[0],a[1],a[2]),'%Y %m %d')
# b=time.mktime(aa)
# b-=86400.0
# print(time.strftime('%Y %m %d',time.localtime(b)))




