# /usr/bin/env python
# -*- coding:utf-8 -*-

from app自动化.config.登录 import *
from app自动化.data.数据 import *

class ceshi(unittest.TestCase):
    def test_1(self):
        aa=shuju()
        bb=denglu()
        shu=aa.shu()
        dr=bb.aaa(int(shu[0][0]),int(shu[0][1]))
        dr.find_element_by_id('com.netease.cloudmusic:id/k1').click()
        sleep(4)
        wd=dr.find_element_by_id('com.netease.cloudmusic:id/xo').text
        self.assertNotEqual(wd,None)
        sleep(3)




