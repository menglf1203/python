# /usr/bin/env python
# -*- coding:utf-8 -*-

#函数
# def jiujiu():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(j,i,i*j),end=' ')
#         print()
# jiujiu()#或者用以下方法调用
# a=jiujiu
# a()


#函数的传参

#
# def jiujiu(*x,y=5):
#     for i in range(x[0],y+1):
#         for j in range(x[0],i+1):
#             print('{}*{}={}'.format(j,i,i*j),end=' ')
#         print()
# jiujiu(3)

# def aaa(*a):
#     print(a)
# aaa(1,2,3,4,5,['jhgfds',98765])

#
# def aaa(**kwargs):
#     print(kwargs)
# aaa(name='电脑',price=19999)
# aaa(name='鼠标',price=10)
# aaa(name='游艇',price=20)
# aaa(name='美女',price=998)

def maopao(a):
    b=len(a)
    t=0
    for i in range(b):
        for j in range(0,b-1):
            if int(a[j])>int(a[j+1]):
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
    print(a)

# maopao([1,32,2,4,5,67,8,])

def xuanze(a):
    b=len(a)
    t=0
    for i in range(b):
        for j in range(i+1,b):
            if int(a[i])>int(a[j]):
                t=a[i]
                a[i]=a[j]
                a[j]=t
    print(a)

# xuanze([23,234,5,76,7])

def jiujiu(*x,y=5):
    for i in range(x[0],y+1):
        for j in range(x[0],i+1):
            print('{}*{}={}'.format(j,i,i*j),end=' ')
        print()

# jiujiu(3)

def zhishu(a):
    int(a[0])
    int(a[1])
    for i in range(a[0],a[1]):
        for j in range(a[0],i+1):
            if i%j==0:
                if i==j:
                    print(i)
                else:
                    break


# zhishu([2,100])


def jiecheng(a):
    b=1
    c=0
    for i in range(1,a+1):
        b*=i
        c+=b
    print(c)

# jiecheng(4)

def huiwen(a):
    b=len(a)
    d=1
    for i in range(0,b):
        if a[i]==a[i-d]:
            d+=2
            print('huiwen')
        else:
            print('bushihuiwen')


# huiwen(asdfg)

def caishuzi():
    import random
    a = random.randrange(1, 10)
    for i in range(0,3):
        b=int(input('请输入数字'))
        if b==a:
            print('厉害')
            break
        elif b>a:
            print('大了')
            continue
        elif b<a:
            print('小了')
            continue

# caishuzi()

def shuixianhua(x=100,y=1000):
    for i in range(x,y):
        a=i//100
        b=i//10%10
        c=i%10
        if a**3+b**3+c**3==i:
            print(i)


# shuixianhua()


def sanjiaoxing(aa):
    a=aa.split(',')
    a.sort()
    b=int(a[0])
    c=int(a[1])
    d=int(a[2])
    if b+c>d:
        if b**2+c**2==d**2:
            print('是直角')
        elif b**2+c**2>d**2:
            print('是锐角')
        else:
            print('是钝角')
    else:
        print('不是三角形')

# sanjiaoxing(2,3,4)



def quchong(a):
    for i in a:
       b = a.count(i)
       for j in range(b-1):
           a.remove(i)
    a.sort()
    print(a)


# quchong([234,4567,22,32,22,343,12])