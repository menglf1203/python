# /usr/bin/env python
# -*- coding:utf-8 -*-

import HTMLTestRunnertest
import HTMLTestRunne
import unittest
from app自动化.test.喔图测试 import *

class baogao():
    def baocun(self):
        suit=unittest.TestSuite()
        suit.addTest(unittest.makeSuite(ceshi))
        now=time.strftime('%Y %m %d %X',time.localtime(time.time()))
        f=open(r'C:\Users\meng\Desktop\a.html','wb')
        runner=HTMLTestRunne.HTMLTestRunner(tester='小仙女',title='手机app',description='测试报告如下',stream=f)
        runner.run(suit)
        f.close()

    def baocun1(self):
        suit = unittest.TestSuite()
        suit.addTest(unittest.makeSuite(ceshi))
        now = time.strftime('%Y %m %d %X', time.localtime(time.time()))
        f = open(r'C:\Users\meng\Desktop\wotu.html', 'wb')
        runner = HTMLTestRunne.HTMLTestRunner(tester='小仙女', title='手机app', description='测试报告如下', stream=f)
        runner.run(suit)
        f.close()

