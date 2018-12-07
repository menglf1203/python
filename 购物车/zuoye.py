# /usr/bin/env python
# -*- coding:utf-8 -*-

class Shangpin():
    def zongshangpin(self,aa=4):
        global name
        global price
        name = ['电脑', '鼠标', '游艇', '美女']
        price = [1999, 10, 200, 998]
        sp=[]
        for i in range(aa):
            sp.append('%d name:%s,price:%d'%(i,name[i],price[i]))
        print(sp)
    def zzc(self):
        global c
        c=0
        zzc = int(input('请输入总资产'))
        c+=zzc
        return c
    def tj(self):
        return che

class Gouwuche(Shangpin):

    def jia(self):
        self.tj()
        tj = input('输入商品编号添加到购物车(end结账)')
        if tj=='end':
            print(che)
            xz=input('结账(1) or 删除商品(2)')
            if xz=='1':
                self.jz(c)
            elif xz=='2':
                self.jian()
        else:
            che.append('%d name:%s,price:%d'%(int(tj),name[int(tj)],price[int(tj)]))
            print('{}已加入购物车'.format(name[int(tj)]))

    def jian(self):
        tj=int(input('输入商品编号从购物车删除(end结账)'))
        if tj=='end':
            print(che)
            self.jz(c)
        else:
            che.remove('%d name:%s,price:%d' % (tj, name[tj], price[tj]))
            print('{}已删除'.format(name[tj]))

    def jz(self,c):
        a = 0
        for i in che:
            a+=int(i.split(':')[-1])
        if a>c:
            je=int(input('余额不足，请输入充值金额'))
            if je>=0:
                c+=je
                if a>c:
                    print('余额不足，购买失败')
                else:
                    c -= a
                    print('购买成功！余额{}元'.format(c))
                    exit()
            else:
                print('输入金额错误，购买失败')
        else:
            print('购买成功！余额{}元'.format(c-a))
            exit()

shangpin=Shangpin()
gouwuche=Gouwuche()

shangpin.zzc()
shangpin.zongshangpin()
che=list()
while True:
    gouwuche.jia()



