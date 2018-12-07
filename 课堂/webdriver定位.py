# /usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep


# dr=webdriver.Firefox()          # 打开火狐浏览器Firefox() 谷歌浏览器Chrome()
# dr.get('http://www.baidu.com')  # 请求的网址
# sleep(2)    # 等待时间
#
# # 获取网站的标题（title），断言某网站的标题是否符合结果
# title=dr.title
# print(title)
# # 获取网站的网址,判断获取到的网址和要请求的是不是同一个网址
# url=dr.current_url
# print(url)

# 保证所有的测试用例在同一环境下测试
# 设置浏览器的大小 (宽,高)不能设置超过屏幕的大小
# dr.set_window_size(400,400)
# # 设置浏览器打开的位置 (x,y轴)
# dr.set_window_position(500,500)
#
# dr.maximize_window()  # 浏览器最大化
# dr.minimize_window()  # 浏览器最小化


# 浏览器的前进和后退
# dr.get('https://www.jd.com')
# dr.back()    # 后退
# sleep(3)
# dr.forward() # 前进
#
#
# sleep(2)
# dr.quit()   # 关闭浏览器
####################################################################
# 对象定位    webdriver模拟人的行为
#
# #通过id属性定位(id属性值是唯一的,才可以定位)
# dr.find_element_by_id('kw').send_keys('python')     # send_keys    找到id=kw的位置，输入(括号中写属性的值)
# dr.find_element_by_id('su').click()                 # click    点击id=su百度一下

#class name属性
#
# dr.find_element_by_class_name('s_ipt').send_keys('python')
# # dr.find_element_by_class_name('btn self-btn bg s_btn btnhover').click()   # 报错可能是不能用class定位
# dr.find_element_by_id('su').click()
#
# #name属性
# dr.find_element_by_name('wd').send_keys('python')
# dr.find_element_by_id('su').click()
#
# # 20181123
# # link text  通过文本来定位  保证定位元素的唯一性
# dr.find_element_by_link_text('查看更多职位').click()
#
# # partial link text 通过局部的文本来进行定位
# dr.find_element_by_partial_link_text('企').click()
#
# # tag name 通过标签的名称去定位,通常用于多个元素的定位
# dr.find_element_by_tag_name('').click()
#
# # xpath 通过路径来定位  路径标记语言
# dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/dl/dd[1]/a').click()    # 绝对路径
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()   # 相对路径
#
# # css selector  通过层叠样式表的选择
# dr.find_element_by_css_selector('body > div.main > div > div.content > dl > dd:nth-child(2) > a').click()

################################################      高级定位
# 定位

#
# dr=webdriver.Firefox()
# dr.get('http://www.moore.ren/')
# sleep(3)
# print(dr.title)
# 3.1定位多个class属性的值为menu-box的元素,定位一组对象的数据类型是列表
# wd=dr.find_elements_by_class_name('menu-box')
# print(len(wd))
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(3)

# 3.2在一个menus中找menu-box
# wd=dr.find_element_by_tag_name('menus').find_elements_by_class_name('menu-box')


# 3.3层级定位获取元素中某个属性的值
# wd=dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a')
# print(wd.get_attribute('text'))    # 获取元素某个属性的值

# wd=dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').text
# print(wd)    # 获取元素的文本信息
# sleep(1)
#
# dr.quit()

# 3.4处理窗口，把每个窗口标号(句柄)
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# sleep(2)
# # print(dr.current_window_handle)   # 获取当前服务器的句柄，即使是我进入了新的窗口，但是没有使用切换的命令，那么还是原来网页的句柄
# # print(dr.window_handles)   # 获取所有窗口的句柄
# wd=dr.window_handles
# print(wd)
# # dr.switch_to_window(wd[-1])  # 和下方那个是一样的，都可以使用，下方是新版本的
# dr.switch_to.window(wd[-1])
# print(dr.title)
# sleep(3)
# dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('meng1203@126.com')
# dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('meng199612@')
# sleep(2)
# dr.find_element_by_xpath('#userForm > input.base-btn.regBtn').click()


