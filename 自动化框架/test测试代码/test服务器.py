# /usr/bin/env python
# -*- coding:utf-8 -*-


import unittest
from 自动化框架.config配置.登录_接口 import 学校_查询
from 自动化框架.data数据.读取数据 import Duqu


class 服务器(unittest.TestCase):
    shuju = Duqu().服务器()
    toubu = 学校_查询().服务器

    def test1(self):
        html=self.toubu(self.shuju[0][0],self.shuju[0][1])
        self.assertIn('welcome',html)
    def test2(self):
        html=self.toubu(self.shuju[1][0],self.shuju[1][1])
        self.assertIn('welcome',html)

    def test3(self):
        html = self.toubu(self.shuju[2][0], self.shuju[3][1])
        self.assertIn('welcome', html)

    def test4(self):
        html = self.toubu(self.shuju[3][0], self.shuju[3][1])
        self.assertIn('welcome', html)


