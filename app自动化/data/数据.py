# /usr/bin/env python
# -*- coding:utf-8 -*-

from time import sleep
import xlrd


class shuju():
    def shu(self):
        s=[]
        f=xlrd.open_workbook(r'C:\Users\meng\Desktop\python\app自动化\data\app1.xlsx')
        sheet=f.sheets()[0]
        hang=sheet.nrows
        for i in range(1,hang):
            s.append(sheet.row_values(i))
        return s
    def shu1(self):
        s = []
        f = xlrd.open_workbook(r'C:\Users\meng\Desktop\python\app自动化\data\app1.xlsx')
        sheet = f.sheets()[0]
        hang = sheet.nrows
        for i in range(1, hang):
            s.append(sheet.row_values(i))
        return s




