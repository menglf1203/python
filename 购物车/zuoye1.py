# /usr/bin/env python
# -*- coding:utf-8 -*-

def shlb():
    global a,b,c,qq
    qq=0
    aq=input('请输入金额：')
    a=int(aq)
    b=[1999,10,20,998]
    c=['电脑','鼠标','游艇','美女']
    for i in range(4):
        ai={}
        ai['name']=c[i]
        ai['price']=b[i]
        print(1+i,ai)
##############################################################################
def gouwuche():
    global qq,ac,a
    while True:
        ac=input('请输入购买(删除购物车)的商品1,*,1（1,*,-1）/退出请输入“end”')
        aa=ac.split(',')
        if ac=='end':
            break
        elif int(aa[0])>0 and int(aa[2])!=0:
            aa1=int(aa[0])
            bb1=int(aa[2])
            q=b[aa1-1]*bb1
            qq+=q
            print('成功购买：    {}*{}'.format(c[aa1-1],bb1))
            print('累计消费{}元,卡内金额{}元'.format(qq,a))
        else:
            print('格式错误，请重新输入。')
##############################################################################
def goumai():
    global a
    while True:
        print('卡内余额：{}'.format(a-qq))
        print('共计消费：%d'%(qq))
        if ac =='end':
            if a>qq:
                print('欢迎下次光临！')
                break
            elif a<qq:
                ye=input('余额不足，请充值；整理购物车‘gwc’；退出‘end’。')
                if ye== 'end':
                    print('欢迎下次光临！')
                    break
                elif ye=='gwc':
                    gouwuche()
                else:
                    a+= int(ye)

shlb()
gouwuche()
goumai()
