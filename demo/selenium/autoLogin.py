#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
cnblog的登录测试，分下面几种情况：
(1)用户名、密码正确
(2)用户名正确、密码不正确
(3)用户名正确、密码为空
(4)用户名错误、密码正确
(5)用户名为空、密码正确（还有用户名和密码均为空时与此情况是一样的，这里就不单独测试了）
'''
import unittest, os
from selenium import webdriver
from time import sleep
import log

log.debug("execute autoLogin.py file now...")

#chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
os.environ["webdriver.chrome.driver"] = chromedriver


class LoginCase(unittest.TestCase):
    def setUp(self):
        #self.dr = webdriver.Chrome()
        self.dr = webdriver.Chrome(chromedriver)
        self.now_handle = self.dr.current_window_handle 
        print "now_handle is", self.now_handle
        #self.dr.maximize_window()
        log.debug("setup is ready!")

    # 定义登录方法
    def login(self, username, password):
        self.dr.get('http://192.168.1.1/login.html')
        self.dr.find_element_by_id('username').send_keys(username)
        self.dr.find_element_by_id('password').send_keys(password)
        self.dr.find_element_by_name('save')[0].click()
        log.debug("logon button is", self.dr.find_element_by_name('save'))

    def test_login_success(self):
        self.login('useradmin', 'useradmin1')  
        sleep(5)
        link = self.dr.find_element_by_id('f1')
        log.debug("link.text is", link.text)
        self.assertTrue(u'状态' in link.text)
        self.dr.get_screenshot_as_file("login_success.jpg")

    #def test_login_pwd_error(self):
        u'''用户名正确、密码不正确'''
    #    self.login('kemi_xxx', 'kemi')  # 正确用户名，错误密码
    #   sleep(2)
    #    error_message = self.dr.find_element_by_id('tip_btn').text
    #    self.assertIn('用户名或密码错误', error_message)  # 用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
    #    self.dr.get_screenshot_as_file("D:\cnblogtest\\login_pwd_error.jpg")

    #def test_login_pwd_null(self):
        u'''用户名正确、密码为空'''
    #    self.login('kemi_xxx', '')  # 密码为空
    #    error_message = self.dr.find_element_by_id('tip_input2').text
    #    self.assertEqual(error_message, '请输入密码')  # 用assertEqual(a,b)方法来断言  a == b  请输入密码等于error_message
    #    self.dr.get_screenshot_as_file("D:\cnblogtest\\login_pwd_null.jpg")

    #def test_login_user_error(self):
        u'''用户名错误、密码正确'''
    #    self.login('kemixing', 'kemi_xxx')  # 密码正确，用户名错误
    #    sleep(2)
    #    error_message = self.dr.find_element_by_id('tip_btn').text
    #    self.assertIn('该用户不存在', error_message)  # 用assertIn(a,b)方法来断言 a in b
    #    self.dr.get_screenshot_as_file("D:\cnblogtest\\login_user_error.jpg")

    #def test_login_user_null(self):
        u'''用户名为空、密码正确'''
    #    self.login('', 'kemi_xxx')  # 用户名为空，密码正确
    #    error_message = self.dr.find_element_by_id('tip_input1').text
    #    self.assertEqual(error_message, '请输入登录用户名')  # 用assertEqual(a,b)方法来断言  a == b
    #    self.dr.get_screenshot_as_file("D:\cnblogtest\\login_user_null.jpg")

    #def tearDown(self):
    #    sleep(2)
    #    print('自动测试完毕！')
    #    self.dr.quit()


if __name__ == '__main__':
    unittest.main()