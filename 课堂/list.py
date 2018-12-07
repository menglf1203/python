# /usr/bin/env python
# -*- coding:utf-8 -*-

#列表list

# a=[1,'dfgh',3,4,5]
# print(a[1])   #支持索引
# print(a[:])   #中括号里加：是显示全部的
# print(a[-2])  #也支持反索引
# print(a[2:9]) #支持切片
# print(a[:2])

# a=[123,'sad',213,['fgh','ytr',87],5,56]
# #列表中有：数字，字符串，列表，元组等
# print(a[1][0])  #支持嵌套索引
# print(a[1][2])  #前提是提取的元素是支持索引(也就是字符串)
# print(a[1][-1]) #字符串中的元素使用和字符串索引一样
# print(a[3][0][0]) #也可以多层数据嵌套
# print(a[3][0])  #多层数据


#列表中的内置函数
# a=[12,'asdf',34]
# b=a[1].upper()   #根据数据类型可以这样写
# print(b)
#
# a=[12,'asdf',34,['uyt',2,5]]
# b=[87,'iuyt','jhg']
# a[3].append([87,2,1])       #将括号中的元素添加到表中，注意：只能添加1个
# print(a)           #默认添加到最后
# a.append(b)        #也可以定义一个列表、字符串等添加进去
# print(a)

# a=[12,'asdf',34,['uyt',2,5]]
# a.insert(1,'abc')     #第一个参数是下标位置，第二个参数是添加的元素
# a.insert(0,[12,4,5])  #添加元素可以是列表、字符串、数字等
# print(a)

# a=[12,'asdf',34,['uyt',2,5]]
# #a.remove(12)     #只能删除某个元素，括号里直接写元素
# a.pop(1)         #删除下标位置删除的，括号里写下标号
# print(a)

# a=[12,'asdf',34,['uyt',2,5]]
# b=a.index(12)  #获取某元素的下标值(如果有重复的，只会显示第一个的下标值)
# print(b)
# print(a[-1].index(2))   #也可以直接写在print括号中
# a='kju1h,ygt'
# b=len(a)
# print(b)
#
# a=[12,34,'asdf',34,[34,34,34]]
# b=a.count(34)      #统计某元素在列表中的个数
# c=len(a)           #统计某数据类型有多少个元素
#                    #len不能统计整数、浮点数
# print(b)
# print(a[4].count(34))
# print(c)
# d='kjuytrertyui'
# print(len(d))


# a=[12,34,'asdf',34,[34,34,34]]
# a.reverse()         #反转列表
# print(a)


# a=['asd','Zsdf','sdfg','qwert']
# a.sort()      #排序，默认是升序
# print(a)      #字符串是根据首字母在ASCII中的顺序排序，先大写后小写
# b=[123,4,56,87,9]
# b.sort()     #数字排序，正序排列
# print(b)
# b.sort(reverse=True)  #先排序在反转
# print(b)     #倒序显示

# import copy
# i=[12,4321,24]
# a=[i,1234,56543]
# b=a.copy()  #复制列表  浅复制
# # a.clear()   #清空
# # print(a)
# # print(b)
# a.append(100)
# a[0].append(100)
# d=copy.deepcopy(a)
# print(d)
# print(a)



# a=[1234,56543]
# b=[12,4321,24]
# a.extend(b)     #将b的元素更新到a列表中
# # b.extend(a)
# print(a)
# print(b)


# b={12,453,45}
# a={213,'ds','afsd'}
#
# print(a|b)
# print(a&b)
# print(a-b)

# a=[123,234,7,56,7,87645,324]
# b=set(a)
# c=list(b)
# c.sort()
# print(c)
# c.sort(reverse=True)
# print(c)