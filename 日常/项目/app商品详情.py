# /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import time
import xlrd
import HTMLTestRunne
import HTMLTestRunnertest
import requests
#
# class App(unittest.TestCase):
#     def toubu(self,a):
#         url = "http://www.zhaoapi.cn/product/getProductDetail"
#         if type(a)==float or type(a)==int:
#             querystring = {"pid": "{}".format(int(a))}
#         else:
#             querystring = {"pid": "{}".format(a.strip())}
#         payload = ""
#         headers = {
#             'cache-control': "no-cache",
#             'Postman-Token': "c7722f39-f0a0-4330-bfea-5f67db4dae6f"
#         }
#         response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
#         html=response.content.decode()
#         print(html)
#         print(type(html))
#         return html
#
#     def wenjian(self):
#         shuju=[]
#         f=xlrd.open_workbook(r'C:\Users\meng\Desktop\app\app.xlsx')
#         sheet=f.sheets()[0]
#         hang=sheet.nrows
#         for i in range(1,hang):
#             shuju.append(sheet.row_values(i))
#         print(shuju)
#         return shuju
#
#     def test_1(self):
#         shuju = self.wenjian()
#         tou = self.toubu(shuju[0][0])
#         self.assertIn('detailUrl',tou)
#         self.assertIn('images', tou)
#         self.assertIn('subhead', tou)
#
#     def test_2(self):
#         shuju = self.wenjian()
#         tou = self.toubu(shuju[1][0])
#         self.assertIn('detailUrl', tou)
#         self.assertIn('images', tou)
#         self.assertIn('subhead', tou)
#
#
#     def test_3(self):
#         shuju = self.wenjian()
#         tou = self.toubu(shuju[2][0])
#         self.assertIn('detailUrl', tou)
#         self.assertIn('images', tou)
#         self.assertIn('subhead', tou)
#
#     def test_4(self):
#         shuju = self.wenjian()
#         tou = self.toubu(shuju[3][0])
#         self.assertIn('detailUrl', tou)
#         self.assertIn('images', tou)
#         self.assertIn('subhead', tou)
#
#     def test_5(self):
#         shuju = self.wenjian()
#         tou = self.toubu(shuju[4][0])
#         self.assertIn('detailUrl', tou)
#         self.assertIn('images', tou)
#         self.assertIn('subhead', tou)
#
#
# suit=unittest.TestSuite()
# suit.addTest(unittest.makeSuite(App))
# now=time.strftime('%Y %m %d',time.localtime(time.time()))
# f=open('app.html','wb')
# runner=HTMLTestRunnertest.HTMLTestRunner(title='商品详情测试报告',tester='小仙女',stream=f,description='测试结果如下')
# runner.run(suit)
# f.close()



class app2(unittest.TestCase):
    def toubu(self,a):
        url = "http://www.zhaoapi.cn/product/getProductCatagory"
        querystring = {"cid": "{}".format(a)}
        payload = ""
        headers = {
            'cache-control': "no-cache",
            'Postman-Token': "4390cbb2-a586-4a9c-b469-896a882a5a24"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        html=response.content.decode()
        return html

    def wenjian(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\meng\Desktop\python\自动化框架\data数据\商品子分类.xlsx')
        sheet=f.sheets()[0]
        hang=sheet.nrows
        for i in range(1,hang):
            shuju.append(i)

        return shuju

    def test_1(self):
        shuju=self.wenjian()
        html=self.toubu(shuju)
        self.assertIn('cid',html)

    def test_2(self):
        shuju=self.wenjian()
        html=self.toubu(shuju)
        self.assertIn('cid', html)

suit=unittest.TestSuite()
suit.addTest(unittest.makeSuite(app2))
now=time.strftime('%Y %m %d %X',time.localtime(time.time()))
f=open('app2.html','wb')
runner=HTMLTestRunnertest.HTMLTestRunner(title='商品子分类结果',tester='小仙女',description='测试结果如下',stream=f)
runner.run(suit)
f.close()


