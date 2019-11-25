#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait  # 显性等待 模块导入

dr= webdriver.Firefox()
dr.implicitly_wait(5)  #隐性等待
dr.get('https://www.jd.com')
sleep(2)
dr.maximize_window()
sleep(2)
ww=dr.find_elements_by_class_name('cate_menu_item')
# ActionChains(dr).move_to_element(ww).perform()  #perfrom 立即执行
for i in ww:
    sleep(2)
    ActionChains(dr).move_to_element(i).perform()
    sleep(2)

# dr.maximize_window()
# sleep(2)
# ww = dr.find_elements_by_class_name('cate_menu_item')
# for i in ww:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)

# 强制等待  sleep
# 显性等待  WebDriverWait
# ww=ui.WebDriverWait(dr,10)
# ww.until(lambda dr:dr.find_element_by_id('').is_displayed()) #dispalyed 判断元素是否可见
# 隐性等待  implicitly_wait(5)  针对全局页面等待


# qq空间执行到滑动窗口
# dr.get('https://qzone.qq.com')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('2209878102')
# sleep(2)
# dr.find_element_by_id('p').send_keys('Lian7')
# sleep(2)
# dr.find_element_by_id('login_button').click()
# sleep(2)
# dr.switch_to.frame('tcaptcha_iframe')
# sleep(2)
# dd=dr.find_element_by_xpath('//*[@id="slideBlock"]')
# ActionChains(dr).drag_and_drop_by_offset(dd,171,0).perform()

# dr.get('https://www.douban.com')
# sleep(2)
'''1.通过网页高度 拉动 滚动条'''
# js='var q=document.documentElement.scrollTop=1500'
# sleep(2)
# # 执行JavaScript语句
# dr.execute_script(js)
# dr.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/h2/a').click()
# sleep(202)
'''2.通过网页元素让滚动条 滚动'''
# dd=dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/a')
# # js='arguments[0].scrollIntoView();'
# # dr.execute_script(js,dd)
# dr.execute_script('arguments[0].scrollIntoView();',dd)
# sleep(2)
# dr.close()





