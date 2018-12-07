# /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from time import sleep
from web自动化.config.登录 import Dl
from selenium.webdriver.common.action_chains import ActionChains


class Dlu(unittest.TestCase):

    def test_1(self):
        dl=Dl()
        dr=dl.denglu2()
        dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/li[2]/a/img').click()
        sleep(1)
        wd = dr.find_element_by_xpath('//*[@id="login"]').is_displayed()
        sleep(2)
        self.assertEqual(wd,True)
        sleep(2)
        dr.quit()

    def test_2(self):
        dl = Dl()
        dr = dl.denglu2()
        wd = dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/li[3]/a/img')
        sleep(2)
        ActionChains(dr).move_to_element(wd).perform()
        aa = dr.find_element_by_id('saveCodeDiv').is_displayed()
        self.assertEqual(aa, True)
        sleep(2)
        dr.quit()

    def test_3(self):
        dl = Dl()
        dr = dl.denglu2()
        dr.find_element_by_xpath('//*[@id="userForm"]/div[3]/a').click()
        wd = dr.find_element_by_name('phone').is_displayed()
        self.assertEqual(wd, True)
        sleep(2)
        dr.quit()

    def test_4(self):
        dl = Dl()
        dr = dl.denglu2()
        dr.find_element_by_class_name('loginBtn').click()
        wd = dr.find_element_by_class_name('current').is_displayed()
        self.assertEqual(wd, True)
        sleep(2)
        dr.quit()




