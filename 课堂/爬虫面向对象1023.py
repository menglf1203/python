# /usr/bin/env python
# -*- coding:utf-8 -*-


# import requests
# import re


# 面向过程的爬图片
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/70.0.3538.67 Safari/537.36'}
# xx=0
# url='http://www.doutula.com/article/list/?page=1'
# res=requests.get(url=url,headers=head)
# html=res.content.decode('UTF-8')
# bianyi=re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}')
# chazhao=bianyi.findall(html)
# for i in chazhao:
#     res=requests.get(url=i,headers=head)
#     html1=res.content.decode('UTF-8')
#     patt1=re.compile(r'this.src=(.*?)">')
#     items1=patt1.findall(html1)
#     for j in items1:
#         j=j.replace("'",'').strip()
#         tupian=requests.get(j)
#         res1=tupian.content
#         if 'jpg' in j:
#             with open(r'C:\Users\meng\Desktop\python\richang\tupian\{}.jpg'.format(xx),'wb') as f:
#                 f.write(res1)
#         elif 'gif' in j:
#             with open(r'C:\Users\meng\Desktop\python\richang\tupian\{}.gif'.format(xx),'wb') as f:
#                 f.write(res1)
#         xx+=1




# 面向对象的爬图片的代码
# class Patupian():
#
#     def zhu(self):
#         url='http://www.doutula.com/article/list/?page=1'
#         res=requests.get(url=url,headers=head)
#         a=res.content.decode('UTF-8')
#         patt=re.compile('<a href="http://www.doutula.com/(.*?)" class="list-group-item random_list">')
#         items=patt.findall(a)
#         return items
#
#     def er(self,items):
#         tupiana=[]
#         for i in items:
#             i='http://www.doutula.com/'+i
#             res1=requests.get(url=i,headers=head)
#             a1 =res1.content.decode('UTF-8')
#             patt1=re.compile('onerror="this.src=(.*?)">')
#             items1=patt1.findall(a1)
#             for j in items1:
#                 j=j.replace("'",'').strip()
#                 tupiana.append(j)
#         return tupiana
#
#     def save(self,url):
#         tupian=requests.get(url)
#         res2=tupian.content
#         if 'jpg' in url:
#             with open(r'C:\Users\meng\Desktop\python\richang\tupian\{}.jpg'.format(url[-25:-4]),'wb') as f:
#                 f.write(res2)
#
#         elif 'gif' in url:
#             with open(r'C:\Users\meng\Desktop\python\richang\tupian\{}.gif'.format(url[-25:-4]),'wb') as f:
#                 f.write(res2)
#
#
#
#
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                           'AppleWebKit/537.36 (KHTML, like Gecko) '
#                           'Chrome/70.0.3538.67 Safari/537.36'}
# patupian=Patupian()
# aa=patupian.zhu()
# bb = patupian.er(aa)
# for i in bb:
#     patupian.save(i)


#
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/70.0.3538.67 Safari/537.36'}
#
# url='https://www.qiushibaike.com/imgrank/page/1/'
# res=requests.get(url=url,headers=head)        # 发送请求
# a=res.content.decode('utf-8')    # 以字节码的方式读取
# patt=re.compile('<img src="//pic.qiushibaike.com/system/(.*?).jpg" alt="')   # 过滤的条件
# items=patt.findall(a)            # 过滤出符合条件的
# aaa=0
# for j in items:
#     i='https://pic.qiushibaike.com/system/'+j+'.jpg'
#     tupian=requests.get(i)
#     res1=tupian.content
#     with open(r'C:\Users\meng\Desktop\python\图片1\{}.jpg'.format(aaa),'wb') as f:
#         f.write(res1)
#         aaa+=1

#
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/70.0.3538.67 Safari/537.36'}
#
# url='http://www.budejie.com/1'
# res=requests.get(url=url,headers=head)
# a=res.content.decode('UTF-8')
# patt=re.compile('data-original="http://mpic.spriteapp.cn/(.*?)" alt="')
# items=patt.findall(a)
# aaa=0
# for i in items:
#     if " title=" in i:
#         i='http://mpic.spriteapp.cn/'+i
#         i=i.split('"')[0]
#         tupian=requests.get(url=i)
#         res1=tupian.content
#         if 'gif' in i:
#             with open(r'C:\Users\meng\Desktop\python\图片1\{}.gif'.format(aaa),'wb') as f:
#                 f.write(res1)
#                 aaa+=1
#         elif 'jpg' in i:
#             with open(r'C:\Users\meng\Desktop\python\图片1\{}.jpg'.format(aaa), 'wb') as f:
#                 f.write(res1)
#                 aaa += 1

