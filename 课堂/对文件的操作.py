# /usr/bin/env python
# -*- coding:utf-8 -*-
#对文件的操作

#open函数

#路径要加双斜杠\\或者在路径前加r
f=open('C:\\Users\\meng\\Desktop\\a.txt','w',encoding='utf-8')  #打开a.txt空文件

# a='''sdafg
# sdfg
# dsfd
# asdf
# sadf'''    #在字符串头尾加上'''或者"""可以多行字符串

# f=open(r'C:\Users\meng\Desktop\a.txt','a',encoding='utf-8')
# f.write(a)   #也可以直接向文件中添加多行字符串
# print(f.read())  #read读取文件的所有内容，结果是字符串类型
# print(f.readlines()[1:4]) #结果是列表,可以是选择第几行和第几行

# print(f.readline())
# print(f.readline())  #每次只读取一行，有迭代功能
#
# f.write('qwertyuyiop\n')     #white本身不具备换行功能
# f.write('sdfghj'+'\n')
# f.close()   #在close上面都会执行


# a = open(r'C:\Users\meng\Desktop\a.txt', 'w', encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         a.write('{}*{}={}\t'.format(j,i,i*j))
#     a.write('\n')
# a.close()

#
# 写入图片
# f=open(r'C:\Users\meng\Desktop\zuoye.jpg','rb')
# dd=f.read()    #读取一张图片jpg，音频  权限用rb wb ab，注意格式
# f.close()
#
# w=open('zuoye.jpg','wb')
# w.write(dd)    #写入图片,权限rb rb ab，不加编码方式
# w.close()
#
#
# 上下文管理器
#
# with语句
# with open(r'C:\Users\meng\Desktop\a.txt','w',encoding='utf-8') as f:
#     for i in range(1,10):
#         for j in range(1,i+1):
#             f.write('{}*{}={}\t'.format(j,i,i*j))
#         f.write('\n')

# #统计一个文件中除单行注释的行和空行外的其他行
# with open(r'C:\Users\meng\Desktop\a.txt','r',encoding='utf-8') as f:
#     aa=f.readlines()
#     b=len(aa)
#     print(aa)   #把文件中的所有内容打印出来
#     print(b)    #文件所有的行
#     for i in aa:
#         if i[0]=='#':   #提取文件中‘#’开头的行
#             b-=1
#         elif i=='\n':   #提取文件中的空行
#             b-=1
#     print(b)

#把脚本导出成txt格式
# with open('10.13作业.py','r',encoding='utf-8') as a:
#     b=a.read()
# with open('a.txt','w',encoding='utf-8') as aa:
#     aa.write(b)
#     aa.close()

#创建是个文件，添加10行内容
# for i in range(10):
#     with open('{}.txt'.format(i),'w',encoding='utf-8') as a:
#         for j in range(10):
#             a.write(str(j)+'\n')



# 删除一个已经存在的文件多个文件
# import os
# for i in range(10):
#     os.remove('{}.txt'.format(i))

#查看当前文件的状态
# f=open('a.txt','wb')
# print(f.name,f.closed,f.mode)

#异常处理语句
# try:
#     a=123
#     print(a+1)
#     print('123')
# except Exception as a:   #和except一样，默认处理所有异常
#     print(a)
# else:                    #只要try语句中的代码没有异常，就执行else
#     print('没有异常')
# finally:
#     print('一定会执行')    #不管是否有异常一定会执行finally


# a=1234
# raise Exception('报错'):  #raise触发异常
# #错误开关，只要一碰到他就会报错
# print(a+1)


# import test

from test import *
ceshi()




# import random   #random是一个库，也相当于是一个模板


# from day1010 import *  #从文件中导入所有函数
# if __name__=='__main__':
#     print(aa())
#     print(jia())



# from day1010 import aa  #从文件中导入aa函数
#
# print(aa())
# print(jia())      #只能导入aa函数，其他函数不能用

