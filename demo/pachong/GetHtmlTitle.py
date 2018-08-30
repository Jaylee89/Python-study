#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, random, time, datetime
import urllib
import urllib2
from bs4 import BeautifulSoup
# import requests as req

import sys, os

reload(sys)
sys.setdefaultencoding('utf-8')

public_url = r"http://www.ppypp.cc/video/play/%s-1-1.html"

local = u'd:/video/视频/'

logs_folder = 'logs/'
if not os.path.isdir(logs_folder):
    os.mkdir(logs_folder)

format_datetime = "%Y%m%d%H%M%S"
timestamp = time.strftime(format_datetime, time.localtime(time.time()))
file_name = r"./logs/{name_format}_log.txt".format(
    name_format = timestamp
)
print "current file name is %s" % file_name


def get_html(page):
    headers = {
        "Host": "www.ppypp.cc",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
        "Accept": "text/html, application/xhtml+xml, application/xml, image/webp,image/*,*/*;q=0.8",
        "Accept - Encoding": "gzip, deflate, sdch",
        "Connection": "keep-alive"
    }

    req = urllib2.Request(page, headers=headers)
    resp = urllib2.urlopen(req)
    data = resp.read()

    # sock = urllib.urlopen(page)
    # numberurl = sock.read()
    # sock.close()
    data = data.decode('utf-8')
    # numberurl = numberurl.decode('gbk')
    return data


def cur_file_dir():
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def print_log_in_file(log):

    with open(file_name, 'a') as file_to_write:
        file_to_write.write(log.encode('utf-8') + "\n") #os.linesep
        print "complete file write, content is %s " % log
        file_to_write.close()

def get_title(index, html):
    content = ""
    if html is "" or html is None:
        return content
    else:
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        content = r"%s, %s" % (index, soup.find("head").title.get_text())
    print_log_in_file(content)
    return (index, soup.find("head").title.get_text())

def main(index, v):
    html = get_html(v)
    get_title(index, html)

if __name__ == "__main__":

    #number = raw_input(u'请输入您期望的页面下标(大于1的整数):'.encode('gbk'))
    #number = int(number) + 1
    start = 67331
    end = 67555

    for i in range(start, end):
        #if i == 2:
        #    break
        final_url = public_url % str(i)
        print 'final_url--->', final_url
        time.sleep(random.randint(0, 5))
        try:
            main(i, final_url)
        except IOError as e:
            print "this page(%s) have IO issue" % str(i)
            continue

    print u"download complete"