# /usr/bin/env python
# -*- coding:utf-8 -*-

from web自动化.config.登录 import *
from web自动化.data.读取数据 import *
import unittest
import time
import HTMLTestRunnertest

class Cs(unittest.TestCase):

    def test_1(self):
        dq = Dq()
        dl = Dl()
        shuju = dq.denglu1()
        dr = dl.denglu1(shuju[0][0], shuju[0][1])
        sleep(2)
        ww=dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div/div/li/a').is_displayed()
        self.assertEqual(ww,True)
        dr.quit()

    def test_2(self):
        dq = Dq()
        dl = Dl()
        shuju=dq.denglu1()
        hang=len(shuju)
        for i in range(1,hang):
            dr=dl.denglu1(shuju[i][0],shuju[i][1])
            sleep(2)
            if dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').is_displayed()==True:
                wd = dr.find_elements_by_class_name('err-info')
                cuowu=[]
                for i in wd:
                    a=i.text
                    cuowu.append(a)
                print('{}{}'.format(cuowu[0],cuowu[1]))
                ww=dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').is_displayed()
                self.assertEqual(ww, True)
                dr.quit()

