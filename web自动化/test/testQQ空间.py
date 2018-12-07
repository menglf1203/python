# /usr/bin/env python
# -*- coding:utf-8 -*-


from web自动化.config.登录 import Dl
from web自动化.data.读取数据 import Dq
import unittest
import time
import HTMLTestRunnertest
from time import sleep


class QQ(unittest.TestCase):
    def test_1(self):
        denglu=Dl()
        duqu=Dq()
        shuju=duqu.QQdenglu()
        dr=denglu.QQkj(shuju[0][0],shuju[0][1])
        sleep(2)
        self.assertNotEqual(dr.current_url, 'https://qzone.qq.com/')


    def test_2(self):
        denglu = Dl()
        duqu = Dq()
        shuju = duqu.QQdenglu()
        hang=len(shuju)
        for i in range(hang):
            dr = denglu.QQkj(shuju[1][0], shuju[1][1])
            sleep(3)
            self.assertEqual(dr.current_url, 'https://qzone.qq.com/')





