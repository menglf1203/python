# /usr/bin/env pythen
# -*- coding:utf-8 -*-

#运算符
# a='ds'*4
# print(a)
# b='asdf'+'asd'
# print(b)
# c=324/23
# print(c)

# a=(2132,213,2.1)
# print(213 in a)       #判断213是a中的成员是否正确
# print(213 not in a)   #判断213不是a中的成员是否正确
# b='sadfss'
# c='zdsfs'
# print(b>c)


# a=3+4
# a+=5   #也可以写a=a+5
# print(a)

#基础语句（判断语句、循环语句、异常处理语句、上下文管理语句）
#判断语句

# a=input('请输入成绩：')
# a=int(a)
# if a>=90:
#     print('优秀')
# elif a>=80:
#     print('良好')
# elif a>=60:
#     print('及格')
# else:
#     print('不及格')


# #嵌套判断
# a=6
# if a%2==0:
#     if a%3==0:
#         print('这个数字既能整除2又能整除3')
#     else:
#         print('这个数字能整除2，不能整除3')
# else:
#     print('这个数字不能整除2')



# #手动输入一串字符串进行嵌套判断
# a=input('请输入')
# if a.startswith('a'):
#     if a.endswith('c'):
#         print('hello,world')
#     else:
#         print('hello')
# elif a.endswith('c'):
#     print('word')
# else:
# # elif (not a.endswith('c')) and (not a.startswith('a')):
#     print('123')



# a=input('输入3个数')
# a=list(a)
# a.sort()
# b=a[0]
# b=int(b)
# c=a[1]
# c=int(c)
# d=a[2]
# d=int(c)


# a=[2,8,9]
# a.sort()

# b=input('请输入')
# a=b.split(',')
# a.sort()
# aa=int(a[0])
# bb=int(a[1])
# cc=int(a[2])
# if aa+bb>cc:
#     if aa**2+bb**2==cc**2:
#        print('是直角三角形')
#     elif aa**2+bb**2>cc**2:
#         print('是锐角三角形')
#     elif aa**2+bb**2<cc**2:
#         print('是钝角三角形')
# else:
#     print('不是三角形')


# c=input('请输入<10的数')
# a=list(c)
# a.sort()
# d=int(a[0])
# e=int(a[1])
# f=int(a[2])
# if (d+e)>f:
#     if (d**2+e**2)==(f**2):
#         print('直角')
#     elif (d**2+e**2)>(f**2):
#         print('锐角')
#     elif (d**2+e**2)<(f**2):
#         print('钝角')
# else:
#     print('不是三角形')


#九九乘法表
# for a in range(1,9):
#     for b in range(1,a):
#         print('{}x{}={}'.format(b,a,a*b),end=' ')
#     print()

# for a in range(1,10):
#     for b in range(1,a+1):
#         print('%d*%d=%2d' % (b,a,a*b),end=' ')
#     print()


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()



#水仙花数
# for a in range(100,999):
#     # b=a/100
#     # print(type(b))   #可查b是浮点数
#     if a==((a//100)**3+(a//10%10)**3+(a%10)**3):
#     # if a==(int(a/100)**3+int(a/10%10)**3+int(a%10)**3):
#     #需要将浮点数变成整数或者整除
#         print(a)

#阶乘
# n=input('请输入一个数')
# t=int(n)
# for a in range(1,t+1):
#     d=0
#     c=1
#     for b in range(1,a+1):
#         c*=b
#         d+=c
# print(d)

#选择排序法
# a=input('请输入一组数')
# b=list(a)
# c=b.index(b[-1])
# for i in range(0,c):
#     for j in range(i+1,c+1):
#         if b[i]>b[j]:
#             d=b[i]
#             b[i]=b[j]
#             b[j]=d
# print(b)

#100内的偶数之和
# b=0
# for a in range(1,101):
#     if a%2 == 0:
#         b+=a
# print(b)

#质数之和
# nun=0
# for a in range(3,100):
#     for b in range(2,a+1):
#         if a%b==0:
#             if a==b:
#                 nun+=a
# print(nun)




