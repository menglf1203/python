# /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import requests
import HTMLTestRunne
import HTMLTestRunnertest
import xlrd

class Ziji(unittest.TestCase):
    def shu(self):
        shuju=[]
        f=xlrd.open_workbook('服务器.xlsx')
        sheet=f.sheets()[0]
        hang=sheet.nrows
        for i in range(1,hang):
            shuju.append(sheet.row_values(i))
        return shuju

    def toubu(self,a,b):
        headers={'Content-Type': "application/json",
                 'cache-control': "no-cache",
                 'Postman-Token': "e946812b-4052-4bb1-a831-6dd51b43ad07"}
        url='http://192.168.0.15:5000/login'
        payload ={'username':'{}'.format(a),'password':'{}'.format(b)}
        res = requests.post(url=url, data=payload, headers=headers)
        html = res.content.decode()
        return html

    def test_1(self):
        shuju=self.shu()
        html=self.toubu(shuju[0][0],int(shuju[0][1]))
        self.assertIn('welcome, zhangsan !',html)

    def test_2(self):
        shuju=self.shu()
        html=self.toubu(shuju[1][0],int(shuju[1][1]))
        self.assertIn('welcome, zhangsan !', html)

    def test_3(self):
        shuju=self.shu()
        html=self.toubu(shuju[2][0],int(shuju[2][1]))
        self.assertIn('welcome, zhangsan !', html)

    def test_4(self):
        shuju=self.shu()
        html=self.toubu(shuju[3][0],int(shuju[3][1]))
        self.assertIn('welcome, zhangsan !', html)

if __name__ == '__main__':
    unittest.main()



