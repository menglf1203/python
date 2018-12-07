# /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import time
import HTMLTestRunnertest
from web自动化.test.test京东 import *


class Bg():
    def baogao_all(self):
        suit=unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(r'..\test', pattern='test*.py')
        suit.addTest(discover)
        now=time.strftime('%Y %m %d %X',time.localtime(time.time()))
        f=open(r'C:\Users\meng\Desktop\python\web自动化\report\aaa.html','wb')
        runner=HTMLTestRunnertest.HTMLTestRunner(title='摩尔登录测试报告',tester='小仙女',description='测试结果如下',stream=f)
        runner.run(suit)
        f.close()

    def baogao_任意(self,a):
        suit=unittest.TestSuite()
        for i in a:
            discover=unittest.defaultTestLoader.discover(r'..\test',pattern='{}.py'.format(i.strip()))
            suit.addTest(discover)
        now = time.strftime('%Y %m %d %X', time.localtime(time.time()))
        with open(r'../report/摩尔.html', 'wb') as f:
            runner = HTMLTestRunnertest.HTMLTestRunner(tester='小仙女',
                                                       description='测试结果如下',
                                                       title='摩尔招聘测试报告',
                                                       stream=f)
            runner.run(suit)

    def QQbg(self,a):
        suit = unittest.TestSuite()
        for i in a:
            discover=unittest.defaultTestLoader.discover(r'..\test',pattern='{}.py'.format(i.strip()))
            suit.addTest(discover)
        now = time.strftime('%Y %m %d %X', time.localtime(time.time()))
        f = open(r'C:\Users\meng\Desktop\python\web自动化\report\考试.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(title='QQ空间测试报告', tester='小仙女', description='测试结果如下', stream=f)
        runner.run(suit)
        f.close()

    def jingdong(self):
        suit=unittest.TestSuite()
        suit.addTest(unittest.makeSuite(Jingdong))
        now = time.strftime('%Y %m %d %X', time.localtime(time.time()))
        f = open(r'C:\Users\meng\Desktop\python\web自动化\report\京东.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(title='京东测试报告', tester='小仙女', description='测试结果如下', stream=f)
        runner.run(suit)
        f.close()










