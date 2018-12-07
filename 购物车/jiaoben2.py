# /usr/bin/env python
# -*- coding:utf-8 -*-


#一个整数，加上100是一个完全平方数，在加上168还是一个完全平方数 -99.21.261.1581
# for i in range(1000):
#     for j in range(1000):
#         if i*i-j*j==168:
#             a=j*j-100
#             b=i*i-100-168
#             print(a)


#输入某月某日，判断这一天是这一年的第几天
# a=[31,28,31,30,31,30,31,31,30,31,30,31]
# c=input('请输入')
# b=c.split(',')
# d=0
# aa=int(b[0])
# bb=int(b[1])
# for i in range(0,aa-1):
#     d+=a[i]
# d+=bb
# print(d)




#输入三个整数，从小到大输出
def zheng(a):
    bb=len(a)
    for i in range(bb):
        b[i]=int(b[i])
#
# a=input('请输入三个数')
# b=a.split(',')
# zheng(b)
# b.sort()
# print(b)


#有一对兔子，从出生后的第三月起每个月都生一个兔子，假如兔子不死，问一年兔子的个数


#
# f1 = 1
# f2 = 1
# for i in range(1,22):
#     print('%12ld %12ld'%(f1,f2))
#     if (i % 3) == 0:
#         print('')
#     f1 = f1 + f2
#     f2 = f1 + f2

# #求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字
# a=int(input('请输入相加的值'))
# b=int(input('请输入次数'))
# c=a
# for i in range(1,b):
#     i=b*10**(i)
#     a+=i
#     c+=a
# print(c)


#      *
#      **
#     ***
#     ****
#    *****
#     ****
#     ***
#      **
#      *


# #菱形制作
# a=['*','**','***','****','*****','****','***','**','*']
# b=len(a)
# c=' '
# for i in a:
#     # aa=a.index(i)
#     for j in c:
#         print(i)

#1/2+2/3+3/5+5/8+8/13+......前20项的和
# a=2
# b=1
# c=0
# for i in range(20):
#     c+=a/b
#     b,a=a,a+b
# print(c)

# #1*2*3......前20的和
# a=0
# b=1
# for i in range(1,21):
#     b*=i
#     a+=b
# print(a)

#阶乘
# a=1
# for i in range(1,6):
#     a*=i
# print(a)


# #打印相反的字符串
# a=input('请输入字符')
# print(a[::-1])



#十进制转换成十六进制
# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
# b=int(input('请输入'))
# c=0
# d=''
# while True:
#     c=b%16
#     c=a[c]
#     b//=16
#     d+=c
#     if b==0:
#         break
# print(d[::-1])

# #一个数字的因数之和等于他本身
# for a in range(1,1000):
#     b=0
#     for i in range(1,a):
#         if a%i==0:
#             b+=i
#     if b==a:
#         print(a)

#不用int将字符串变整数

# a='12345'
# b=a[::-1]
# c=0
# for i,j in enumerate(b):
#     for h in range(10):
#         if str(h)==j:
#             c+=h*10**i
# print(c)


#最大的放在最后一位，最小的放在第一位
# a=[12,4,56,7,8,89,23]
# bb=a.index(max(a))
# cc=a.index(min(a))
# a[0],a[cc]=a[cc],a[0]
# a[-1],a[bb]=a[bb],a[-1]
# print(a)



#回文
#
# a=input('请输入')
# b=len(a)//2
# c=1
# for i in range(b-1):
#     if a[i]!=a[i-c]:
#         print('不是回文')
#         break
#     else:
#         print('是回文')


#有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# a=[1,3,5,7,9]
# b=input('插入一个数')
# c=len(a)
# for i in range(c):
#     b=int(b)
#     if b<=a[i]:
#         a.insert(i,b)
#         break
# if int(b)>=int(a[-1]):
#     a.append(b)
# print(a)


#
# b=0
# c=0
# a=int(input('请输入奇数'))
# for i in range(a):
#     b=9*10**i
#     c+=b
#     if  c%a==0:
#         print(c)
#         break
#倒序显示
# a=[1234,3245,4321,4532,213,2]
# a.sort(reverse=True)
# print(a)


#17
# a=[1,22,333,444,5555]
# b=int(input('请输入'))
# # c=len(a)
# for i in a:
#     c = a.index(i)
#     if b<=i:
#         a.insert(c,b)
#         break
# if b>a[-1]:
#     a.append(b)
# print(a)

#16
# a=[12,45,666,67,8,233]
# b=a.index(max(a))
# c=a.index(min(a))
# a[0],a[c]=a[c],a[0]
# a[-1],a[b]=a[b],a[-1]
# print(a)

#15

# for i in range(1,1000):
#     c=0
#     for j in range(1,i):
#         if i%j!=0:
#             continue
#         else:
#             c+=j
#     if c==i:
#         print(i)


#14
# aa=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
# a=int(input('请输入'))
# c=''
# while True:
#     b=a%16
#     a//=16
#     c+=aa[b]
#     if a==0:
#         print(c[::-1])
#         break
#
#13
#
# a=['ee','we','df',234]
# b=len(a)
# c=[]
# for i in range(1,b):
#     c.append(a[i])
# c.append(a[0])
#
# print(c)

#12
#
# a=input('请输入，以逗号分隔')
# b=a.split(',')
# for i in b:
#     for j in b:
#         for h in b:
#             if i!=j and j!=h and i!=h:
#                 print(i,j,h)
#             else:
#                 break


