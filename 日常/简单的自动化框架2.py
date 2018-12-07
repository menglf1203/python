# /usr/bin/env python
# -*- coding:utf-8 -*-

# 用python 代码生成测试报告
import unittest
import requests
import HTMLTestRunne         # 英文测试报告  不能pip下载，也不能python去下载
import HTMLTestRunnertest    # 中文测试报告  是在网上流传的
import time


class Haofenshu(unittest.TestCase):

    def toubu(self,city):
        head = {
            'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
        }
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
        city = {'filterInput': '{}'.format(city)}
        res = requests.get(url=url, headers=head, params=city)
        html = res.json()
        return html

    def test1(self):
        html=self.toubu('北京')
        self.assertEqual(html['code'],0)

    def test2(self):
        html=self.toubu('^&*')
        self.assertFalse(html['code']==0)

    def test3(self):
        html=self.toubu('666')
        self.assertFalse(html['code']==0)

# if __name__ == '__main__':
#     unittest.main()


# 生成测试报告，生成一个测试套件
suit=unittest.TestSuite()

# 添加测试用例 将测试用例添加到测试套件中
# 1.添加class类名(测试名)
for i in range(1,4):
    suit.addTest(Haofenshu('test{}'.format(i)))
# 2.将整个类中的所有测试用例添加到测试套件中(根据函数的名字如果以test开头才会添加)
suit.addTest(unittest.makeSuite(Haofenshu))
# 设置时间
now=time.strftime('%Y %m %d %H-%M-%S',time.localtime())
# with open('abc.html','w') as f:
#     f.read()
f=open('abcd.html','wb')
runner=HTMLTestRunne.HTMLTestRunner(tester='小仙女',
                                         description='测试结果如下',
                                         title='好分数测试报告',
                                         stream=f)

runner.run(suit)
f.close()