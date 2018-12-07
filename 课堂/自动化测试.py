# /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest  # 单元测试
import requests
import json
import time
import HTMLTestRunne
from aaa.HTMLTestRunne import HTMLTestRunner
import xlrd

# head={'cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
# city='河南'
# params={'filterInput':'{}'.format(city)}
# url='http://testsupport-be.haofenshu.com/v1/schools/infos'
# res=requests.get(url=url,headers=head,params=params)
# html=res.json()

#接受数据可以有两种方式  1,调用json模块   2,直接使用json

# html=res.content.decode('utf-8')
# aa=json.loads(html)
# print(aa)

# print(html['code'])   # 取某个键的值
# assert html['code'] == 1
# 简单的断言   in包含预期结果  ！=是不等于

# class Haofenshu():
#     def duanyan1(a):
#         head = {'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
#         params = {'filterInput': '{}'.format(a)}
#         url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#         res = requests.get(url=url, headers=head, params=params)
#         html = res.json()
#         assert html['code'] == 0



# unittest.TestCase 测试用例，主要用于用例管理
# unittest.TestSuite 测试套件，多个测试用例结合在一起
# unittest.TestLoader 测试载入，将测试用例加载到测试套件中
# unittest.TestRunner 执行测试用例

# class Test(unittest.TestCase):
#
#     def setUp(self):                  # 作用：初始化测试环境，在每次执行测试用例前执行（保证每个用例在相同环境下去执行）
#         print('开始')
#     def tearDown(self):               # 在每次执行测试用例后执行
#         print('关闭')
#     def test1(self):
#         print('a')
#     def test2(self):
#         print('b')
#
# unittest.main()


# import unittest
# import requests
# import HTMLTestRunne
# import HTMLTestRunnertest
# import xlrd
#
# # 断言
# # class Haofenshu(unittest.TestCase):
# #
# #     def test_2(self):
# #         self.assertNotEqual('a', 'b')
# #
# #     def test_1(self):
# #         self.assertEqual('a','1a')
# #
# #
# # if __name__ == '__main__':
# #     unittest.main()
#
#
#
# class Haofenshu(unittest.TestCase):
#
#     def toubu(self,city):
#         head = {
#             'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
#         }
#         url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#         city = {'filterInput': '{}'.format(city)}
#         res = requests.get(url=url, headers=head, params=city)
#         html = res.json()
#         return html
#
#     def test1(self):
#         html=self.toubu('北京')
#         self.assertEqual(html['code'],0)
#
#     def test2(self):
#         html=self.toubu('^&*')
#         self.assertFalse(html['code']==0)
#
#     def test3(self):
#         html=self.toubu('666')
#         self.assertFalse(html['code']==0)
#
# if __name__ == '__main__':
#     unittest.main()


# 用python 代码生成测试报告
# import unittest
# import requests
# # import HTMLTestRunne         # 英文测试报告  不能pip下载，也不能python去下载
# # import HTMLTestRunnertest    # 中文测试报告  是在网上流传的
# import time
# from aaa.HTMLTestRunnertest import HTMLTestRunner
#
# class Haofenshu(unittest.TestCase):
#
#     def toubu(self,city):
#         head = {
#             'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
#         }
#         url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#         city = {'filterInput': '{}'.format(city)}
#         res = requests.get(url=url, headers=head, params=city)
#         html = res.json()
#         return html
#
#     def test1(self):
#         html=self.toubu('北京')
#         self.assertEqual(html['code'],0)
#
#     def test2(self):
#         html=self.toubu('^&*')
#         self.assertFalse(html['code']==0)
#
#     def test3(self):
#         html=self.toubu('666')
#         self.assertFalse(html['code']==0)
#
# # if __name__ == '__main__':
# #     unittest.main()
#
#
# # 生成测试报告，生成一个测试套件(不加main 也不能加setup和teardown)
# suit=unittest.TestSuite()
#
# # 添加测试用例 将测试用例添加到测试套件中
# # 1.添加class类名(测试名)
# # for i in range(1,4):
# #     suit.addTest(Haofenshu('test{}'.format(i)))
# # 2.将整个类中的所有测试用例添加到测试套件中(根据函数的名字如果以test开头才会添加)
# suit.addTest(unittest.makeSuite(Haofenshu))
# # 设置时间
# now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
# # with open('abc.html','w') as f:
# #     f.read()
# f=open('abc.html','wb')
# runner=HTMLTestRunnertest.HTMLTestRunner(tester='小仙女',
#                                          description='测试结果如下',
#                                          title='好分数测试报告',
#                                          stream=f)
# runner.run(suit)
# f.close()





# 2018.11.17
# 用python 代码生成英文的测试报告
# import unittest
# import requests
# import time
# import HTMLTestRunne
# from aaa.HTMLTestRunne import HTMLTestRunner
# import xlrd
#
# class Haofenshu(unittest.TestCase):
#     def shu(self):
#         shuju=[]
#         f=xlrd.open_workbook('好分数.xls')
#         sheet=f.sheets()[0]
#         num=sheet.nrows
#         for i in range(1,num):
#             sj=sheet.row_values(i)
#             shuju.append(sj)
#         return shuju
#
#     def toubu(self,city):
#         head = {
#             'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
#         }
#         url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#         city = {'filterInput': '{}'.format(city)}
#         res = requests.get(url=url, headers=head, params=city)
#         html = res.json()
#         return html
#
#     def test1(self):
#         shuju=self.shu()
#         html=self.toubu(shuju[0][0])
#         self.assertEqual(html['code'],int(shuju[0][1]))
#
#     def test2(self):
#         shuju = self.shu()
#         html=self.toubu(shuju[1][0])
#         self.assertTrue(html['code']==int(shuju[1][1]))
#
#     def test3(self):
#         shuju = self.shu()
#         html=self.toubu(shuju[2][0])
#         self.assertTrue(html['code']==int(shuju[2][1]))
#         self.assertIn('学校',html['msg'])
#
#     def test4(self):
#         shuju = self.shu()
#         html=self.toubu(shuju[3][0])
#         self.assertTrue(html['code']==int(shuju[3][1]))
#
# suit=unittest.TestSuite()
# suit.addTest(unittest.makeSuite(Haofenshu))
# now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
# f=open('abcd.html','wb')
# runner=HTMLTestRunne.HTMLTestRunner(tester='小仙女',
#                                          description='测试结果如下',
#                                          title='好分数测试报告',
#                                          stream=f)
# runner.run(suit)
# f.close()





