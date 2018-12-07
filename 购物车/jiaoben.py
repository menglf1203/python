# /usr/bin/env python
# -*- coding:utf-8 -*-

#选择排序法
# a=input('请输入')
# b=a.split(',')
# c=len(b)
# t=0
# for i in range(0,c):
#     for j in range(i+1,c):
#         if b[i]>b[j]:
#             t=b[i]
#             b[i]=b[j]
#             b[j]=t
#         else:
#             continue
# print(b)

#冒泡排序法
# a=input('请输入')
# b=a.split(',')
# c=len(b)
# t=0
# for i in range(0,c):
#     for j in range(0,c-1):
#         if b[j]>b[j+1]:
#             t=b[j]
#             b[j]=b[j+1]
#             b[j+1]=t
#         else:
#             continue
# print(b)


# # 水仙花数
# for i in range(100,1000):
#     if (i//100)**3+(i//10%10)**3+(i%10)**3==i:
#         print(i)




# a=input('请输入')
# b=a.split(',')
# b.sort()
# # c=len(b)
# print(b[-1])
# print(b[-2])


# #去重并排序
# t=input('请输入')
# a=t.split(',')
# c=[]
# for i in a:
#     if i not in c:
#         c.append(i)
# c.sort()
# print(c)

# a=int(input('请输入'))
# b=0
# c=1
# for i in range(1,a+1):
#     c*=i
#     b+=c
# print(b)


#质数之和
# a=0
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         a+=i
# print(a)



# import random

# a=random.randrange(1,10)
# for i in range(3):
#     b=int(input('请输入'))
#     if b==a:
#         print('congming')
#         break
#     elif b>a:
#         print('dale,你还有{}次'.format(2-i))
#     elif b<a:
#         print('xaiole,你还有{}次'.format(2-i))
# else:
#     print('bendan')


# a=input('请输入')
# b=a.split(',')
# b.sort()
# aa=int(b[0])
# bb=int(b[1])
# cc=int(b[2])
# if aa+bb>cc:
#     if aa**2+bb**2==cc**2:
#         print('zhijiao')
#     elif aa**2+bb**2>cc**2:
#         print('ruijiao')
#     elif aa**2+bb**2<cc**2:
#         pring('dunjiao')
# else:
#     print('bushi')



# a=[1,1,1,1,1,2,43,5,65,6,7,7,87]
# for i in a:
#     if a.count(i)>0:
#         for j in range(a.count(i)-1):
#             a.remove(i)
# a.sort()
# print(a)








#while循环   1-100的和
# a=1
# c=0
# while a<101:
#     c+=a
#     a+=1
# print(c)

# #无限循环猜数字游戏
# import random
#
# a=random.randrange(1,10)
#
# while True:
#     b = int(input('请输入数字'))
#     if b==a:
#         print('congming')
#         break
#     elif b>a:
#         print('dale')
#     elif b<a:
#         print('xiaole')




# #九九乘法表while
# a=1
# while a<10:
#     b=1
#     while b<=a:
#         print('{}*{}={}'.format(b,a,b*a),end=' ')
#         b+=1
#     a+=1
#     print('')


#
# a=input('请输入四个数字')
# b=set()
# for i in a:
#     for j in a:
#         for q in a:
#             b.add('{}{}{}'.format(i,j,q))
# print(b)

#将列表中的元素向左挪一位
# a=['45','123','asd']
# b=len(a)
# t=0
# for i in range(0,b-1):
#     t=a[i]
#     a[i]=a[i+1]
#     a[i+1]=t
# print(a)



# #sum第三个python内置函数
# a=[1,45,76,98]   #元素只能是数字（整数或者浮点数）
#                  # 可以是元组和列表中的
# print(sum(a))
# print(sum(a)/4)
# print(max(a))
# print(min(a))




# while True:
#     a=input('手动输入一组数')
#     if a=='exit':
#         break
#     else:
#         b=len(a)
#         c=0
#         d=0
#         for i in range(0,b):
#             d=int(a[i])
#             c+=d
#             e=c/b
#         print(e)
#         for i in range(0,b):
#             d=int(a[i])
#             if d<e:
#                 print(d)
# #