#
# import re
# import requests
# import time
#
# import pymysql
# import xlwt
# import xlrd
# import xlutils
#
# a=pymysql.connect(host='192.168.0.42',port=3306,user='root',password='123456',charset='utf8')
# b=a.cursor()
# b.execute('use test;')
# b.execute('desc biao;')
# c=b.fetchall()
#
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet1')
# for i in range(3):
#     sheet.write(0,i,'{}'.format(c[i][0]))
#
# b.execute('select * from biao;')
# c2=b.fetchall()
# chang=len(c2)
#
# for j in range(1,chang+1):
#     sheet.write(j, 0, '{}'.format(c2[j-1][0]))
#     sheet.write(j, 1, '{}'.format(c2[j-1][1]))
#     sheet.write(j, 2, '{}'.format(c2[j-1][2]))
#
# f.save('test.xls')



import paramiko
# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh123.connect(hostname='192.168.0.59',port=22,username='root',password='123456')
# a,b,c=ssh123.exec_command('ls -al')
# print(b.read().decode())
# ssh123.close()

# ssh123=paramiko.Transport(('192.168.0.59',22))
# ssh123.connect(username='root',password='123456')
# sftp123=paramiko.SFTPClient.from_transport(ssh123)


# import os
# for i in range(10):
#     os.mkdir('{}'.format(i))
#     for j in range(10):
#         with open(r'C:\Users\meng\Desktop\python\richang\{}.txt'.format(j),'w') as f:
#             f.write('123')
#         os.remove('{}.txt'.format(j))
#     os.rmdir('{}'.format(i))
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
# yj['subject']='lallala试试试试，在不在线'
# text="""
# 2018年10月30日，微风，星期二
# 日报已发送
# 回去吃大闸蟹
# 哈哈哈
# 气死你
# 就是你
# 别看了
# 就是你
#
# """
# text=email.mime.text.MIMEText(text)
# yj.attach(text)
#
# smtp123=smtplib.SMTP_SSL(server,465)
# smtp123.login(sender,passwd)
# smtp123.sendmail(sender,recver,yj.as_string())
# smtp123.close()

# #
# import requests
# import os
#
#
# # head={'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# a=1
# for i in range(803,864):
#     url='https://www.88dush.com/xiaoshuo/47/47361/17519{}.html'.format(i)
#     res=requests.get(url=url)
#     html=res.content.decode('gbk')
#     patt=re.compile(r'<div class="yd_text2">(.*?)<div class="yd_ad1">',re.S)
#     items=patt.findall(html)
#     for j in items:
#         neirong=j.replace('&nbsp;','').replace('<br />','').replace('</div>','').strip()
#         with open('feichai2.txt','a') as f:
#             f.write('{}'.format(neirong))
#             a+=1
#     print(a)
# import xlwt
#
# url='https://www.xzw.com/astro/'
# res=requests.get(url=url)
# html=res.content.decode('utf-8')
# patt=re.compile(r'<div class="a-nav">(.*?)<em class="todayastro">')
# items=patt.findall(html)
# items=items[0]
# patt2=re.compile(r'" href="(.*?)" hidefocus="')
# items2=patt2.findall(items)
# for i in items2:
#     i='https://www.xzw.com'+i
#     res3=requests.get(url=i)
#     html3 = res3.content.decode('utf-8')
#     patt3 = re.compile(r'<strong class="f_yh">(.*?)<div class="xz_key">')
#     items3 = patt3.findall(html3)
#     for j in items3:
#         h=j.replace('</strong>','').replace('<small>',' ').replace('<em class="cl_',' ').replace('</em></h1><ul><li><label>',' ').replace('">','')
#         h=h.replace('</label>','').replace('</li><li><label>',' ').replace('</li></ul></dt><dd><p>',' ').replace('</p>','').replace('</small>','')
#         with open('a.txt','a',encoding='utf-8') as f:
#             f.write('{}\n'.format(h))



# import re
# import requests
# import xlwt
# import xlrd
# import xlutils
#
#
# a=input('>>>')
# b=a.split(',')
# b[0]=int(b[0])
# b[1]=int(b[1])
# b[2]=int(b[2])
# b.sort()
# print(b)



# a=[2,5,8,9]
# b=int(input('>>>'))
# for i in a:
#     c = a.index(i)
#     if b<i:
#         a.insert(c,b)
#         break
# if b>=a[-1]:
#     a.append(b)
# print(a)

#
# a=[1,2,3,5,6,9]
# b=int(input('请输入一个数'))
# for i,j in enumerate(a):
#     if b<a[i]:
#         a.insert(i,b)
#         break
# print(a)
