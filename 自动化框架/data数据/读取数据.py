# /usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd

class Duqu():
    def duqu(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\meng\Desktop\python\自动化框架\data数据\好分数.xls')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(1,num):
            sj=sheet.row_values(i)
            shuju.append(sj)
        return shuju

    def 服务器(self):
        shuju = []
        f = xlrd.open_workbook(r'C:\Users\meng\Desktop\python\自动化框架\data数据\服务器.xlsx')
        sheet = f.sheets()[0]
        hang = sheet.nrows
        for i in range(1, hang):
            shuju.append(sheet.row_values(i))
        return shuju

    def appwenjian(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\meng\Desktop\python\自动化框架\data数据\app.xlsx')
        sheet=f.sheets()[0]
        hang=sheet.nrows
        for i in range(1,hang):
            shuju.append(sheet.row_values(i))
        print(shuju)
        return shuju

    def haofenshu1(self):
        shuju = []
        f = xlrd.open_workbook(r'C:\Users\meng\Desktop\python\自动化框架\data数据\好分数1.xlsx')
        sheet = f.sheets()[0]
        hang = sheet.nrows
        for i in range(1, hang):
            shuju.append(sheet.row_values(i))
        return shuju


