#/usr/bin/env python
# -*- coding:utf-8 -*-


#调用函数的方法：变量名.函数名()
#属于字符串的内置函数
# a='abcdefgh'
# b=a.upper() # 将字符串中所有的小写变成大写
# print(b)


# a='jh234gtres中国DFGHJKL'
# b=a.upper()  #将字符串中的所有大写变成小写
# c=a.lower()  #将字符串中的所有小写变成大写
# d=a.capitalize() #将字符串中的首字母变大写
# e=a.swapcase()  #将字符串中的大写变小写，小写变大写
# print(b)
# print(c)
# print(d)
# print(e)


# aa=' asdfghj '
# f=aa.lstrip() #去除字符串左边的空格
# g=aa.rstrip() #去除字符串左边的空格
# h=aa.strip() #去除字符串两边的空格
# print(f)
# print(g)
# print(h)


# a='aasdfe,GHJKL,2345a'
# b=a.replace('asd','啊') #替换
# c=a.replace(',','')     #去掉逗号
# d=a.replace(',','  ')   #将逗号替换为两个空格
# f=a.replace('a','B',3)
#  #将前一个字符替换为第二个字符，后面的数字为几就是替换几次
# print(b,c,d)
# print(f)


# a='ertyuiolkjhgfd'
# b=a.startswith('ery')   #判断字符串是否以括号中的元素开头
# c=a.endswith('d')       #判断字符串是否以括号中的元素结尾
# print(b,c)

# #格式化字符串  format  %
# aa='hello{},我今年{}岁'           #占位符{字符、数字、下划线}
# b=aa.format('小红',3)
# #format(格式化字符串)是用来填充占位符的
# a='hello{name},我今年{age}岁'     #占位符{字符、数字、下划线}
# c=a.format(name='小米',age='18')
# print(b)
# print(c)

# aa='hello%s,我今年%d岁'    #占位符%
# b=aa%('小红',5)           #决定数据类型
# print(b)
#
# a='hello%s,我今年%.2f岁' #占位符 .数字%指的是精确小数点多少位的
# c=a%('小红',5.8)         #决定数据类型
# print(c)

# a='asd'
# b='-'.join(a)
# #以指定字符串为分隔符
# # 将a中所有的元素连接起来形成一个新的字符串
# print(b)


# a='1,2,3'
# #以指定字符串为分隔符，将a中的元素分割成一个列表
# b=a.split(',')
# print(b)
# print(type(b))

# a=[123,'weadsf','sad',['afs',2134]]
# b=a.count(123)
# print(b)