#11

# a='234567'
# b=a[::-1]
# bb=0
# for i,j in enumerate(b):
#     c=int(b[i])*10**i
#     bb+=c
# print(bb)

#10

# a=[123,345,6466,6466,234,213]
# a.sort()
# aa=len(a)
# b=max(a)
# c=a.count(b)
# for i in range(c):
#     print(b)
#     a.remove(b)
# bb=max(a)
# cc=a.count(bb)
# for j in range(cc):
#     print(bb)

#9
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if a**3+b**3+c**3==i:
#         print(i)

#8
# import random
#
# b = random.randrange(0, 10)
# for i in range(3):
#     a = int(input('请输入'))
#     if a==b:
#         print('聪明')
#         break
#     if a>b:
#         print('大了')
#     if a<b:
#         print('小了')

#7
# a=input('请输入')
# a=a.split(',')
# b=len(a)
# t=0
# for i in range(b):
#     for j in range(i+1,b):
#         if int(a[i])>int(a[j]):
#             t=a[i]
#             a[i]=a[j]
#             a[j]=t
# print(a)

#6
# a=input('请输入')
# b=len(a)
# c=1
# for i in range(b):
#     if a[i]==a[i-c]:
#         c+=2
#     else:
#         print('不是回文')
#         break
# else:
#     print('是回文')





# a=[123,345,65443,65443,2134,132]
# b=set(a.copy())
# c,d=max(b),min(b)
# f,g=a.count(c),a.count(d)
# print(c*f,d*g)


# #去重
# a=[123,45,532,32,32,21,45]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# c=len(b)
# t=0
# for j in range(c):
#     for h in range(j+1,c):
#         if b[j]>b[h]:
#             t=b[j]
#             b[j]=b[h]
#             b[h]=t
# print(b)


#10打印第一大数和第二大数
# a=[434,12,4,21,22,434]
# aa=a.copy()
# b=max(aa)
# c=aa.count(b)
# for i in range(c):
#     print(b)
#     aa.remove(b)
# bb=max(aa)
# cc=aa.count(bb)
# for j in range(cc):
#     print(bb)

#十进制转换十六进制
# aa=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
# a=int(input('qingshuru'))
# c=''
# while True:
#     b=a%16
#     a//=16
#     c+=aa[b]
#     if a==0:
#         print(c[::-1])
#         break



#11\15
#
# a='23445'
# # b=a[::-1]
# # c=0
# # for i,j in enumerate(b):
# #     cc=int(j)*10**i
# #     c+=cc
# # print(c)

# for i in range(1,1000):
#     c = 0
#     for j in range(1,i):
#         if i%j==0:
#             c+=j
#     if c==i:
#         print(i)


#16

# a=[12,23,2,23,2,12]
# b=max(a)
# c=min(a)
# bb=a.index(b)
# cc=a.index(c)
# a[-1],a[bb]=a[bb],a[-1]
# a[0],a[cc]=a[cc],a[0]
# print(a)

#17
# a=[1,3,4,6,8,90]
# b=int(input('请输入'))
# c=len(a)
# for i in range(c):
#     if b<=a[i]:
#         a.insert(i,b)
#         break
# if b>a[-1]:
#     a.append(b)
# print(a)


#13
# a=['qwe','ds','sad',23,'34']
# b=len(a)
# c=[]
# for i in range(1,b):
#     c.append(a[i])
# c.append(a[0])
# print(c)

#12

# a=input('请输入，以逗号分隔')
# b=a.split(',')
# c=set()
# for i in b:
#     for j in b:
#         for h in b:
#             if i!=j and j!=h and i!=h:
#                 c.add('{}{}{}'.format(i,j,h))
# print(c)

#3
# a=input('>>>>')
# b=a.split(',')
# aa=int(b[0])
# bb=int(b[1])
# cc=int(b[2])
# if aa+bb>cc:
#     if aa**2+bb**2==cc**2:
#         print('直角')
#     elif aa**2+bb**2>cc**2:
#         print('锐角')
#     elif aa**2+bb**2<cc**2:
#         print('钝角')
# else:
#     print('不是')

#
# import random
#
# a=random.randrange(1,10)
#
# for i in range(3):
#     b = int(input('>>>'))
#     if b==a:
#         print('聪明')
#         break
#     elif b>a:
#         print('大了')
#     elif b<a:
#         print('小了')
# else:
#     print('你真是太笨了')


# #13
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if a**3+b**3+c**3==i:
#         print(i)

#20

# a=input('>>>')
# b=len(a)//2
# for i in range(b):
#     if a[i]!=a[-i-1]:
#         print('bushi')
#         break
# else:
#     print('shi')

# def maopao(a):
# #     b=len(a)
# #     t=0
# #     for i in range(b):
# #         for j in range(b-1):
# #             if a[j]>a[j+1]:
# #                 t=a[j]
# #                 a[j]=a[j+1]
# #                 a[j+1]=t
# #     print(a)
# #
# # maopao([12,34,23,2])

# a=[i for i in range(b) for j in range(b-1) if a[j]>a[j+1] a[j],a[j+1]=a[j+1],a[j]]
#



# #菱形制作
# for i in range(3):
#     print(' '*i,end=' ')
#     print('* '*(3-i))
#
# a=5
# for i in range(a):
# 	print(' '*i,'* '*a)
# 	a-=1


