# -*- coding:utf8 -*-

import re, random, time
import urllib
import urllib2
#from bs4 import BeautifulSoup

import sys, os

reload(sys)
sys.setdefaultencoding('utf-8')
t = time.time()
url = "http://gzf.xdz.com.cn/system/resource/gzf/codeimg.jsp?random="+str(int(t))

def get_image():
    t = time.time()
    headers = {
        "Host": "http://gzf.xdz.com.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.5.0.15179",
        "Accept": "text/html, application/xhtml+xml, application/xml, image/webp,image/*,*/*;q=0.8",
        "Connection": "keep-alive"
    }
    print "url is http://gzf.xdz.com.cn/system/resource/gzf/codeimg.jsp?random=1495273747" #, url
    req = urllib2.Request("http://gzf.xdz.com.cn/system/resource/gzf/codeimg.jsp?random=1495273747", headers=headers)
    resp = urllib2.urlopen(req)
    data = resp.read()

    # 写文件
    with open('./%d.png'% (t), "w", 'utf-8') as f:
        f.write(data)
        print u"文件成功"

if __name__ == "__main__":
    get_image()