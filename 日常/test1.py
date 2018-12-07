# /usr/bin/env python
# -*- coding:utf-8 -*-

from appium import webdriver
from time import sleep
import unittest
import time
import HTMLTestRunnertest
import HTMLTestRunne

# 上课讲的
# desired_caps={'platformName':'Android',
# #              'platformVersion':'4.4.2',
#               'deviceName':'127.0.0.1:62001',
#               'appPackage':'com.alltuu.android',
#               'appActivity':'android.alltuu.com.newalltuuapp.splash.SplashActivity'}
# # 1.测试平台是ios还是安卓 2.设备的版本 3. 设备的序列号\ip  4. 要测试的包名 5. 测试的activity

# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# 客户端连接服务器  appium服务器的地址



# 面向对象
# class Aa():
#     def aaa(self):
#         desired_caps={'platformName':'Android',
#         #              'platformVersion':'4.4.2',
#                       'deviceName':'127.0.0.1:62001',
#                       'appPackage':'com.netease.cloudmusic',
#                       'appActivity':'activity.LoadingActivity'}
#         # 1.测试平台是ios还是安卓 2.设备的版本 3. 设备的序列号\ip  4. 要测试的包名 5. 测试的activity
#         driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#         # 客户端连接服务器  appium服务器的地址
#         sleep(10)
#         driver.find_element_by_id('com.netease.cloudmusic:id/h_').click()
#         sleep(3)
#         driver.find_element_by_id('com.netease.cloudmusic:id/eq').click()
#         sleep(3)
#         driver.find_element_by_id('com.netease.cloudmusic:id/a1g').clear()
#         sleep(3)
#         driver.find_element_by_id('com.netease.cloudmusic:id/a1g').send_keys('17839216322')
#         sleep(3)
#         driver.find_element_by_id('com.netease.cloudmusic:id/ep').send_keys('123456')
#         sleep(3)
#         driver.find_element_by_id('com.netease.cloudmusic:id/eq').click()
#         try:
#             sleep(10)
#         except:
#             sleep(30)
#         driver.find_element_by_id('com.netease.cloudmusic:id/apf').click()
#         sleep(5)
#         return driver
# class Bb(unittest.TestCase):
#     def test_1(self):
#         aa=Aa()
#         dr=aa.aaa()
#         dr.find_element_by_id('com.netease.cloudmusic:id/k1').click()
#         sleep(4)
#         wd=dr.find_element_by_id('com.netease.cloudmusic:id/xo').text
#         self.assertNotEqual(wd,None)
#         sleep(3)
#
# class Cc():
#     def baocun(self):
#         suit=unittest.TestSuite()
#         suit.addTest(unittest.makeSuite(Bb))
#         now=time.strftime('%Y %m %d %X',time.localtime(time.time()))
#         f=open(r'C:\Users\meng\Desktop\a.html','wb')
#         runner=HTMLTestRunne.HTMLTestRunner(tester='小仙女',title='手机app',description='测试报告如下',stream=f)
#         runner.run(suit)
#         f.close()
#
# if __name__ == '__main__':
#     cc=Cc()
#     cc.baocun()
#




# 网易云音乐

# from appium import webdriver
# import time
#
# desired_caps = {'platformName': 'Android',
# #                'platformVersion':'6.0',
#                 'deviceName':'127.0.0.1:62001',
#                 'appPackage':'com.netease.cloudmusic',
#                 'appActivity':'activity.LoadingActivity'}
#
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# time.sleep(20)
#
# print("立即体验")
# driver.find_element_by_id("com.netease.cloudmusic:id/mx").click()
# time.sleep(3)
#
# print("点击抽屉菜单")
# driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
# time.sleep(3)
#
# print("立即登录")
# driver.find_element_by_id("com.netease.cloudmusic:id/abx").click()
# time.sleep(3)
#
# print("手机号登录")
# driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
# time.sleep(3)
#
# print("输入手机号")
# driver.find_element_by_id("com.netease.cloudmusic:id/i4").send_keys("15537831769")
# time.sleep(3)
#
# print("输入密码")
# driver.find_element_by_id("com.netease.cloudmusic:id/i2").send_keys("gao19930903")
# time.sleep(3)
#
# print("登录")
# driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
# time.sleep(3)
#
# #断言
# print("点击抽屉菜单")
# driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
# time.sleep(3)
#
#
# print("用户名")
# title=driver.find_element_by_id("com.netease.cloudmusic:id/ac2").text
# aa= "用户507297819"
# if title==aa:
#     print("登录成功")
#
# driver.quit()



