# /usr/bin/env python
# -*- coding:utf-8 -*-

#字典也可以循环语句
# a={'name':'小米','age':333,'qew':123}
# for i,j in a.items():
#     print(i,j)



# #100内的和
# nun=0
# for a in range(1,101):
#     nun+=a
# print(nun)
#
# #也可以这样写100内的和
# print(sum(range(101)))


# #100内奇数的和
# nun=0
# for a in range(1,101,2):
#     nun+=a
# print(nun)
# #100内奇数的和
# print(sum(range(1,101,2)))
#
# #100内偶数的和
# nun=0
# for a in range(0,101,2):
#     nun+=a
# print(nun)
# #100内偶数的和
# print(sum(range(0,101,2)))

# #打印3次hello也可以用循环语句实现
# a=0
# for i in range(1,4):   #仅代表循环多少次
#     print('hello')



# #1-2+3-4+5-6……+99 奇数的和 减 偶数的和
# a=sum(range(1,100,2))
# b=sum(range(2,100,2))
# print(a-b)
# #或者
# print((sum(range(1,100,2)))-(sum(range(2,100,2))))


# #1-2+3-4+5-6……+99
# nun=0
# num=0
# for a in range(1,100,2):
#     nun+=a
# for b in range(2,100,2):
#     num+=b
# print(nun-num)


#1-2+3-4+5-6……+99
# b=0
# for i in range(1,100):
#     if i%2==0:
#         b-=i
#     else:
#         b+=i
# print(b)

#enumerate函数：将下标位置和元素对应

# a='kjhgtfre'
# for i in enumerate(a):
#     print(i)


#输入想要找的商品编号，可以打印出来，从数字1开始
# a=['电脑','手表','保温杯']
# for i,j in enumerate(a):
#     print(i+1,j)
# b=int(input('请输入数字'))
# print(a[b-1])


#循环嵌套
#
# for a in range(10):
#     if a>5:
#         print(a)
#

#

#
# a=random.randrange(1,10)   #从1-10之间随机产生的，取不到10
# a=random.randint(1,10)   #从1-10之间随机产生的，可以取到10
# print(a)
#猜数字游戏
# import random   #必须要有的
# a=random.randrange(1,10)
# for i in range(3):
#     i=int(i)
#     b = int(input('请输入一个数'))
#     if b==a:
#         print('猜对了')
#         break
#     elif b>a:
#         print('大了你还有%d次'%(2-i))
#         continue
#     elif b<a:
#         print('小了你还有%d次'%(2-i))
#         continue
# else:
#     print('笨蛋')



#循环嵌套循环
# for i in range(3):
#     for j in range(2):
#         print(123)



#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%dX%d=%d'%(j,i,i*j),end='\t')
#     print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,i*j),end='\t')
#     print()

#break
# for i in range(10):
#     if i==5:
#         break
#     else:
#         print(i)


# #质数之和
# nun=0
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i%j==0:
#             if i==j:
#                 nun+=i
#             else:
#                 break
# print(nun)



# #判断所有人的名字的个数=2，终止循环；不是则显示完美
# a=['小明啊','小花','小刘啊']
# for i in a:
#     if len(i)==2:
#         break
# else:
#     print('完美')
# #不用for..else..实现
# a=['小明啊','小花啊','小刘啊']
# c=0
# for i in a:
#     if len(i)==2:
#         c=c+1
#         break
# if c==0:
#     print('完美')




#阶乘
# d=0
# a=int(input('请输入一个数'))
# for i in range(1,a+1):
#     c=1
#     for j in range(1,i+1):
#         c*=j
#     d+=c
# print(d)

#阶乘
# n=int(input('请输入一个数'))
# c=1
# d=0
# for b in range(1,n+1):
#     c*=b
#     d+=c
# print(d)


# a=[123,456,43,123]
# a=set(a)
# a=list(a)
# a.sort()
# print(a)










