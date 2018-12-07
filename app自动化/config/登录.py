# /usr/bin/env python
# -*- coding:utf-8 -*-

from appium import webdriver
from time import sleep
import unittest
import time


class denglu():
    def aaa(self,a,b):
        desired_caps={'platformName':'Android',
        #              'platformVersion':'4.4.2',
                      'deviceName':'127.0.0.1:62001',
                      'appPackage':'com.netease.cloudmusic',
                      'appActivity':'activity.LoadingActivity'}
        # 1.测试平台是ios还是安卓 2.设备的版本 3. 设备的序列号\ip  4. 要测试的包名 5. 测试的activity
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 客户端连接服务器  appium服务器的地址
        sleep(10)
        driver.find_element_by_id('com.netease.cloudmusic:id/h_').click()
        sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/eq').click()
        sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/a1g').clear()
        sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/a1g').send_keys('{}'.format(a))
        sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/ep').send_keys('{}'.format(b))
        sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/eq').click()
        try:
            sleep(10)
        except:
            sleep(30)
        driver.find_element_by_id('com.netease.cloudmusic:id/apf').click()
        sleep(5)
        return driver

    def bbb(self,a,b):
        de = {'platformName': 'Android', 'deviceName': '127.0.0.1:622001',
              'appPackage': 'com.alltuu.android',
              'appActivity': 'android.alltuu.com.newalltuuapp.splash.SplashActivity'}
        dr = webdriver.Remote('http://localhost:4723/wd/hub', de)
        sleep(10)
        dr.find_element_by_id('com.alltuu.android:id/phone_edittext').clear()
        sleep(3)
        dr.find_element_by_id('com.alltuu.android:id/phone_edittext').send_keys('{}'.format(a))
        sleep(3)
        dr.find_element_by_id('com.alltuu.android:id/password_edittext').send_keys('{}'.format(b))
        sleep(3)
        dr.find_element_by_id('com.alltuu.android:id/remember_pw_icon_unchecked').click()
        sleep(3)
        dr.find_element_by_id('com.alltuu.android:id/login_btn').click()
        sleep(10)
        return dr



