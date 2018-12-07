# /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import xlwt
import xlrd
import xlutils
#
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
#
# class Douban:
#
#     def qingqiu(self,page):
#         url = 'https://movie.douban.com/top250?start=50&filter='.format(page)
#         res=requests.get(url=url,headers=head)
#         a=res.content.decode('utf-8')
#         return a
#
#     def guolv(self,a):
#         patt = re.compile('<img width="100" alt="(.*?)" src="https://img')
#         items =patt.findall(a)
#         return items
#
#     def guolv2(self,a):
#         patt = re.compile('<span class="inq">(.*?)</span>')
#         items =patt.findall(a)
#         return items
#
# aaa=1
# dou=Douban()
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('sheet1')
# sheet.write(0, 0, '电影名')
# sheet.write(0, 1, '简介')
# for i in range(0, 250, 25):
#     a=dou.qingqiu(i)
#     b=dou.guolv(a)
#     for j in b:
#         sheet.write(aaa, 0, '{}'.format(j))
#         aaa+=1
# f.save('test2.xls')
# aaa=1
# from xlutils.copy import copy
# f = xlrd.open_workbook('test2.xls')
# new_f=copy(f)
# sheet2=new_f.get_sheet(0)
# for i in range(0, 250, 25):
#     a=dou.qingqiu(i)
#     b=dou.guolv2(a)
#     for j in b:
#         sheet2.write(aaa, 1, '{}'.format(j))
#         aaa+=1
# new_f.save('test2.xls')

#
# import xlwt
# import xlutils
# import xlrd
# import re
# import requests
# import chardet
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
#
#
# dianying=[]
# jianjie=[]
# for i in range(0,251,25):
#     url='https://movie.douban.com/top250?start={}&filter='.format(i)
#     res=requests.get(url=url,headers=head)
#     a=res.content.decode('utf-8')
#     patt=re.compile(r'<div class="pic">(.*?)<div class="item">',re.S)
#     items=patt.findall(a)
#     for i in items:
#         patt1=re.compile(r'<img width="100" alt="(.*?)" src="',re.S)
#         items1=patt1.findall(i)
#         dianying.append(items1[0])
#
#         patt2=re.compile(r'<span class="inq">(.*?)</span>',re.S)
#         items2=patt2.findall(i)
#         jianjie.append(items2[0])
#
# dd=list(zip(dianying,jianjie))
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet1',cell_overwrite_ok=True)
# sheet.write(0,0,'电影名')
# sheet.write(0,1,'简介')
# for i in dd:
#     sheet.write(dd.index(i)+1,0,'{}'.format(i[0]))
#     sheet.write(dd.index(i)+1,1,'{}'.format(i[1]))
# f.save('test3.xls')







#
# url='http://www.budejie.com/pic/1'
# res=requests.get(url=url,headers=head)
# a=res.content.decode('UTF-8')
# patt=re.compile(r'data-original="http://mpic.spriteapp.cn/(.*?)" title="')
# items=patt.findall(a)
# aaa=0
# for i in items:
#     i='http://mpic.spriteapp.cn/'+i
#     tupian=requests.get(i)
#     res1=tupian.content
#     if 'jpg' in i:
#         with open(r'C:\Users\meng\Desktop\python\图片2\{}.jpg'.format(aaa),'wb') as f:
#             f.write(res1)
#             aaa+=1
#     elif 'gif' in i:
#         with open(r'C:\Users\meng\Desktop\python\图片2\{}.gif'.format(aaa),'wb') as f:
#             f.write(res1)
#             aaa += 1


# head={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#
#
# url='https://www.qqtn.com/tp/sgtp_1.html'
# res=requests.get(url=url,headers=head)
# a=res.content.decode('gbk')
# patt=re.compile(r'<li><a href="(.*?)" target="_blank" title="',re.S)
# items=patt.findall(a)
# for i in items:
#     url1='https://www.qqtn.com/'+i
#     res1=requests.get(url=url1,headers=head)
#     a1 = res1.content.decode('gbk')
#     patt1=re.compile(r'<p align="center"><img src="(.*?)"/></p>',re.S)
#     items1=patt1.findall(a1)
#     for j in items1:
#         tupian=requests.get(url=j)
#         res2=tupian.content
#         with open(r'C:\Users\meng\Desktop\python\图片2\{}.jpg'.format(j[-21:-4]),'wb') as f:
#             f.write(res2)
#
# print('over')

