# /usr/bin/env python
# -*- coding:utf-8 -*-

import re
import requests
import os

class Doutula():

    def neirong(self):
        lianjie=[]
        mingcheng=[]

        url = 'http://www.doutula.com/article/list/?page=8'
        res = requests.get(url=url,headers=head)
        html = res.content.decode('UTF-8')
        patt = re.compile(r'<a href="(.*?)" class="list-group')
        items=patt.findall(html)
        for i in items:
            lianjie.append(i)

        patt2=re.compile(r'<div class="random_title">(.*?)<div class="date">')
        items2=patt2.findall(html)
        for i in items2:
            mingcheng.append(i)

        neirong=list(zip(lianjie,mingcheng))
        return neirong

    def baocun(self,neirong):

        for i,j in neirong:
            res=requests.get(url=i,headers=head)
            html=res.content.decode()
            patt=re.compile(r'onerror="this.src=(.*?)">')
            items=patt.findall(html)
            a=0
            j=j.replace('?','')
            os.mkdir(r'C:\Users\meng\Desktop\python\{}'.format(j))
            for h in items:
                h=h.replace("'",'')
                tupian=requests.get(url=h,headers=head)
                items2=tupian.content
                if 'jpg' in h:
                    with open(r'C:\Users\meng\Desktop\python\{}\{}.jpg'.format(j,a),'wb') as f:
                        f.write(items2)
                        a+=1
                elif 'gif' in h:
                    with open(r'C:\Users\meng\Desktop\python\{}\{}.gif'.format(j,a),'wb') as f:
                        f.write(items2)
                        a+=1

doutula=Doutula()
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
a=doutula.neirong()
doutula.baocun(a)
