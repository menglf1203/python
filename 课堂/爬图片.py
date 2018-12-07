# /usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re


head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.67 Safari/537.36'}

url=input('输入url')
res=requests.get(url='{}'.format(url),headers=head)
a=res.content.decode('UTF-8')
zhengze=input('请输入正则表达式')
patt=re.compile('{}'.format(zhengze))
items=patt.findall(a)
aaa=0
for i in items:
    if " title=" in i:
        i='http://mpic.spriteapp.cn/'+i
        i=i.split('"')[0]
        tupian=requests.get(url=i)
        res1=tupian.content
        if 'gif' in i:
            with open(r'C:\Users\meng\Desktop\python\图片1\{}.gif'.format(aaa),'wb') as f:
                f.write(res1)
                aaa+=1
        elif 'jpg' in i:
            with open(r'C:\Users\meng\Desktop\python\图片1\{}.jpg'.format(aaa), 'wb') as f:
                f.write(res1)
                aaa += 1