# b=['324','98','876','56']
# for i,j in enumerate(b):
#     b[i]=int(j)
# print(b)

# for i in b:
#     aa=int(i)
#     print(aa)






# while True:
#     a=input('>>>>>')
#     if a=='exit':
#         break
#     else:
#         b=a.split(',')
#         sum=0
#         for i in b:
#             sum+=int(i)
#         print(sum/len(b))
#         for j in b:
#             if int(j)<sum/len(b):
#                 print(j)




#十六进制转换十进制
#
# a=input('请输入')
# b=len(a)
# c=','.join(a)
# d=c.split(',')
# d.reverse()
# n=0
# for i in range(0,b):
#     e=int(d[i])
#     j=e*(16**i)
#     n+=j
# print(n)

# b=['324','98','876','56']
# for i,j in enumerate(b):
#     b[i]=int(j)
# print(b)





#一个有顺序的列表，随机加入一个数，加入的数在正确位置
# a=[123,234,235,434,56]
# t=len(a)
# a.sort()
# b=int(input('请输入一个数'))
# for i in range(0,t):
#     if b<=int(a[i]):
#         a.insert(i,b)
#         break
# if b>int(a[-1]):
#     a.append(b)
# print(a)

# #一个有顺序的列表，随机加入一个数，加入的数在正确位置元帅写的
# a=int(input('请输入一个数'))
# b=[2,3,4,8]
# for i in b:
#     if a>i:
#         b.append(a)
#         b.sort()
#         break
# print(b)


#十进制转十六进制
# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b=int(input('请输入'))
# f=''
# while True:
#     c=b%16
#     b=b//16
#     f+=a[c]
#     if b==0:
#         break
# print(f[::-1])






#判断字符串是否回文
# a=input('请输入')
# b=len(a)
# c=b//2
# d=1
# for i in range(0,c):
#     e=i-d
#     d+=2
#     if a[i]!=a[e]:
#         print('不是回文')
#         break
# else:
#     print('是回文')

#老师讲的判断是否回文字符串
# a='abcba'
# b=len(a)//2
# for i in range(b):
#     if a[i]!=a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')







#一个数的因数之和等于它本身
# for i in range(1,1000):
#     i=int(i)
#     j=0
#     a = []
#     for j in range(1,i+1):
#         j=int(j)
#         for q in range(j+1,i+1):
#             q=int(q)
#             if j*q==i:
#                 a.append(j)
#                 a.append(q)
#     if sum(a)-i==i:
#         print(i)
# #一个数的因数之和等于它本身
# for a in range(1,1000):
#     a=int(a)
#     sum=0
#     for b in range(1,a+1):
#         if a%b==0 and a != b:
#             sum=sum+b
#     if sum==a:
#         print(a)

# #把列表中最大的放在最后一位，最小的放在第一位
# t=0
# a=[7,9,5,2,4]
# aa=a.copy()
# for i in a:
#     if i==min(a):
#         aa[0]=i
#         t=a.index(i)
#         aa[t]=a[0]
#     elif i==max(a):
#         aa[-1]=i
#         t=a.index(i)
#         aa[t]=a[-1]
# print(aa)


# #把列表中最大的放在最后一位，最小的放在第一位
# a=[23,56,987,234]
# b=a.index(max(a))
# c=a.index(min(a))
# a[c],a[0]=a[0],a[c]
# a[b],a[-1]=a[-1],a[b]
# print(a)


# #不用int将字符串变成整数
# a='32487654545'
# b=a[::-1]               #先把字符串反转
# s=0
# for i,j in enumerate(b):
#     for h in range(10):
#         if str(h)==j:
#             s+=h*10**i
# print(s)
# #6*10**0=6   倒数第一位
# #5*10**1=50   倒数第二
# #4*10**2=400    倒数第三


# #选择法
# a=input('请输入一组数')
# b=a.split(',')
# c=len(b)
# for i in range(c):
#     for j in range(i+1,c):
#         if int(b[i])>int(b[j]):
#             t=b[i]
#             b[i]=b[j]
#             b[j]=t
# print(b)


