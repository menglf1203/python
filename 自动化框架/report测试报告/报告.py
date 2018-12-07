# /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import time
import HTMLTestRunnertest
import HTMLTestRunne
from 自动化框架.test测试代码.test学校 import *
from 自动化框架.test测试代码.test查询 import *

class Baogao():

    def run_所有(self):
        suit = unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(r'..\test测试代码',pattern='test*.py')
        print(discover)
        # discover 发现,支持通过正则表达式去匹配所有的用例  pattern
        suit.addTest(discover)
        rnow = time.strftime('%Y %m %d %X', time.localtime(time.time()))
        f = open(r'../report测试报告/renyi.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='小仙女',
                                                   description='测试结果如下',
                                                   title='总测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()

    def run_任意(self,bb):
        suit = unittest.TestSuite()
        for i in bb:
            discover = unittest.defaultTestLoader.discover(r'..\test测试代码', pattern='{}.py'.format(i.strip()))
            suit.addTest(discover)
        now = time.strftime('%Y %m %d %X', time.localtime(time.time()))
        with open(r'../report测试报告/all.html', 'wb') as f:
            runner = HTMLTestRunnertest.HTMLTestRunner(tester='小仙女',
                                                       description='测试结果如下',
                                                       title='666测试报告',
                                                       stream=f)
            runner.run(suit)

    def apprun_任意(self,a):
        suit = unittest.TestSuite()
        for i in a:
            print(i)
            discover = unittest.defaultTestLoader.discover(r'..\test测试代码', pattern='{}.py'.format(i.strip()))
            suit.addTest(discover)
        now = time.strftime('%Y %m %d', time.localtime(time.time()))
        f = open(r'../report测试报告/apprenyi.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(title='商品详情测试报告', tester='小仙女', stream=f, description='测试结果如下')
        runner.run(suit)
        f.close()

    def hao_任意(self,a):
        suit = unittest.TestSuite()
        for i in a:
            discover = unittest.defaultTestLoader.discover(r'..\test测试代码', pattern='{}.py'.format(i.strip()))
            suit.addTest(discover)
        now = time.strftime('%Y %m %d', time.localtime(time.time()))
        f = open('../report测试报告/haofenshu1.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(title='好分数测试', tester='小仙女', description='测试结果如下', stream=f)
        runner.run(suit)
        f.close()



