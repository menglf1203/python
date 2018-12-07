# /usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from 自动化框架.config配置.登录_接口 import *
from 自动化框架.data数据.读取数据 import *

class ceshi(unittest.TestCase):
    wenjian=Duqu.appwenjian
    toubu=Appt.apptoubu
    def test_1(self):
        shuju = self.wenjian()
        tou = self.toubu(shuju[0][0])
        self.assertIn('detailUrl' ,tou)
        self.assertIn('images', tou)
        self.assertIn('subhead', tou)

    def test_2(self):
        shuju = self.wenjian()
        tou = self.toubu(shuju[1][0])
        self.assertEqual('{}', tou)

    def test_3(self):
        shuju = self.wenjian()
        tou = self.toubu(shuju[2][0])
        self.assertIn('html', tou)

    def test_4(self):
        shuju = self.wenjian()
        tou = self.toubu(shuju[3][0])
        self.assertEqual('{"msg":"天呢！商品id不能为空","code":"1"}', tou)

    def test_5(self):
        shuju = self.wenjian()
        tou = self.toubu(shuju[4][0])
        self.assertIn('html', tou)

    def test_6(self):
        shuju = self.wenjian()
        tou = self.toubu(shuju[5][0])
        self.assertIn('html', tou)