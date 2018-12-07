# /usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
import xlrd
import xlutils
import paramiko
import xlwt


# 打开一个文件
# a=xlrd.open_workbook('test_1.xls')
# # 两种获取标签页的方式 1.通过索引来获取
# sheet=a.nsheets         # 获取有多少个标签页
# sheet=a.sheets()[0]     # 索引获取标签页，获取第一个
# print(sheet.row_values(0))   # row_values() 读取第几行的内容，第一行从0开始
# b=sheet.nrows     # 获取文件中有多少行
# print(b)
#
# for i in range(b):
#     print(sheet.row_values(i))
#
# c=sheet.ncols                # 获取有多少列
# cc=sheet.col_values(0)       # col_values() 读取第几列的内容，第一列从0开始

# for i in range(c):
#     print(sheet.col_values(i))

# b=sheet.cell(0,0).value     # 读取某个单元格的内容
# print(b)

# # 2.通过标签页的名称来获取
#
# b=a.sheet_names()   # 获取所有标签页的名称
# sheet=a.sheet_by_name('sheet_1')  # 括号中填写操作的标签页
# c=sheet.nrows
#
# for i in range(c):
#     print(sheet.row_values(i))

# aa=pymysql.connect(host='192.168.0.193',port=3306,user='root',password='123456',charset='utf8')
# bb=aa.cursor()
# bb.execute('use test_1;')
# bb.execute('drop table biao_2;')
# bb.execute('show tables;')
# cc=bb.fetchall()
# print(cc)


#
# a=xlrd.open_workbook('test_1.xls')
# sheet=a.nsheets         # 获取有多少个标签页
# sheet=a.sheets()[0]
# b=sheet.nrows
#
# bb.execute('create table biao_2({} char(10),{} int,{} char(10));'.format(b[0],b[1],b[2]))
#
# for i in range(1,b):
#     b=sheet.row_values(i)
#     bb.execute('insert into biao_2 values("{}","{}","{}");'.format(b[0],b[1],b[2]))
# bb.execute('select * from biao_2;')
# cc=bb.fetchall()
# print(cc)

# excel表格追加
#
# from xlutils.copy import copy
# # from 文件夹名.文件名 import 函数名
#
# a=xlrd.open_workbook('test.xls')
# # 复制文件
# new_a=copy(a)
# # xlutils只能操作复制的文件 不能操作原文件
# sheet=new_a.get_sheet(0)   # 通过索引来获取
# sheet.write(5,5,'66666')
# new_a.save('test.xls')
#
# from xlutils.copy import copy
# a=xlrd.open_workbook('1234.xls')
# aa=copy(a)
# sheet=aa.get_sheet(0)
#
# sheet.write(0,3,'成绩')
# for i in range(11,21):
#     sheet.write(i,0,'小花')
#     sheet.write(i,1,'{}'.format(i))
#     sheet.write(i,2,'小班')
#     sheet.write(i,3,'{}'.format(i+40))
# aa.save('1234.xls')






#
# a=xlrd.open_workbook('test.xls')
# sheet=a.sheet_names()
# sheet=a.sheet_by_name('sheet')
# b=sheet.nrows
# print(b)
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
# #######################################################3
# x=pymysql.connect(host='192.168.0.193',port=3306,user='root',password='123456',charset='utf8')
# bb=x.cursor()
# bb.execute('use test_1;')
#
#
# a=xlrd.open_workbook('test_1.xls')
# sheet=a.nsheets
# sheet=a.sheets()[0]
# # b=sheet.row_values(0)
# #
# # bb.execute('create table biao_3({} char(10),{} int,{} char(10));'.format(b[0],b[1],b[2]))
# b=sheet.nrows
#
# for i in range(1,b):
#     c=sheet.row_values(i)
#     bb.execute('insert into biao_3 values("{}","{}","{}");'.format(c[0],c[1],c[2]))
# bb.execute('select * from  biao_3;')
# cc=bb.fetchall()
# print(cc)

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


##################################################################

# # 创建一个传输通道  因为函数只能接收的是元组，所以使用双括号
# ssh123=paramiko.Transport(('192.168.0.193',22))
# ssh123.connect(username='root',password='123456')
# # 传输文件 使用sftp协议  创建一个sftp的实例 来实现上传下载
# sftp=paramiko.SFTPClient.from_transport(ssh123)
# # get是从linux上下载文件到本地 get('下载文件名','存放的文件名')
# sftp.get('/home/shell/1.out','1.txt')
# # 不论下载和上传都必须带文件名
# # put是从本地向linux上上传文件
# sftp.put('a.txt','/home/shell/a.txt')


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


# 数据库到表格
# a=pymysql.connect(host='192.168.0.193',port=3306,user='root',password='123456',charset='utf8')
# b=a.cursor()
# b.execute('use test_1;')
# b.execute('desc biao;')
# c=b.fetchall()
#
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet1')
#
# for i in range(3):
#     sheet.write(0,i,'{}'.format(c[i][0]))
#
# b.execute('select * from biao;')
# c=b.fetchall()
# d=len(c)
# for i in range(1,d):
#     sheet.write(i, 0, '{}'.format(c[i][0]))
#     sheet.write(i, 1, '{}'.format(c[i][1]))
#     sheet.write(i, 2, '{}'.format(c[i][2]))
#
# f.save('test.xls')


#数据库到txt
#
# a=pymysql.connect(host='192.168.0.193',port=3306,user='root',password='123456',charset='utf8')
# b=a.cursor()
# b.execute('use test_1;')
# b.execute('desc biao;')
# c=b.fetchall()
# with open('a.txt','w',encoding='utf-8') as f:
#     f.write('{},{},{}\n'.format(c[0][0],c[1][0],c[2][0]))
# b.execute('select * from biao;')
# c=b.fetchall()
# with open('a.txt','a',encoding='utf-8') as f:
#     for i in range(30):
#         f.write('{},{},{}\n'.format(c[i][0],c[i][1],c[i][2]))


# txt到数据库
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
# b.execute('drop table biao_3;')
# a.commit()

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