# 3.5处理框架
# dr=webdriver.Firefox()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# # dr.switch_to_frame('login_frame')   # 切换到内嵌框架中,只能根据id、name或者定位到框架来切换
# wd=dr.find_element_by_xpath('//*[@id="login_frame"]')   # 定位到框架
# dr.switch_to_frame(wd)
#
# dr.find_element_by_id('img_out_1461633952').click()
#
# dr.switch_to.default_content()   # 退出到原始的页面
# dr.switch_to.parent_frame()      # 切换到上一层框架



####################################################     案例


# QQ空间跳过验证码1
#
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# import os
# dr=webdriver.Firefox()
# dr.get('https://user.qzone.qq.com/')
# dr.maximize_window()
# #dr.switch_to_default_content()   #跳出窗口
# web = dr.find_element_by_id('login_frame')   #输入定位信息
# #dr.switch_to_frame('f1')
# sleep(3)
# dr.switch_to.frame(web)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(1)
# dr.find_element_by_id('u').send_keys('3352455136')
# sleep(2)
# dr.find_element_by_id('p').send_keys('wazsby520')
# sleep(2)
# dr.find_element_by_css_selector('#login_button').click()
# sleep(2)
# web = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
# dr.switch_to.frame(web)
# web = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# ac = ActionChains(dr)
# ac.move_to_element(web)
# ac.drag_and_drop_by_offset(web,185,0)
# ac.perform()
# sleep(30)
# dr.quit()

# QQ空间2

# dr=webdriver.Firefox()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.switch_to_frame('login_frame')
#
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(3)
# dr.find_element_by_class_name('inputstyle').send_keys('123456')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('123456')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# ww=dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
# dr.switch_to_frame(ww)
#
# start=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# sleep(2)
# ActionChains(dr).drag_and_drop_by_offset(start,192,0).perform()  # 模拟用户操作




# 携程，酒店级别，国内酒店，酒店级别或者房间数，显示，中间间隔几秒
#
# dr=webdriver.Firefox()
# dr.get('http://www.ctrip.com/')
# sleep(2)
# # wd=dr.find_element_by_id('J_roomCountList')
# # sleep(2)
# dd=dr.find_elements_by_tag_name('option')
# sleep(3)
# for i in dd:
#     dr.find_element_by_xpath('//*[@id="J_roomCountList"]').click()
#     sleep(4)
#     i.click()
#     sleep(1)




# 防火墙登录
# dr=webdriver.Firefox()
# dr.get('https://192.168.0.254:8889/')
# sleep(2)
# dr.find_element_by_name('txt_name').clear()
# sleep(1)
# dr.find_element_by_name('txt_name').send_keys('administrator')
# sleep(1)
# dr.find_element_by_name('txt_password').send_keys('Bane@7766')
# sleep(2)
# wd=dr.find_elements_by_class_name('nobody')
# yzm=[]
# for i in wd:
#     aa=i.get_attribute('src')
#     patt = re.compile('/imgs/(.).gif')
#     items=patt.findall(aa)
#     yzm.append(items)
#
# dr.find_element_by_id('input1').send_keys('{}{}{}{}'.format(yzm[0][0],yzm[1][0],yzm[2][0],yzm[3][0]))
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
#
# sleep(5)
# dr.quit()