#
# import docx
#
# head={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#
#
# url='https://www.sbkk88.com/html/sanmao/beiying/70603.html'
# res=requests.get(url=url,headers=head)
# a=res.content.decode('gbk')
# patt=re.compile(r'" type="text/javascript"></script><p>(.*?)<ul class="mingzhu_page">',re.S)
# items=patt.findall(a)
# for i in items:
#     items1=i.replace('<br/>','').replace('&quot;','')
#     docc = docx.Document()
#     docc.add_paragraph(u'{}'.format(i), style=None)
#
#
# docc.save('aaa.docx')




import pymysql
import xlwt
import xlrd
import xlutils
import paramiko

# a=pymysql.connect(host='192.168.0.89',port=3306,user='root',passwd='123456',charset='utf8')
# b=a.cursor()
# b.execute('use test;')

# b.execute('drop table biao2')
# with open('a.txt','r',encoding='utf-8') as f:
#
#     aaa=f.read().split('\n')
#     for i in aaa:
#         if aaa.index(i)==0:
#             i=i.split(',')
#             # b.execute('create table biao2({} char(255),{} char(255),{} char(255),{} char(255));'.format(i[0], i[1], i[2],i[3]))
#         elif i!='':
#             i = i.split(',')
#             b.execute('insert into biao2 values("{}","{}","{}","{}");'.format(i[0],i[1],i[2],i[3]))
#
# b.execute('select * from biao2;')
# c=b.fetchall()
# print(c)
# a.commit()

# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname='192.168.0.89',port=22,username='root',password='123456')
# a,b,c=ssh123.exec_command('ls -al')
# print(b.read().decode())
# ssh123.close()

# ssh123=paramiko.Transport(('192.168.0.89',22))
# ssh123.connect(username='root',password='123456')
# sftp=paramiko.SFTPClient.from_transport(ssh123)
# sftp.get()

import time

# a=input('>>>').split(',')
# b=time.strptime('{} {} {}'.format(a[0],a[1],a[2]),'%Y %m %d')
# c=time.mktime(b)
# aa=time.localtime(c)
# if int(a[0])%4==0 and int(a[0])%100!=0:
#     print('闰年，星期{}，今年是一年中的{}天'.format(aa[-3],aa[-2]))
# elif int(a[0])%100==0 and int(a[0])%400==0:
#     print('闰年，星期{}，今年是一年中的{}天'.format(aa[-3],aa[-2]))
# else:
#     print('平年，星期{}，今年是一年中的{}天'.format(aa[-3],aa[-2]))

#
# a=input('>>>').split('.')
# b=time.strptime('{} {} {}'.format(a[0],a[1],a[2]),'%Y %m %d')
# bb=time.mktime(b)
# c=time.localtime(bb)
# if int(a[0])%4==0 and int(a[0])%100!=0:
#     print('闰年，星期{}，是一年中的第{}天'.format(c[-3],c[-2]))
# elif int(a[0])%100==0 and int(a[0])%400==0:
#     print('闰年，星期{}，是一年中的第{}天'.format(c[-3], c[-2]))
# else:
#     print('平年，星期{}，是一年中的第{}天'.format(c[-3], c[-2]))


# a=input('>>>').split('.')
# b=time.strptime('{} {} {}'.format(a[0],a[1],a[2]),'%Y %m %d')
# bb=time.mktime(b)
# bb-=86400.0
# c=time.strftime('%Y %m %d',time.localtime(bb))
# print(c)


