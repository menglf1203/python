# /usr/bin/env python
# -*- coding:utf-8 -*-
#
# import smtplib                  # 发送邮件的协议
# import email.mime.text          # 处理发送的内容
# import email.mime.multipart     # 处理邮件的表头
#
# # 发送邮件
#
# sender='meng1203@126.com'      # 发送者
# recver=['meng1203@126.com',
#         '1305061941@qq.com',
#         '1461633952@qq.com']    # 接收者，如果发送多个，可以用列表装多个['1305061941@qq.com','1461633952@qq.com']
#
# server='smtp.126.com'          # 服务器地址smtp.163.com/smtp.126.com
# passwd='meng123823'            # 授权码
#
# # 创建一个空邮件
# kyj=email.mime.multipart.MIMEMultipart()
# # 发件人
# kyj['from']=sender    # sender 也可以直接写邮箱
# # 收件人
# kyj['to']=','.join(recver)      # ','.join(recver)  /  recver
# # 主题
# kyj['subject']='gogogo小黄鸭'
# # 正文
# text="""
# lalallalalalalallalalalalal！！！
# 啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦！！！
# """
# # 处理文本信息
# text=email.mime.text.MIMEText(text)
# # 将处理的文本信息添加到邮件里
# kyj.attach(text)
#
# # 添加附件；处理附件：以二进制的方式读取文件,以字节流的方式发送，定义发送文件名
# # 可以添加多个附件，定义多个附件名就可以
# att1=email.mime.text.MIMEText(open('test.xls','rb').read(),'base64','utf-8')
# att1['Content-Type']='application/octet-stream'
# att1['Content-Disposition']='attachment;filename="666.xls"'
# kyj.attach(att1)
#
#
#
# # 定义服务器和端口
# smtp123=smtplib.SMTP_SSL(server,465)
# # 登录服务器
# smtp123.login(sender,passwd)
# # 发送邮件
# smtp123.sendmail(sender,recver,kyj.as_string())
# # 断开连接
# smtp123.close()


##################################################################################



# 时间模块

import time
import calendar
# 时间戳  代表从公元1970年1月1日到现在经过的秒数
# print(time.time())

# 本地时间  元组  默认显示当前时间
# 参数 填时间戳的（秒数）   例：time.localtime(1540025624)
# print(time.localtime(time.time()))  # 可以通过索引显示
# print(time.asctime(time.localtime(time.time())))

# 显示日历
# print(calendar.month(2018,10))


# 格式化成现代化时间   年  月  日   时间  时间 星期
# print(time.strftime('%Y %m %d %H-%M-%S %X %w',time.localtime()))

# 将现代化时间格式化成元组  注意strftime和strptime的区别
# a=time.strptime('1997 01 11 00:00:11','%Y %m %d %X')
# print(time.mktime(a))

# 将元组的时间转化为时间戳
# 时间戳必须是有9个元素的元组，是按年月日来算的，星期和夏令时等无所谓但是必须有
# b=(2018,10,20,12,12,12,12,12,0)
# print(time.mktime(a))


# 休眠
# time.sleep(5)
# print('over')


# 输入一个现在化日期（年月日），输出：今年是否为闰年，今天星期几，今天是一年中的第几天
#
# a=input('>>>')
# a=a.split(',')
# aa=time.strptime('{} {} {}'.format(a[0],a[1],a[2]),'%Y %m %d')
# if int(a[0])%100==0:
#     if int(a[0])%400==0:
#         print('闰年,星期{},是一年中的第{}天'.format(aa[-3]+1,aa[-2]))
#     else:
#         print('平年,星期{},是一年中的第{}天'.format(aa[-3]+1,aa[-2]))
# elif int(a[0])%100!=0 and int(a[0])%4==0:
#     print('闰年,星期{},是一年中的第{}天'.format(aa[-3]+1,aa[-2]))
# else:
#     print('平年,星期{},是一年中的第{}天'.format(aa[-3]+1,aa[-2]))



# 输入日期(年月日)，输出日期的前一天
# 计算平年闰年的二月份前一天时间不好算，可以按时间戳去计算一天的秒数(时间戳)是86400
# a=input('>>>')
# a=a.split(',')
# aa=time.strptime('{} {} {}'.format(a[0],a[1],a[2]),'%Y %m %d')
# b=time.mktime(aa)
# b-=86400.0
# print(time.strftime('%Y %m %d',time.localtime(b)))






