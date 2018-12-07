# /usr/bin/env python
# -*- conding:utf-8 -*-

k=int(input('请输入总资产'))
a={}
aa=[]
name=['电脑','鼠标','游艇','菜刀']
price=[1999,10,20,998]
num=len(name)
def all(x=4):
    for i in range(0,x):
        a['name']=name[i]
        a['price']=price[i]
        print(i,a)
def gouwuche():
    print(aa)
all()
while True:
    kk=int(input('选择0-3正确的商品编号添加购物车'))
    if kk not in aa:
        for j in range(0,num):
            aa.append(kk)
            aa.append(name[kk])
            aa.append(price[kk])
            break
        print(aa)
        kkk=input('是否购买')
        if kkk=='是':
            if price[kk]<=k:
                k -= price[kk]
                print('{}购买成功,当前余额{}元'.format(name[kk],k))
                aa.remove(kk)
                aa.remove(name[kk])
                aa.remove(price[kk])
                continue
            else:
                print('余额不够')
                kkkk=input('是否充值')
                if kkkk=='是':
                    jine=input('请输入金额，最低10元')
                    if int(jine)>=10:
                        k+=int(jine)
                        print('充值成功，当前余额{}元'.format(k))
                        kkk = input('是否购买')
                        if kkk == '是':
                            if price[kk] <= k:
                                k -= price[kk]
                                print('{}购买成功,当前余额{}元'.format(name[kk], k))
                                aa.remove(kk)
                                aa.remove(name[kk])
                                aa.remove(price[kk])
                                continue
                            else:
                                print('购买失败')
                    else:
                        print('充值失败')
                        all()
                else:
                    print('充值失败，当前余额{}元'.format(k))
        else:
            all()
            kk
    else:
        wen=input('已加入购物车是否删除')
        if wen=='是':
            gouwuche()
            kkkkk=int(input('删除商品，请输入商品编号'))
            if kkkkk in aa:
                aa.remove(kkkkk)
                aa.remove(name[kkkkk])
                aa.remove(price[kkkkk])
                print('已删除')
                continue
        else:
            continue









