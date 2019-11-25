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
# 进入qq首页
dr.get('https://y.qq.com/')
sleep(2)
# 点击 我的音乐
dr.find_element_by_xpath('/html/body/div[1]/div/ul[1]/li[2]/a').click()
sleep(5)
# 切换到白色框架
dr.switch_to.frame('divdialog_0')
sleep(2)
# 切换到 关闭 框架
dr.switch_to_frame('popup__hd')
sleep(2)
dr.switch_to_frame('')
# 点击关闭按钮
dr.find_element_by_xpath('/html/body/div[10]/div[1]/a/i[1]').click()
sleep(2)
# 点击 立即登录
dr.find_element_by_xpath('/html/body/div[3]/div/div/a').click()
sleep(2)
# 切换到 登陆 框架
dr.switch_to.frame('divdialog_0')
sleep(2)
# 点击 账号密码登陆
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(2)
# 输入账号
dr.find_element_by_id('u').send_keys('2424672489')
sleep(5)
# 输入密码
dr.find_element_by_id('p').send_keys('LianQing0919*')
sleep(5)
# 点击登陆
dr.find_element_by_css_selector('#login_button').click()
sleep(3)













