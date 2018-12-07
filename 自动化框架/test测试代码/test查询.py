# /usr/bin/env python
# -*- coding:utf-8 -*-


import time
import HTMLTestRunne
from 自动化框架.config配置.登录_接口 import *
from 自动化框架.data数据.读取数据 import *
import unittest

class 查询(unittest.TestCase):

    tes_学校 = 学校_查询().学校_快查
    shuju = Duqu().duqu()

    def test1(self):
        html=self.tes_学校(self.shuju[0][0])
        self.assertEqual(html['code'],int(self.shuju[0][1]))

    def test2(self):
        html=self.tes_学校(self.shuju[1][0])
        self.assertTrue(html['code']==int(self.shuju[1][1]))

    def test3(self):
        html=self.tes_学校(self.shuju[2][0])
        self.assertTrue(html['code']==int(self.shuju[2][1]))
        self.assertIn('学校',html['msg'])

    def test4(self):
        html=self.tes_学校(self.shuju[3][0])
        self.assertTrue(html['code']==int(self.shuju[3][1]))


