# /usr/bin/env python
# -*- coding:utf-8 -*-

# 爬虫 requests  第三方库
# 正则表达式：匹配文件中的内容

# 模仿浏览器的模块 urllib urllib3 requests
# 匹配内容的模块  re正则表达式，bs4和正则表达式相同，xpath

# 爬虫分为两类：聚焦爬虫和搜索爬虫

# 面向对象的爬虫代码

# 第一步：分析网址的变化
# 第二步：分析html文件，过滤并下载想要的资源（找到你想要的资源，然后用正则表达式过滤出来）
# 第三步：保存  保存的权限和格式
import requests
import re

#
# class Qiushi(object):
#
#     def qingqiu(self,page):
#         url='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         response=requests.get(url=url)   # 发送请求 response可改变
#         # 读取结果的方式: 1.以字符串的方式读取 2.以字节码的方式读取
#         # print(response.text)      # 以字符串的方式读取
#         html=response.content.decode('utf-8')   # 以字节码的方式读取
#         return html
#
#     def guolv(self,aaa):
#         shuju=[]
#         patt = re.compile('<div class="content">(.*?)</div>',re.S)
#         items = patt.findall(aaa)
#         for i in items:
#             sj=i.replace('<span>','').replace('</span>','').replace('\n','').replace('<br/>','').strip()
#             shuju.append(sj)
#         return shuju
#
#     def save(self,shuju):
#         with open('a.txt','a',encoding='utf-8') as f:
#             for i in shuju:
#                 f.write(i+'\n')
#
#
#
#
# qiushi=Qiushi()
# for i in range(1,14):
#     jieguo=qiushi.qingqiu(i)     # 查看网页源代码（内容为1页的）
#     shuju=qiushi.guolv(jieguo)
#     qiushi.save(shuju)
# print('over')



# 正则表达式 re  只能匹配字符串

# a="""qwe12
# 3qwe456qwe789qwe"""
# # 将要匹配的正则编译
# b=re.compile('qwe(.*?)qwe',re.S)   # re.S 让.可以匹配包括换行符在内的所有字符，结果是一个列表
# # 到目的字符串中去查找
# c=b.findall(a)
# print(c)

# 贪婪模式：尽可能多的去匹配最后的字符串   带有*是贪婪     按照要求从头到尾一下子全部显示
# 非贪婪模式：尽可能少的去匹配最后的字符串  带有？是非贪婪  按照要求一段一段去匹配的
# 带有？又带有*的    以？为主     是非贪婪模式

# 'qwe(.*?)qwe' 带括号的是不包括qwe的
# 'qwe.*?qwe' 不带括号的是包括qwe的

# . 匹配任意一个字符，但是匹配不了换行符


# 面向过程
# import requests
# import re
# import xlwt
#
# shuju=[]
# f=xlwt.Workbook(encoding='utf-8')
# for i in range(1,14):
#     url='https://www.qiushibaike.com/text/page/{}/'.format(i)
#     response=requests.get(url=url)
#     a=response.text
#     bianyi=re.compile('<div class="content">(.*?)</div>',re.S)
#     sheet = f.add_sheet('sheet{}'.format(i), cell_overwrite_ok=True)
#     chazhao=bianyi.findall(a)
#     aa=0
#     for j in chazhao:
#         j=j.replace('<span>','').replace('</span>','').replace('\n','').replace('<br/>','').strip()
#         sheet.write(aa, 0, j)
#         aa+=1
#
#
# f.save('test.xls')




