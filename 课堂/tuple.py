# /usr/bin/env python
# -*- coding:utf-8 -*-

# a=('435','sad',132,'dsf',132)
# f=(9,)    #如果元组中只有一个元素，在最后要加上逗号
# g=(9)
# print(type(f))     #元组tuple
# print(type(g))
# b=a.count(132)
# c=a.index(132)
# print(b,c)


#dict字典

# a={'name':'小米','age':18,'sex':'女'}
# print(type(a))
# #添加
# a['sec']=234
# print(a)
# #删除key所在的键值对
# a.pop('sex')
# print(a)
# #默认删除的最后一个
# a.popitem()
# print(a)

# a={'name':'小米','age':18,'sex':'女'}
# #获取所有的key键,values值，item键值对
# b=a.keys()
# c=a.values()
# d=a.items()
# print(b)
# print(c)
# print(d)

# #将b更新到a中
# a={'name':'小米','age':[45,23,2],'sex':'女'}
# b={'add':76}
# a.update(b)        #将字典b中的元素更新到a中
# a['name']='小明'    #修改键值
# print(a)
# print(a['age'][2])   #支持通过key取值的



#set(集合)

# a={12,34,5,65,12,234,56,7654,3}
# print(type(a))
# print(a)   #集合里的数据是不重复的，会自动删除一个
#            #不重复的；无序的；不支持索引
# a.add(10)  #添加,不能添加元素是列表
# print(a)



# a={12,34,5,65,12,234,56,7654,3}
# a.pop()    #默认删除最后一个，也可以说随机删除一个
# a.remove(12)  #删除括号中指定的元素
# print(a)


# a={12,34,5,65,12}
# b={13}
# a.update(b)  #将集合b中的所有元素更新到a中
# print(a)

#并集  |
# a={12,34,5,65,12}
# b={13,12}
# print(a|b)

#交集  &
# a={12,34,5,65,12}
# b={13,12}
# print(a&b)

#差集
# a={12,34,5,65,12}
# b={13,12}
# print(a-b)


# a=input(557845)   #从键盘上读值是字符串
# a=int(a)  #从键盘上读值只能是数字
# print(type(a))



