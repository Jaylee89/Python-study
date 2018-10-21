# -*- coding:utf8 -*-

import time, random
from functions.weibo.weibo import Weibo
from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar

class Cookie():
    def __init__(self):
        pass
    def save_cookie_to_file(self, req):
        # 设置保存cookie的文件，同级目录下的cookie.txt
        filename = 'cookie.txt'
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookiejar.MozillaCookieJar(filename)
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        handler = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
        opener = request.build_opener(handler)
        # 此处的open方法打开网页
        response = opener.open(req)
        if response.getheader('Set-Cookie') != None:
            cj = response.getheader('Set-Cookie').split(';')[0]
            print(cj)
        # 保存cookie到文件
        cookie.save(ignore_discard=True, ignore_expires=True)

    def load_existing_cookie(self):
        # 设置保存cookie的文件的文件名,相对路径,也就是同级目录下
        filename = 'cookie.txt'
        # 创建MozillaCookieJar实例对象
        cookie = cookiejar.MozillaCookieJar()
        # 从文件中读取cookie内容到变量
        cookie.load(filename, ignore_discard=True, ignore_expires=True)
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        handler = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
        opener = request.build_opener(handler)
        return opener

    def weibo_simulator(self):
        retult = None
        cookie_file = 'cookie.txt'
        # 登陆地址
        login_url = 'https://passport.weibo.cn/sso/login'
        # User-Agent信息
        user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
        # Headers信息
        header = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
        # 登陆Form_Data信息
        Login_Data = {}
        Login_Data['username'] = '18182428724'
        Login_Data['password'] = 'jal891012'
        Login_Data['savestate'] = '1'
        Login_Data['r'] = 'https://m.weibo.cn'
        Login_Data['ec'] = '0'
        Login_Data['pagerefer'] = 'https://m.weibo.cn/login?backURL=https%253A%252F%252Fm.weibo.cn%252F'
        Login_Data['entry'] = 'mweibo'
        Login_Data['wentry'] = ''
        Login_Data['loginfrom'] = ''
        Login_Data['client_id'] = ''
        Login_Data['code'] = ''
        Login_Data['qq'] = '0'
        Login_Data['hff'] = ''
        Login_Data['hfp'] = ''
        # 使用urlencode方法转换标准格式
        logingpostdata = parse.urlencode(Login_Data).encode('utf-8')
        # 声明一个CookieJar对象实例来保存cookie
        # cookie = cookiejar.CookieJar()
        # cookie = cookiejar.MozillaCookieJar(cookie_file)
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        # cookie_support = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
        # opener = request.build_opener(cookie_support)
        # 创建Request对象.
        login_url_prelogon = r"https://passport.weibo.cn/signin/login"
        login_url_prelogon_data = {
            "entry":"mweibo",
            "res": "wel",
            "wm": "3349",
            "r": "https%3A%2F%2Fm.weibo.cn"
        }
        req1 = request.Request(url=login_url_prelogon, data=login_url_prelogon_data, headers=header)
        req2 = request.Request(url=login_url, data=logingpostdata, headers=header)
        try:
            # 使用自己创建的opener的open方法
            # first link info
            self.save_cookie_to_file("https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn")
            time.sleep(random.randint(2, 3))
            # self.save_cookie_to_file("https://captcha.weibo.com/static/js/patternLock.min.js")
            opener = self.load_existing_cookie()

            response = opener.open(req2)
            html = response.read().decode('utf-8')
            print(r'html is :\n%s' % html)
            retult = "SUCCESS"
        except error.URLError as e:
            if hasattr(e, 'code'):
                print("HTTPError:%d" % e.code)
            elif hasattr(e, 'reason'):
                print("URLError:%s" % e.reason)
            retult = None
        except Exception as e:
            if hasattr(e, 'code'):
                print("Exception:%d" % e.code)
            elif hasattr(e, 'reason'):
                print("Exception:%s" % e.reason)
            retult = None
        finally:
            return retult


if __name__ == '__main__':
    cookie = Cookie()
    # cookie.save_cookie_to_file()
    # cookie.load_existing_cookie()
    cookie.weibo_simulator()

    # user_id = 2608649530
    # filter = 0
    # wb = Weibo(user_id, filter)
    # wb.get_username(cookie)