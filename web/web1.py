#!/usr/bin/python
#-*-coding:utf-8-*-#
from time import sleep

#打开浏览器，请求网址
from selenium import webdriver
# 选择浏览器
dr = webdriver.Firefox()
# 打开网址
dr.get('https://www.baidu.com')
# dr.get('https://www.jd.com/')
# dr.get('https://www.ctrip.com')
# sleep(2)
# 安装的什么浏览器驱动就联想什么浏览器
#
# 获取当前页面的标题  断言：预期与实际结果是否一致
# dr.title
# print(dr.title)
# assert dr.title=='京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！'
# 获取当前网址url  做断言
# dr.current_url
# 设置浏览器窗口的大小
#   最大化浏览器窗口
# print(dr.maximize_window())
# sleep(2)
#   最小化
# dr.minimize_window()
#   设置窗口    大小
# dr.set_window_size(500,800)
#   设置浏览器窗口 位置
# dr.set_window_position(100,100)
#
# dr.get('https://re.taobao.com/search_ou?keyword=%E5%A5%B3%E8%A3%852019%E6%96%B0%E6%AC%BE%E6%BD%AE&catid=&refpid=mm_26632258_3504122_32538762&_input_charset=utf8&clk1=783aeb609b92367c1a1b6660fc2dbe4f&spm=a2e15.8261149.07626516005.1.e7f029b4zXalqQ')
# sleep(2)
# dr.get('https://re.taobao.com/search_ou?keyword=%E5%A5%B3%E8%A3%852019%E7%A7%8B%E8%A3%85&catid=&refpid=430292_1006&_input_charset=utf8&clk1=e45ea2eec2065349c2ddd072e0aaeabb&spm=a231k.8165028.0782702701.1.7de32e639yJVcz')
# sleep(3)
# #   回退
# dr.back()
# sleep(5)
# #   前进
# dr.forward()
# sleep(2)
#
# dr.get('https://www.tmall.com/')
# dr.get('https://ju.taobao.com/jusp/other/mingpin/tp.htm?spm=875.7931836/B.2017039.4.66144265SzvFGe&pos=2&acm=201708280-2.1003.2.6966849&scm=1003.2.201708280-2.OTHER_1573130649831_6966849')
# dr.get('https://detail.ju.taobao.com/home.htm?spm=608.7763366.J_l39srnjiz00.2.5bd96462uErszt&id=10000606739705&item_id=593754281603')
#
# 关闭浏览器
# dr.quit()     #彻底退出浏览器
# sleep(5)
# dr.close()    #关闭浏览器窗口
#
# dr.get('https://mail.qq.com')
# sleep(3)
# dr.switch_to.frame('login_frame')
#
# 定位方法
# 1.id
# dr.find_element_by_id('u').send_keys('2424672489@qq.com')
# sleep(2)
# dr.find_element_by_id('p').send_keys('LianQing0919*')
# sleep(2)
# dr.find_element_by_id('login_button').click()
# sleep(2)
#
# 2.class
#
# 3.xpath
# dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[1]/a[3]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('肖战')
# sleep(2)
#
# 4.name
# dr.find_element_by_name('wd')
#
# 5.tag_name 标签
#
# 6.link_test 通过文本来定位
# dr.find_element_by_link_text('新闻').click()
#
# 7.partial_link_text  通过模糊文本
# dr.find_element_by_partial_link_text('hao').click()
#
# 8.css_selector  通过css定位
# dr.find_element_by_css_selector('a.mnav:nth-child(1)').click()
# sleep(2)
#
# dr.close()

#list定位 （定位一组对象）
# # ww = dr.find_elements_by_class_name('mnav')
# ww = dr.find_element_by_id('u1').find_elements_by_tag_name('u')
# for i in ww:
# #     #获取某个属性的值
#     i.click()
#     sleep(2)
    # print(i.get_attribute('href'))
    # sleep(2)

#绝对定位 （层级定位）   先定位父元素，在定位子元素,父元素必须唯一
# ww=dr.find_element_by_id('J_roomCountList').find_elements_by_tag_name('option')
# for i in ww:
#     i.click()
#     sleep(2)
#     print(i.get_attribute('text'))

# dr.get('https://qzone.qq.com/')
# sleep(2)
# 切换框架  内嵌框架 iframe
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(4)
# dr.close()

# dd=dr.find_element_by_xpath('//*[@id="login_frame"]')
# dr.switch_to.frame(dd)
# sleep(3)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]')
# sleep(3)

# #退出框架   退出到最开始页面
# dr.switch_to.default_content()
# #退出到上一级框架
# dr.switch_to.parent_frame()

#切换窗口
# 浏览管理窗口：通过句柄来管理窗口
# 句柄：唯一标识一个窗口的字符串
#   获取当前窗口的句柄
# print(dr.current_window_handle)
# dr.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[4]/ul[1]/li[1]/a').click()
# sleep(2)
# #   获取所有句柄
# # print(dr.window_handles)
# ww=dr.window_handles
# #   切换到第二个窗口
# dr.switch_to.window(ww[1])
# print(dr.title)

# dr.find_element_by_id('kw').send_keys('qq空间')
# sleep(1)
# dr.find_element_by_id('su').click()
# sleep(2)
# # dr.switch_to.frame('wrapper_wrapper')
# # dr.switch_to.frame('content_left')
# dr.find_element_by_id('1').find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/h3/a[1]').click()
# sleep(2)
# dr.switch_to.frame('login ')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)

#打开网址
dr.get('file:///E:/1905/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/abc.html')
sleep(2)
dr.find_element_by_xpath('/html/body/button').click()
sleep(2)
# 处理alert弹出框
# 切换到弹出框
ww=dr.switch_to_alert()
# 获取弹出框上文本信息
print(ww.text)
ww.send_keys('hello world!')
# 点击确定
ww.accept()
# 点击取消
# ww.dismiss()
sleep(2)
dr.close()


























