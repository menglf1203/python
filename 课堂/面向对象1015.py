# /usr/bin/env python
# -*- coding:utf-8 -*-
#
#
# import test
# test.caishuzi()
#
#
# from test import *
# caishuzi()
#
# import time
# print(time.ctime())
#
#
# a='iuytrew'
# try:
#     a=int(a)
# except Exception as x:
#     print(x)
# else:
#     print('meicuo')
#
#
# 面向对象
# 定义一个类
# 类：属性、方法
# class Shuzi():   #类名首字母一般为大写
#     def jiecheng(self):    # self也是类的实例化,方便在类的内部调用
#         print(self.__class__)
#
#     def jiujiu(self):   #函数名后的括号里必须写上self
#         for i in range(1,10):
#             for j in range(1,i+1):
#                 print('{}*{}={}\t'.format(j,i,i*j),end='')
#             print()
#
#     def zhishu(self):
#         self.aaa()
#
#     def __aaa(self):
#         import random
#         a=random.randrange(1,10)
#         return a
#
#
#
# Shuzi().jiujiu()
# Shuzi().zhishu()
# # #对象是类的实例化
# a=Shuzi()   # 类的外部实例化
# a.zhishu()
#
#
# 继承
#
# class Test_1():  # 父继承
#     def aaa(self):    #私有方法
#         return 123
#
# class Test_2(Shuzi,Test_1):  # 嵌套继承
#     # def aaa(self):         # 多态，会优先选择自己的
#     #     a=0
#     #     for i in range(1,101):
#     #         a+=i
#     #     return a
#     pass
#
# test_2=Test_2()   # 给类赋值，方便调用
# print(test_2.aaa())
#
#
# class Stu():
#     a='小明'    # 两个基本属性
#     b=2
#     def __init__(self,a,b):   # 初始化属性
#         self.name=a           # 对象传参
#         self.age=b
#
#     def test_1(self):
#         print('我叫%s，今年%d年级'%(self.name,self.age))
#
#     def test_2(self,c=10):     # C是参数传参
#         print('我叫%s，今年%d岁'%(self.name,c))
#
# aa=Stu('小明',6)   # 可以直接给类中所有方法赋值
# aa.test_1()
# aa.test_2()     # test_2函数中有必须参数


class Test_1():

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def zhishu(self):
        s = 0
        for i in range(self.a,self.b):
            for j in range(self.a,i):
                if i%j==0:
                    break
            else:
                s+=i
        print(s)

    def huiwen(self,aa):
        b=len(aa)//2
        for i in range(b+1):
            if aa[i]!=aa[-i-1]:
                print('no')
                break
        else:
            print('yes')



test_1=Test_1(2,10)
test_1.zhishu()
test_1.huiwen('abcba')