#
# import smtplib
# import email.mime.text
# import email.mime.multipart
#
# sender='meng1203@126.com'
# recver='1461633952@qq.com'
# server='smtp.126.com'
# passwd='meng123823'
#
# yj=email.mime.multipart.MIMEMultipart()
# yj['from']=sender
# yj['to']=recver
# yj['subject']='zheshi yigekongyoujian'
# text="""
# 今天是2018.10.25，天气还好吧
# 然后今天没有讲课
# 但是zhiwan了一盘狼人杀
# 还输了
# 然后很无聊
# 很无聊
# 还头晕，头疼，我要去吃饭，哒哒哒哒哒~~~~
# """
#
# text=email.mime.text.MIMEText(text)
# yj.attach(text)
#
# smtp123=smtplib.SMTP_SSL(server,465)
# smtp123.login(sender,passwd)
# smtp123.sendmail(sender,recver,yj.as_string())
# smtp123.close()



import paramiko

# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname='192.168.0.89',port=22,username='root',password='123456')
# a,b,c=ssh123.exec_command('ls -a')
# print(b.read().decode())
# ssh123.close()


# ssh123=paramiko.Transport(('192.168.0.89',22))
# ssh123.connect(username='root',password='123456')
# sftp=paramiko.SFTPClient.from_transport(ssh123)
# sftp.get()


# import xlrd
# import pymysql
# abc = pymysql.connect(host='192.168.0.57',
#                       port=3306,
#                       user='root',
#                       password='123456',charset='utf8')
# youbiao = abc.cursor()
# youbiao.execute('use test;')
# with open('b.txt','r',encoding='utf-8') as f:
#     aa=f.readline()
#     bb=aa.split(' ')
#     youbiao.execute('create table biao_6({} char(10),{} float,{} char(10));'.format(bb[0], bb[1], bb[2]))
#     aa=f.read().split('\n')
#     for j in aa:
#         bb=j.split(' ')
#         youbiao.execute('insert into biao_6 values("{}","{}","{}")'.format(bb[0],bb[1],bb[2]))
# abc.commit()


#
# import requests
# import os
#
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#
# url='http://www.iqeq.com.cn/Mensa.html'
# res=requests.get(url=url,headers=head)
# a=res.content.decode('gbk')
# patt=re.compile(r'<span><img src="img/kaishiceshi.gif" alt="开始测试" /></span>(.*?)</P></LI></OL><hr />',re.S)
# items=patt.findall(a)
# neirong=items[0]
# patt1=re.compile(r'<LI class=style1>(.*?)<IMG height',re.S)
# items1=patt1.findall(neirong)
# for i in items1:
#     i=i.replace('\r\n','').replace('<P>','').replace('</P>','').strip()
#     with open('c.txt','a',encoding='utf-8') as f:
#         f.write('{}\n'.format(i))

