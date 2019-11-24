#!/usr/bin/python
#-*-coding:utf-8-*-
from time import sleep
from selenium import webdriver

dr=webdriver.Firefox()
# dr.get('https://v.qq.com/')
# # dr.switch_to.frame('login_frame')
# #点击头像
# dr.find_element_by_css_selector('.quick_user_avatar').click()
# sleep(2)
# #选择qq登陆
# dr.find_element_by_xpath('/html/body/div[46]/div[2]/div/div/div[2]/a[1]').click()
# dr.switch_to.frame('_login_frame_quick_')
# sleep(3)
# dr.switch_to.frame('ptlogin_iframe')
# sleep(5)
# #账号密码登陆
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(5)
# # 账号
# dr.find_element_by_id('u').send_keys('2424672489')
# sleep(5)
# #密码
# dr.find_element_by_id('p').send_keys('LianQing0919*')
# sleep(5)
# dr.switch_to.frame('ptlogin_iframe')
# sleep(5)
# #登陆
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(5)
# dr.switch_to.frame('slider_inner')
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[5]/a/img[1]').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[5]/div[1]/div/div[1]/a[4]').click()
# sleep(2)
# dr.switch_to.frame('ptlogin_iframe')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="keywords"]').send_keys('斗罗大陆')
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[1]/a').click()
# sleep(2)
# dr.close()

# dr.get('https://qzone.qq.com/')
# sleep(5)
# dr.switch_to.frame('login_frame')
# sleep(5)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(5)
# dr.find_element_by_id('u').send_keys('2424672489')
# sleep(5)
# dr.find_element_by_id('p').send_keys('LianQing0919*')
# sleep(5)
# dr.find_element_by_css_selector('#login_button').click()
# sleep(3)
dr.get('https://y.qq.com/')
dr.find_element_by_xpath('/html/body/div[1]/div/ul[1]/li[2]/a').click()
sleep(3)

# dr.find_element_by_xpath('')
# sleep(1)
dr.find_element_by_xpath('/html/body/div[10]/div[1]/a').click()
sleep(2)
dr.switch_to.frame('mod_popup_mask')
dr.switch_to.frame('divdialog_0')
dr.switch_to.frame('popup_hd')
dr.find_element_by_xpath('popup_close').click()
sleep(3)
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(3)
dr.find_element_by_id('u').send_keys('2424672489')
sleep(5)
dr.find_element_by_id('p').send_keys('LianQing0919*')
sleep(5)
dr.find_element_by_css_selector('#login_button').click()
sleep(3)













