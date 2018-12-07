# /usr/bin/env python
# -*- coding:utf-8 -*-


import unittest
import xlrd
import HTMLTestRunnertest
import HTMLTestRunne
import requests
import time

class Hao1(unittest.TestCase):
    def wenjian(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\meng\Desktop\app\好分数1.xlsx')
        sheet=f.sheets()[0]
        hang=sheet.nrows
        for i in range(1,hang):
            shuju.append(sheet.row_values(i))
        return shuju


    def toubu(self,a,b):
        url = "http://testsupport-be.haofenshu.com/v1/accounts/session"
        payload = "account={}&password={}".format(a,b)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'Postman-Token': "20d04552-d6ec-43c0-8d8d-22c5adba170c"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        html=response.json()
        return html

    def test_1(self):
        shuju=self.wenjian()
        toubu=self.toubu(shuju[0][0],int(shuju[0][1]))
        self.assertNotEqual('登录成功', toubu)
        self.assertEqual(toubu['code'],0)

    def test_2(self):
        shuju = self.wenjian()
        toubu = self.toubu(shuju[1][0], int(shuju[1][1]))
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

    def test_3(self):
        shuju = self.wenjian()
        toubu = self.toubu(shuju[2][0], int(shuju[2][1]))
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

suit=unittest.TestSuite()
suit.addTest(unittest.makeSuite(Hao1))
now=time.strftime('%Y %m %d',time.localtime(time.time()))
f=open('hao1.html','wb')
runner=HTMLTestRunnertest.HTMLTestRunner(title='好分数测试',tester='小仙女',description='测试结果如下',stream=f)
runner.run(suit)
f.close()