# 防火墙新建内容
#
#
# dr=webdriver.Chrome()
# dr.get('http://192.168.0.254/')
# sleep(2)
# dr.find_element_by_name('txt_name').clear()
# sleep(1)
# dr.find_element_by_name('txt_name').send_keys('administrator')
# sleep(2)
# dr.find_element_by_name('txt_password').clear()
# sleep(1)
# dr.find_element_by_name('txt_password').send_keys('Bane@7766')
# sleep(2)
# wd=dr.find_element_by_id('checkinfo').find_elements_by_tag_name('img')
# yzm=[]
# for i in wd:
#     aa=i.get_attribute('src')[-5]
#     yzm.append(aa)
# sleep(1)
# dr.find_element_by_class_name('login_yzm').send_keys('{}{}{}{}'.format(yzm[0],yzm[1],yzm[2],yzm[3]))
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# sleep(3)
# wd=dr.switch_to_alert()        # 弹出框
# sleep(2)
# wd.accept()
# sleep(2)
# dr.switch_to_frame('left')            # 进入框架
# sleep(2)
# dr.find_element_by_id('04').click()   # 点击防火墙
# sleep(2)
# dr.find_element_by_id('041').click()  # 点击策略
# sleep(2)
# dr.switch_to_default_content()
# sleep(2)
# dr.switch_to_frame('mainFrame')
# sleep(2)
# dr.find_element_by_class_name('btn_a').click()   # 新建策略
# sleep(2)
# dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a').click()  # 提交



# qq空间登录
#
# dr=webdriver.Firefox()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.switch_to_frame('login_frame')
# sleep(1)
# dr.find_element_by_id('img_out_1461633952').click()
#




# 喔影登录
#
# dr=webdriver.Firefox()
# dr.get('http://www.alltuu.com/v')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[1]/div/ul/li[6]/div/div/div/a[1]').click()
# sleep(2)
# dr.find_element_by_id('loginUsername').send_keys('17839216322')
# sleep(1)
# wd=dr.find_element_by_xpath('/html/body/ul').find_elements_by_tag_name('li')
# for j,i in enumerate(wd):
#     if j==0:
#         i.click()
#         sleep(2)
#         break
# dr.find_element_by_id('loginPassword').send_keys('meng199612@')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login"]').click()
#
# sleep(4)
# dr.quit()



# QQ邮箱标为已读

# dr=webdriver.Firefox()
# dr.get('https://mail.qq.com/')
# sleep(1)
# dr.switch_to_frame('login_frame')
# sleep(2)
# dr.find_element_by_id('img_out_1461633952').click()
# sleep(2)
# dr.switch_to_default_content()
# dr.find_element_by_xpath('//*[@id="folder_1"]').click()
# sleep(2)
# dr.switch_to_frame('mainFrame')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="ckb_selectAll"]').click()
# sleep(1)
# dr.find_element_by_id('setAllReaded').click()
# sleep(3)
#
# dr.quit()






##################################################   总结
# 鼠标移动

from selenium.webdriver.common.action_chains import ActionChains
dr=webdriver.Firefox()
dr.get('')
wd=dr.find_element_by_id('')
for i in wd:
    ActionChains(dr).move_to_element(i).perform()

# 定位一组对象
wd=dr.find_elements_by_id('')

# 获取元素中某个属性的值,如果是text的值可以直接在后面加.text
wd=dr.find_element_by_id('')
print(wd.get_attribute('src'))

# 层级定位
wd=dr.find_element_by_id('').find_elements_by_tag_name('')

# 处理web窗口
print(dr.current_window_handle)   # 当前的句柄
wd=dr.window_handles              # 所有的句柄
dr.switch_to_window(wd[-1])       # 切换句柄


# 处理框架
dr.switch_to_frame('')     # 切换到内置框架中
dr.switch_to.default_content()  # 退到原始页面
dr.switch_to.parent_frame()     # 切换到上一层框架



# 等待时间
from selenium import webdriver
from time import sleep
import selenium.webdriver.support.ui as ui



dr=webdriver.Firefox()
dr.get('http://www.moore.ren/')
# dr.maximize_window()
# 强制等待sleep()
sleep(2)

# 智能等待  设置控制器dr等待  (先判断等待的元素是否显示在页面，如果显示了就不需要等待，不显示则等待)
wait=ui.WebDriverWait(dr,10)  # 最大等待时间，就是说等待10秒后还是没有显示就会报错timeout
un=wait.until(lambda dr:dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[6]/div/a/img').is_displayed())
# is_displayed判断元素有没有显示在屏幕上
# is_enabled 是判断元素是否为灰化状态

print(dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[6]/div/a/img').is_displayed())

dr.quit()