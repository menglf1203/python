# /usr/bin/env python
# -*- coding:utf-8 -*-

from app自动化.config.登录 import *
from app自动化.data.数据 import *

class ceshi(unittest.TestCase):
    def test_1(self):
        aa=shuju()
        bb=denglu()
        shu1=aa.shu1()
        dr=bb.bbb(int(shu1[0][0]),int(shu1[0][1]))
        wd = dr.find_elements_by_class_name('android.widget.TextView')
        for i in wd:
            j = i.text
            self.assertIsNotNone(j)



