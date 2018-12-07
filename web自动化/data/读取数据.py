# /usr/bin/env python
# -*- coding:utf-8 -*-

import xlrd

class Dq():
    def denglu1(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\meng\Desktop\python\web自动化\data\登录.xlsx')
        sheet=f.sheets()[0]
        hang=sheet.nrows
        for i in range(1,hang):
            a=sheet.row_values(i)
            if type(a[0])==float:
                a[0]=int(a[0])
                shuju.append(a)
            elif type(a[1])==float:
                a[1] = int(a[1])
                shuju.append(a)
            else:
                shuju.append(a)

        return shuju

    def denglu2(self):
        pass

    def QQdenglu(self):
        shuju=[]
        f = xlrd.open_workbook(r'C:\Users\meng\Desktop\考试.xlsx')
        sheet = f.sheets()[0]
        hang = sheet.nrows
        for i in range(1, hang):
            a = sheet.row_values(i)
            if type(a[0]) == float:
                a[0] = int(a[0])
                shuju.append(a)
            elif type(a[1]) == float:
                a[1] = int(a[1])
                shuju.append(a)
            else:
                shuju.append(a)
        return shuju



