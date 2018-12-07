# /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from 自动化框架.config配置.登录_接口 import *
from 自动化框架.data数据.读取数据 import *

class haofenshu1(unittest.TestCase):
    wenjian=Duqu.haofenshu1
    html=学校_查询.haofenshu1

    def test_1(self):
        shuju=self.wenjian()
        if type(shuju[0][1])!=str:
            toubu=self.html(shuju[0][0],int(shuju[0][1]))
        else:
            toubu = self.html(shuju[0][0], shuju[0][1])
        self.assertNotEqual('登录成功', toubu)
        self.assertEqual(toubu['code'],0)

    def test_2(self):
        shuju = self.wenjian()
        if type(shuju[1][1]) != str:
            toubu = self.html(shuju[1][0], int(shuju[1][1]))
        else:
            toubu = self.html(shuju[1][0], shuju[1][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

    def test_3(self):
        shuju = self.wenjian()
        if type(shuju[2][1]) != str:
            toubu =self.html(shuju[2][0], int(shuju[2][1]))
        else:
            toubu = self.html(shuju[2][0],shuju[2][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

    def test_4(self):
        shuju = self.wenjian()
        if type(shuju[3][1]) != str:
            toubu =self.html(shuju[3][0], int(shuju[3][1]))
        else:
            toubu = self.html(shuju[3][0], shuju[3][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)


    def test_5(self):
        shuju = self.wenjian()
        if type(shuju[4][1]) != str:
            toubu =self.html(shuju[4][0], int(shuju[4][1]))
        else:
            toubu = self.html(shuju[4][0], shuju[4][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

    def test_6(self):
        shuju = self.wenjian()
        if type(shuju[5][1]) != str:
            toubu =self.html(shuju[5][0], int(shuju[5][1]))
        else:
            toubu = self.html(shuju[5][0], shuju[5][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

    def test_7(self):
        shuju = self.wenjian()
        if type(shuju[6][1]) != str:
            toubu =self.html(shuju[6][0], int(shuju[6][1]))
        else:
            toubu = self.html(shuju[6][0], shuju[6][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

    def test_8(self):
        shuju = self.wenjian()
        if type(shuju[7][1]) != str:
            toubu =self.html(shuju[7][0], int(shuju[7][1]))
        else:
            toubu = self.html(shuju[7][0], shuju[7][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

    def test_9(self):
        shuju = self.wenjian()
        if type(shuju[8][1]) != str:
            toubu =self.html(shuju[8][0], int(shuju[8][1]))
        else:
            toubu = self.html(shuju[8][0], shuju[8][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

    def test_10(self):
        shuju = self.wenjian()
        if type(shuju[9][1]) != str:
            toubu =self.html(shuju[9][0], int(shuju[9][1]))
        else:
            toubu = self.html(shuju[9][0], shuju[9][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

    def test_11(self):
        shuju = self.wenjian()
        if type(shuju[10][1]) != str:
            toubu =self.html(shuju[10][0], int(shuju[10][1]))
        else:
            toubu = self.html(shuju[10][0], shuju[10][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

    def test_12(self):
        shuju = self.wenjian()
        if type(shuju[11][1]) != str:
            toubu =self.html(shuju[11][0], int(shuju[11][1]))
        else:
            toubu = self.html(shuju[11][0], shuju[11][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)

    def test_13(self):
        shuju = self.wenjian()
        if type(shuju[12][1]) != str:
            toubu =self.html(shuju[12][0], int(shuju[12][1]))
        else:
            toubu = self.html(shuju[12][0], shuju[12][1])
        self.assertNotIn('登录成功', toubu)
        self.assertNotEqual('code', 0)



