# /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import time
import HTMLTestRunnertest
from 自动化框架.test测试代码.test学校 import *
from 自动化框架.test测试代码.test查询 import *
from 自动化框架.report测试报告.报告 import *



# class Run():
#
#     def run_所有(self):
#         suit = unittest.TestSuite()
#         discover=unittest.defaultTestLoader.discover(r'..\test测试代码',pattern='test*.py')
#         print(discover)
#         # discover 发现,支持通过正则表达式去匹配所有的用例  pattern
#         suit.addTest(discover)
#         rnow = time.strftime('%Y %m %d %X', time.localtime(time.time()))
#         f = open(r'../report测试报告/renyi.html', 'wb')
#         runner = HTMLTestRunnertest.HTMLTestRunner(tester='小仙女',
#                                                    description='测试结果如下',
#                                                    title='总测试报告',
#                                                    stream=f)
#         runner.run(suit)
#         f.close()
#
#     def run_任意(self,bb):
#         suit = unittest.TestSuite()
#         for i in bb:
#             discover = unittest.defaultTestLoader.discover(r'..\test测试代码', pattern='{}.py'.format(i.strip()))
#             suit.addTest(discover)
#         now = time.strftime('%Y %m %d %X', time.localtime(time.time()))
#         with open(r'../report测试报告/all.html', 'wb') as f:
#             runner = HTMLTestRunnertest.HTMLTestRunner(tester='小仙女',
#                                                        description='测试结果如下',
#                                                        title='666测试报告',
#                                                        stream=f)
#         runner.run(suit)



if __name__ == '__main__':
    yunxing = Baogao()
    with open(r'../driver测试用例/需要测试的文件.txt','r') as f:
        bb=f.readlines()
        if 'all' in bb:
            yunxing.run_所有()
        else:
            yunxing.run_任意(bb)



# if __name__=='__main__':
#     run=Run()
#     run.run_所有()


# if __name__ == '__main__':
#     run = Run()
#     wenjian = run.wenjian()
#     for i in wenjian:
#         j=globals()[i]   # 一个字符串变成一个类的对象
#         run.run_任意(j)


# if __name__ == '__main__':
#     yunxing = Run()
#     wenjian = yunxing.wenjian()
#     print(wenjian)
#     yunxing.run_任意(wenjian)

#
# import unittest
# import xlrd
# import time
# import HTMLTestRunnertest
# import HTMLTestRunne
#
# def renyi(a):
#     suit=unittest.TestSuite()
#     for i in a:
#         print(i)
#         discover=unittest.defaultTestLoader.discover(r'..\test测试代码',pattern='{}.py'.format(i.strip()))
#         suit.addTest(discover)
#     now=time.strftime('%Y %m %d',time.localtime(time.time()))
#     f=open(r'..\report测试报告\ceshi.html','wb')
#     runner=HTMLTestRunnertest.HTMLTestRunner(title='测试报告',tester='小仙女',description='测试结果',stream=f)
#     runner.run(suit)
#     f.close()
#
#
# a=[]
# with open('需要测试的文件.txt','r') as f:
#     aa=f.readlines()
# for i in aa:
#     a.append(i)
# print(a)
# renyi(a)