# 喔图云登录测试
# class aa():
#     def aaa(self):
#         de={'platformName':'Android','deviceName':'127.0.0.1:622001',
#             'appPackage':'com.alltuu.android',
#             'appActivity':'android.alltuu.com.newalltuuapp.splash.SplashActivity'}
#         dr=webdriver.Remote('http://localhost:4723/wd/hub',de)
#
#         # 打印屏幕高和宽
#         print(dr.get_window_size())
#         for i in range(8):
#             # 获取屏幕的高
#             x = dr.get_window_size()['width']
#             # 获取屏幕宽
#             y = dr.get_window_size()['height']
#             # 滑屏，大概从屏幕右边2分之一高度，往左侧滑动,滑动后显示的是 热点tab
#             dr.swipe(9/ 10 * x, 2 / 3 * y, 1 / 10 * x, 2 / 3 * y, 100)
#             time.sleep(4)
#
#         dr.find_element_by_id('com.alltuu.android:id/button').click()
#         sleep(5)
#         dr.find_element_by_id('com.alltuu.android:id/phone_edittext').clear()
#         sleep(3)
#         dr.find_element_by_id('com.alltuu.android:id/phone_edittext').send_keys('17839216322')
#         sleep(3)
#         dr.find_element_by_id('com.alltuu.android:id/password_edittext').send_keys('123456')
#         sleep(3)
#         dr.find_element_by_id('com.alltuu.android:id/remember_pw_icon_unchecked').click()
#         sleep(3)
#         dr.find_element_by_id('com.alltuu.android:id/login_btn').click()
#         sleep(10)
#         return dr
# class bb(unittest.TestCase):
#     def test_1(self):
#         a=aa()
#         dr=a.aaa()
#         wd=dr.find_elements_by_class_name('android.widget.TextView')
#         for i in wd:
#             j=i.text
#             self.assertIsNotNone(j)
#
# suit=unittest.TestSuite()
# suit.addTest(unittest.makeSuite(bb))
# now=time.strftime('%Y %m %d %X',time.localtime(time.time()))
# f=open(r'C:\Users\meng\Desktop\a.html','wb')
# runner=HTMLTestRunnertest.HTMLTestRunner(tester='小仙女',title='喔图云登录',description='测试结果如下',stream=f)
# runner.run(suit)
# f.close()



# 雷电的腾讯新闻点击搜索框
#
# de={'platformName':'Android','deviceName':'emulator-5554',
#     'appPackage':'com.tencent.news','appActivity':'ui.NewsDetailActivity'}
# dr=webdriver.Remote('http://localhost:4723/wd/hub',de)
# sleep(10)
# dr.find_element_by_id('com.tencent.news:id/home_channel_search_box').click()
# sleep(5)
# print('我的')
# dr.find_element_by_id('com.tencent.news:id/search_page_box').send_keys('软件测试')
# sleep(5)
# dr.press_keycode(66)  # 模拟物理按键enter
# sleep(3)
# wd=dr.find_element_by_id('com.tencent.news:id/channelbar_text').is_displayed()
# sleep(5)



de={'platformName':'Android','deviceName':'127.0.0.1:62..1',
    'appPackage':'com.alltuu.android',
    'appActivity':'android.alltuu.com.newalltuuapp.splash.SplashActivity'}

dr=webdriver.Remote('http://localhost:4723/wd/hub',de)
sleep(8)
print(dr.get_window_size())
for i in range(8):
    # 获取屏幕的高
    x = dr.get_window_size()['width']
    # 获取屏幕宽
    y = dr.get_window_size()['height']
    # 滑屏，大概从屏幕右边2分之一高度，往左侧滑动,滑动后显示的是 热点tab
    dr.swipe(9/ 10 * x, 2 / 3 * y, 1 / 10 * x, 2 / 3 * y, 100)
    time.sleep(4)
sleep(5)
dr.find_element_by_id('com.alltuu.android:id/login_btn').click()
sleep(5)
dr.find_element_by_id('com.alltuu.android:id/phone_edittext').send_keys('1789216322')
sleep(5)
dr.find_element_by_id('com.alltuu.android:id/password_edittext').send_keys('123456')
sleep(5)
dr.find_element_by_id('com.alltuu.android:id/login_btn').click()
sleep(5)
dr.find_element_by_xpath('//ViewGroup[5]/ViewGroup').click()
sleep(5)
print('我的')
dr.quit()











