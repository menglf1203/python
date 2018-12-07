# /usr/bin/env python
# -*- coding:utf-8 -*-

from 自动化框架.report测试报告.报告 import *

# if __name__ == '__main__':
#     yunxing = Baogao()
#     with open(r'../driver测试用例/需要测试的文件.txt','r') as f:
#         bb=f.readlines()
#         if 'all' in bb:
#             yunxing.run_所有()
#         else:
#             yunxing.run_任意(bb)


# if __name__ == '__main__':
#     yunxing = Baogao()
#     with open(r'../driver测试用例/app需要测试的文件.txt','r') as f:
#         bb=f.readlines()
#         if 'all' in bb:
#             yunxing.run_所有()
#         else:
#             yunxing.apprun_任意(bb)

if __name__ == '__main__':
    yunxing = Baogao()
    with open(r'../driver测试用例/好分数需要测试的文件.txt','r') as f:
        bb=f.readlines()
        if 'all' in bb:
            yunxing.run_所有()
        else:
            yunxing.hao_任意(bb)