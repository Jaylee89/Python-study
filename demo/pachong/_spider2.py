# -*- coding:utf8 -*-


import re, random, time
import urllib
import requests as req

#import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

def get_html(url):
    send_headers = {
        "Host":"www.budejie.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.5.0.15179",
        "Accept": "text/html, application/xhtml+xml, application/xml, image/webp,image/*,*/*;q=0.8",
        "Connection":"keep-alive"
    }
    page = urllib.Request(url, headers=send_headers)
    sock = urllib.urlopen(page)
    numberurl = sock.read()
    sock.close()
    #numberurl = numberurl.decode('utf-8')
    numberurl = numberurl.decode('gbk')
    return numberurl

def download(mp4_url, path):
    path = "".join(path.split())
    urllib.urlretrieve(mp4_url, './%s.mp4' % path)
    print u'下载成功%s' % path

def get_mpl_url(request):
    reg = r' data-mp4="(.*?.mp4)"'
    mpl_url = re.findall(reg, request)
    return mpl_url

def get_name(request):
    reg = re.compile(r'<div class"j-r-list-c-desc">(.*?)</div>', re.S)
    name = re.findall(reg, request)
    return name

def main():
    html = get_html(url)
    mp4_url = get_mpl_url(html)
    mp4_name = get_name(html)

    try:
        for x, y in zip(mp4_url, mp4_name):
            if '/' in y:
                continue
            download(x, y)
    except IOError as e:
        print "have IO issue in file download", e

if __name__ == "__main__":
    number = raw_input(u'请输入要下载的视频页数')
    number = int(number)
    i=1
    for i in range(i, number):
        url = 'http://www.budejie.com/video/%d' % i
        time.sleep(random.randint(20, 30))
        print u'正在打开下载第%d页' %i
        main()
        i +=1
    print u"下载完成"








