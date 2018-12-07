# /usr/bin/env python
# -*- coding:utf-8 -*-



from web自动化.config.登录 import Dl
import unittest
import time
import HTMLTestRunnertest
from time import sleep



class Jingdong(unittest.TestCase):
    def test_1(self):
        dl=Dl()
        dr=dl.jingdong()
        ww=dr.find_element_by_class_name('ftx-02').is_displayed()  # 判断有没有显示在页面上
        self.assertEqual(ww,True)

    def test_2(self):
        dl=Dl()
        dr=dl.jingdong()
        sleep(2)
        dr.find_element_by_xpath('//*[@id="settleup-2014"]/div[1]/a').click()
        sleep(2)
        ww=dr.find_element_by_class_name('p-name').is_displayed()
        sleep(2)
        self.assertEqual(ww,True)