#
# import xlrd
# from xlutils.copy import copy
# import pymysql
# abc = pymysql.connect(host='192.168.0.74',
#                       port=3306,
#                       user='root',
#                       password='123456')
# you = abc.cursor()
# you.execute('show databases;')
# you.execute('use shuju;')
# you.execute('show tables;')
# you.execute('select * from excel;')
# aa = you.fetchall()
# you.execute('desc excel;')
# bb = you.fetchall()
# # print(bb[0][0])
# excel = xlrd.open_workbook('test2.xls')
# new_excel = copy(excel)
# sheet = new_excel.get_sheet(0)
# print(aa[0][0])
# for i in range(len(aa)):
#     # print(aa[i])
#     for j in range(len(bb)):
#         # print(i,j,aa[j][1])
#         if i == 0:
#             sheet.write(i,j,bb[j][0])
#         else:
#             sheet.write(i,0,aa[j][0])
#             sheet.write(i,1,aa[j][1])
#             sheet.write(i,2,aa[j][2])
# print(i,j,aa[j][0],aa[j][1],aa[j][2])
# new_excel.save('test2.xls')
#
# import re
# import requests
#
# 爬取植物图片
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#
#
# url='http://www.27270.com/zhiwu/list_35_1.html'
# res=requests.get(url=url,headers=head)
# a=res.content.decode('gbk')
# patt=re.compile(r'<ul class="w110 oh Zw_PicList">(.*?)<div class="hr10"></div>',re.S)
# items0=patt.findall(a)
# items=items0[0]
# patt1=re.compile(r'<li><a href="(.*?)" title="')
# items1=patt1.findall(items)
# a=0
# for i in items1:
#     for h in range(1,6):
#         j=i.replace('.html','_{}.html'.format(h))
#         res2=requests.get(url=j,headers=head)
#         a2=res2.content.decode('gbk')
#         patt2=re.compile(r'src="http://(.*?)" /></a><a href=',re.S)
#         items2=patt2.findall(a2)
#         for x in items2:
#             items2='http://'+x
#             print(items2)
#             tupian=requests.get(items2)
#             res3=tupian.content
#             with open(r'C:\Users\meng\Desktop\python\图片1\{}.jpg'.format(a),'wb') as f:
#                 f.write(res3)
#                 a+=1
#
# import re
# import requests
# import xlwt
#
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#
# url='https://search.51job.com/list/080200,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
# res=requests.get(url=url,headers=head)
# html=res.content.decode('gbk')
# patt=re.compile(r'" href="(.*?)" onmousedown="">')
# items=patt.findall(html)
# ming=[]
# xinzi=[]
# zhize=[]
# for i in items:
#     res2=requests.get(url=i,headers=head)
#     html2=res2.content.decode('gbk')
#     patt2=re.compile(r'<h1 title="(.*?)">')
#     items2=patt2.findall(html2)
#     for j in items2:
#         ming.append('{}'.format(j))
#
#     patt3=re.compile(r'</h1>(.*?)<p class="cname">',re.S)
#     items3=patt3.findall(html2)
#     for j in items3:
#         if '年</strong>' in j:
#             patt3_1 = re.compile(r'<strong>(.*?)年</strong>')
#             items3_1 = patt3_1.findall(html2)
#             for m in items3_1:
#                 mm = m.replace('</strong>','')
#                 xinzi.append('{}'.format(mm))
#         else:
#             patt3_2 = re.compile(r'<strong>(.*?)月</strong>')
#             items3_2 = patt3_2.findall(html2)
#             for m in items3_2:
#                 mm = m.replace('</strong>', '')
#                 xinzi.append('{}'.format(mm))
#
#     patt4=re.compile(r'<div class="bmsg job_msg inbox">(.*?)<div class="mt10">',re.S)
#     items4=patt4.findall(html2)
#     for k in items4:
#         k=k.replace('\r','').replace('\t','').replace('<p>','').replace('</p>','').replace('<br>','').replace('<span>','').replace('</span>','').replace('&nbsp;','').replace('\n','').strip()
#         zhize.append('{}'.format(k))
#
# neirong=list(zip(ming,xinzi,zhize))
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet1')
# sheet.write(0,0,'职称')
# sheet.write(0,1,'薪资')
# sheet.write(0,2,'要求')
# for p,n in enumerate(neirong):
#     sheet.write(p+1,0,'{}'.format(n[0]))
#     sheet.write(p + 1, 1, '{}'.format(n[1]))
#     sheet.write(p + 1, 2, '{}'.format(n[2]))
# f.save('ceshi.xls')
# #
# import os
#
# os.chdir(r'D:\360安全浏览器下载\软件测试实践\ATMSimulationSystem\bin\Debug')
# a=os.popen(r'D:\360安全浏览器下载\软件测试实践\ATMSimulationSystem\bin\Debug\ATM自动取款机模拟系统.exe')

import re
import requests
import time
#
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# url='http://manhua.fzdm.com/17/'
# res=requests.get(url=url,headers=head)
# html=res.content.decode('utf-8')
# patt=re.compile(r'<li class="pure-u-1-2 pure-u-lg-1-4"><a href="(.*?)" title="')
# items=patt.findall(html)
# items=items[80:81]
# aaa=0
# for i in items:
#     for j in range(100):
#         url2='http://manhua.fzdm.com/17/'+i+'index_{}.html'.format(j)
#         res2 = requests.get(url=url2, headers=head)
#         html2 = res2.content.decode('utf-8')
#         if html2=='404':
#             break
#         else:
#             patt2=re.compile(r'var mhurl="(.*?)"')
#             items2=patt2.findall(html2)
#             h='http://p0.xiaoshidi.net/'+items2[0]
#             tupian=requests.get(h)
#             res3=tupian.content
#             with open(r'E:\30\{}.jpg'.format(aaa),'wb') as f:
#                 f.write(res3)
#                 aaa+=1
#             time.sleep(3)

