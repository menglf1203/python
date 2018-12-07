# /usr/bin/env python
# -*- coding:utf-8 -*-


# import os   #导入os
# #os模块
#
# a=os.popen('ping 192.168.0.1')   #执行windows命令os.popen
# a=os.popen('nslookup www.baidu.com')
# print(a.read())
#
#
# 获取当前所在的位置
# print(os.getcwd())    # 获取当前文件的所在位置
#
# 切换目录
# os.chdir(r'C:\Users\meng\Desktop')   # 两个斜杠或者前面加r是为了让转义字符不转义
# print(os.getcwd())
#
# 创建目录
#
# os.mkdir(r'C:\Users\meng\Desktop\aaa')  # 如果不加路径，就在当前目录下创建
# os.makedirs(r'C:\Users\meng\Desktop\aaa\bbb')  # 创建递归目录
#
# 删除递归目录
# os.removedirs(r'C:\Users\meng\Desktop\aaa\bbb')
# 删除空目录
# os.rmdir(r'C:\Users\meng\Desktop\aaa')
# 删除文件
# os.remove(r'C:\Users\meng\Desktop\123.txt')
#
# 获取当前目录下的所有文件
# print(os.listdir(r'C:\Users\meng\Desktop\python'))
# 更改文件名
# os.rename('day10.6.py','day1006.py')  #旧文件名，新文件名
# 将文件名与路径分隔开(分隔的是字符串，有无此文件和路径都不管照常显示)
# print(os.path.split(r'C:\Users\meng\Desktop\python'))
# 将文件的后缀名与路径分隔开
# print(os.path.splitext(r'C:\Users\meng\Desktop\python\day1014.py'))
#
# 打印一个目录下.py的文件
# for i in os.listdir():
#     if os.path.splitext(i)[-1]=='.py':
#         print(os.path.splitext(i))
#
# # 判断是否为普通文件
# print(os.path.isfile('_pycache_'))   # 是_pycache_一个目录
# # 判断是否为目录文件
# print(os.path.isdir('123'))          # .idea是一个目录
# # 判断是否为链接文件
# print(os.path.islink('day.py'))
#
#
# # 统计一个路径下有多少文件和目录
# os.chdir(r'D:\123')
# a=0
# b=0
# for i in os.listdir():   # 不能直接在listdir中切换路径
#     if os.path.isfile(i):
#         a+=1
#     elif os.path.isdir(i):
#         b+=1
# print('文件:%d,目录:%d'%(a,b))
# # # 或者用列表推导式
# # a=[i for i in os.listdir() if os.path.isfile(i) ]
# # b=[y for y in os.listdir() if os.path.isdir(y)]
# #
# # print(len(a),len(b))
#
# # 判断目录下有多少个py文件
# a=0
# for i in os.listdir():
#     c=os.path.splitext(i)
#     if c[-1]=='.py':
#         a+=1
# print(a)

# 需要下载的模块
# xlwt        作用：给excel表格写入数据
# xlrd       作用：读取Excel表格中的数据
# xlutils    作用：给excel表格中追加数据

import xlwt     #写入
import xlrd     #读取
import xlutils  #追加
#
# # 打开一个文件
# f=xlwt.Workbook(encoding='utf-8')
# # 添加一个标签页，括号中写标签页的名称
# sheet=f.add_sheet('python操作excel表格')
# # 写入数据
# # 第一个数字代表行(从0开始)
# # 第二个数字代表列(从0开始)
# # 第三个字符串代表写入的内容
# sheet.write(0,1,'数据')
# # 保存文件
# f.save('text.xls')



