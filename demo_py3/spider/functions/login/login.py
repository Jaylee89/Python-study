# -*- coding:utf8 -*-

import requests
import common.util as util
import traceback
from lxml import etree

def login():

    url='https://passport.weibo.cn/signin/login'
    #提交信息
    dat={'username':'18182428724',
    'password':'jal891012',
    'savestate':'1',
    'r':'',
    'ec':'0',
    'pagerefer':'',
    'entry':'mweibo',
    'wentry':'',
    'loginfrom':'',
    'client_id':'',
    'code':'',
    'qq':'',
    'mainpageflag':'1',
    'hff':'',
    'hfp':''}
    #模拟浏览器信息
    header={'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'152',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'',
    'Host':'passport.weibo.cnn',
    'Referer':'https://passport.weibo.cn/signin/login?display=0&retcode=6102',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}
    session=requests.session()
    html=session.post(url,dat,header)
    html.encoding = 'gb2312'
    content1 = html.text
    # content1.encode('utf-8').decode('unicode_escape')
    util.saveFile(content1, "login")
    #html.text
    html2=session.get('https://m.weibo.cn/')
    html2.encoding='gb2312'
    content=html2.text
    # content.encode('utf-8').decode('unicode_escape')
    util.saveFile(content, "home")
    get_username(session)


def get_username(session):
    try:
        url = "https://weibo.cn/%d/info" % (2608649530)
        # html = requests.get(url, cookies=self.cookie).content
        # html = requests.get(url, cookies=cookie).content
        html = session.get(url)
        html.encoding = 'gb2312'
        content = html.text
        # content.decode('unicode_escape')
        selector = etree.HTML(content)
        username = selector.xpath("//title/text()")[0]
        print("用户名: " , username[:-3])

    except Exception as e:
        print("Error: ", e)
        # traceback.print_exc()

if __name__ == "__main__":
    login()