#
# import re
# import pymysql
# import xlwt
# import xlrd
# import xlutils
#
# a=pymysql.connect(host='192.168.0.60',port=3306,user='root',password='123456',charset='utf8')
# b=a.cursor()
# b.execute('use test;')
# b.execute('drop biao1;')
# # with open('b.txt','r',encoding='utf-8') as f:
# #     tou=f.readline().split(',')
# #     print(tou)
# #     b.execute('create table biao1({} char(20),{} char(30),{} char(30));'.format(tou[0][0],tou[1][0],tou[2][0]))
# #     neirong=f.read()
# #     hang=len(neirong)
# #     for i in range(hang):
# #         b.execute('insert into biao1 values("{}","{}","{}");'.format(neirong[i][0],neirong[i][1],neirong[i][2]))
#
# b.execute('select * from biao1;')
# c=b.fetchall()
# print(c)
#
# a.commit()



















#
# import re
# import requests
#
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#
# url='http://www.doutula.com/article/list/?page=1'
# res=requests.get(url=url,headers=head)
# html=res.content.decode('UTF-8')
# patt=re.compile(r'</div> <div class="col-sm-9">(.*?)<div class="text-center">',re.S)
# items=patt.findall(html)
# items=items[0]
# patt2=re.compile(r'<a href="(.*?)" class="list-group-item random_list',re.S)
# items2=patt2.findall(items)
# tt=0
# for i in items2:
#     res3 = requests.get(url=i, headers=head)
#     html3 = res3.content.decode('UTF-8')
#     patt3=re.compile(r'onerror="(.*?)">')
#     items3=patt3.findall(html3)
#     for j in items3:
#         j=j.replace('this.src=','').replace("'",'')
#         tupian=requests.get(url=j)
#         res4=tupian.content
#         if 'jpg' in j:
#             with open(r'C:\Users\meng\Desktop\python\图片4\{}.jpg'.format(tt),'wb') as f:
#                 f.write(res4)
#                 tt+=1
#         elif 'gif' in j:
#             with open(r'C:\Users\meng\Desktop\python\图片4\{}.gif'.format(tt),'wb') as f:
#                 f.write(res4)
#                 tt+=1

import socket
# 基于tcp的客户端
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.0.61',3300))
# s.send('nihao'.encode('utf-8'))
# msg=s.recv(1024)
# print(msg.decode('utf-8'))

# 基于udp的客户端
# c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# c.sendto('good morning'.encode('utf-8'),('192.168.0.61',3300))
# msg=c.recv(1024)
# print(msg.decode('utf-8'))

# c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# c.connect(('192.168.0.61',3001))
# c.send('nihao'.encode('utf-8'))
# msg=c.recv(1024)
# print(msg.decode('utf-8'))

# c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # c.sendto('你好'.encode('utf-8'),('192.168.0.61',3300))
# # msg=c.recv(1024)
# # print(msg.decode('utf-8'))


# c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# c.sendto('nihao'.encode('utf-8'),('192.168.0.36',3001))
# msg=c.recv(1024)
# print(msg.decode('utf-8'))


# c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# c.connect(('192.168.0.61',3300))
# c.send('nihao!!!'.encode('utf-8'))
# msg=c.recv(1024)
# print(msg.decode('utf-8'))

#
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.0.36',3300))
# s.send('nihao'.encode('utf-8'))
# msg=s.recv(1024)
# print(msg.decode('utf-8'))


# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.sendto('你好呀'.encode('utf-8'),('192.168.0.61',3000))
# msg=s.recv(1024)
# print(msg.decode('utf-8'))

# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.0.36',3333))
# s.send('你好'.encode('utf-8'))
# msg=s.recv(1024)
# print(msg.decode('utf-8'))


# c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# c.connect(('192.168.0.61',3000))
# c.send('nihao'.encode('utf-8'))
# msg=c.recv(1024)
# print(msg.decode('utf-8'))

# c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# c.sendto('nihao'.encode('utf-8'),('192.168.0.61',3300))
# msg=c.recv(1024)
# print(msg.decode('utf-8'))













