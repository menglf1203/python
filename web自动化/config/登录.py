# /usr/bin/env python
# -*- coding:utf-8 -*-


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class Dl():
    def denglu1(self,a,b):
        dr=webdriver.Firefox()
        dr.get('http://www.moore.ren/')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
        sleep(2)
        wd=dr.window_handles
        dr.switch_to.window(wd[-1])
        sleep(2)
        dr.find_element_by_id('emailInput').clear()
        sleep(1)
        dr.find_element_by_id('emailInput').send_keys('{}'.format(a))
        sleep(2)
        dr.find_element_by_id('passwordInput').send_keys('{}'.format(b))
        sleep(2)
        dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
        sleep(2)

        return dr

    def denglu2(self):
        dr = webdriver.Firefox()
        dr.get('http://www.moore.ren/login/login.htm')
        sleep(2)
        return dr

    def QQkj(self,a,b):
        dr = webdriver.Firefox()
        dr.get('https://qzone.qq.com/')
        sleep(2)
        dr.switch_to_frame('login_frame')
        sleep(2)
        dr.find_element_by_id('switcher_plogin').click()
        sleep(1)
        dr.find_element_by_class_name('inputstyle').send_keys('{}'.format(a))
        sleep(1)
        dr.find_element_by_xpath('//*[@id="p"]').send_keys('{}'.format(b))
        sleep(2)
        dr.find_element_by_id('login_button').click()
        sleep(2)
        dr.switch_to_default_content()
        sleep(1)

        try:
            dr.switch_to_frame('login_frame')
            sleep(2)
            wd = dr.find_element_by_xpath('/html/body/div[1]/div[11]/div[2]/iframe')
            dr.switch_to_frame(wd)
            sleep(2)
            start = dr.find_element_by_id('tcaptcha_drag_button')
            for i in range(180,200):
                ActionChains(dr).drag_and_drop_by_offset(start, i, 0).perform()
                sleep(2)
                if 'https://user.qzone.qq.com/' in dr.current_url:
                    break

            dr.switch_to_default_content()
        except:
            pass

        return dr

    def jingdong(self):
        dr = webdriver.Firefox()
        dr.get('https://item.jd.com/7437780.html')
        sleep(2)
        dr.find_element_by_id('InitCartUrl').click()
        sleep(2)
        return dr














