# /usr/bin/env python
# -*- coding:utf-8 -*-


# 职位名称  薪资  公司名称  公司地点

import requests
import re
import pymysql


head={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

a,b,c,d=[],[],[],[]
url='https://www.zhipin.com/c101010100/?query=软件测试&page=2&ka=page-1'
res=requests.get(url=url,headers=head)
html=res.content.decode('utf-8')
patt=re.compile(r'<div class="job-title">(.*?)<div class="job-primary">',re.S)
items=patt.findall(html)
for i in items:
    a.append(i.split('</div>')[0])

    patt1=re.compile(r'<span class="red">(.*?)</span>',re.S)
    items1=patt1.findall(i)
    b.append(items1[0])

    patt2=re.compile(r'<h3 class="name"><a href="/gongsi(.*?)</a></h3>')
    items2=patt2.findall(i)
    items3=items2[0].split('>')[-1]
    c.append(items3)

    patt4=re.compile(r'<div class="info-detail"></div>(.*?)<em class="vline"></em>',re.S)
    items4=patt4.findall(i)
    i=items4[0].split('<p>')[-1]
    d.append(i)

neirong=list(zip(a,b,c,d))
print(neirong)

toubu=['职位名称','薪资','公司名称','公司地点']
aa=pymysql.connect(host='192.168.0.97',port=3306,user='root',passwd='123456',charset='utf8')
bb=aa.cursor()
bb.execute('use test;')
bb.execute('create table boss({} char(30),{} char(30),{} char(30),{} char(30));'.format(toubu[0],toubu[1],toubu[2],toubu[3]))
for h in neirong:
    bb.execute('insert into boss values("{}","{}","{}","{}");'.format(h[0],h[1],h[2],h[3]))

aa.commit()
