# /usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import unittest
import time
import HTMLTestRunnertest
import xlrd


class Fuwuqi(unittest.TestCase):
    def toubu(self,a,b):
        url = "http://192.168.0.57:5000/login"
        payload = {'username':'{}'.format(a),'password':'{}'.format(b)}
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'Postman-Token': "1a10d802-6edc-4f43-8496-df54fc37bbc1"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        toubu=response.content.decode()
        return toubu
    def wenjian(self):
        shuju=[]
        f=xlrd.open_workbook('服务器.xlsx')
        sheet=f.sheets()[0]
        hang=sheet.nrows
        for i in range(1,hang):
            shuju.append(sheet.row_values(i))
        return shuju


    def test_1(self):
        shuju=self.wenjian()
        toubu=self.toubu(shuju[0][0],int(shuju[0][1]))
        self.assertIn('welcome, zhangsan !',toubu)

    def test_2(self):
        shuju=self.wenjian()
        toubu=self.toubu(shuju[1][0],int(shuju[1][1]))
        self.assertIn('welcome, zhangsan !',toubu)

    def test_3(self):
        shuju=self.wenjian()
        toubu=self.toubu(shuju[2][0],int(shuju[2][1]))
        self.assertIn('welcome, zhangsan !',toubu)

suit=unittest.TestSuite()
suit.addTest(unittest.makeSuite(Fuwuqi))
now=time.strftime('%Y %m %d %X',time.localtime(time.time()))
f=open('fueuqi.html','wb')
runner=HTMLTestRunnertest.HTMLTestRunner(title='服务器测试报告',tester='小仙女',description='测试结构如下',stream=f)
runner.run(suit)
f.close()