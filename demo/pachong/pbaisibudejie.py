# -*- coding:utf8 -*-
# -*- coding:utf8 -*-

import re, random, time
import urllib
import urllib2
from bs4 import BeautifulSoup
#import requests as req

import sys, os

reload(sys)
sys.setdefaultencoding('utf-8')

def get_html(page):
    #send_headers = {
    #    "Host":"www.budejie.com",
    #    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.5.0.15179",
    #    "Accept": "text/html, application/xhtml+xml, application/xml, image/webp,image/*,*/*;q=0.8",
    #    "Connection":"keep-alive"
    #}
    #page = urllib2.Request(url, headers=send_headers)
    #sock = urllib2.urlopen(page)
    

    #headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    #opener = urllib.request.build_opener()
    #opener.addheaders = [headers]
    #data = opener.open(url).read()

    headers = {
        "Host":"www.budejie.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.5.0.15179",
        "Accept": "text/html, application/xhtml+xml, application/xml, image/webp,image/*,*/*;q=0.8",
        "Connection":"keep-alive"
    }

    req = urllib2.Request(page, headers=headers)
    resp = urllib2.urlopen(req)
    data = resp.read()

    #sock = urllib.urlopen(page)
    #numberurl = sock.read()
    #sock.close()
    data = data.decode('utf-8')
    #numberurl = numberurl.decode('gbk')
    return data

def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
        return path
     elif os.path.isfile(path):
        return os.path.dirname(path)

def download(mp4_url, path):
    path = "".join(path.split())
    current_path = cur_file_dir()
    print 'download path-->', current_path
    #unicodestring = ur'\\视频\\%s.mp4'.encode('gbk') % path.strip()
    #asciistring = unicodestring.decode()
    #asciistring = unicodestring
    vedioPath = current_path + os.sep + u"视频"
    print 'file name is ', path.strip()
    finalPath = vedioPath + path.strip() + '.mp4'
    if os.path.exists(vedioPath) == False:
        #os.mkdir(vedioPath)
        os.makedirs(vedioPath)
    print 'finalPath is', finalPath
    #urllib.urlretrieve(mp4_url, r'D:\\software\\preinstall\\DevelopTool\\python\\demo\\pachong\\pbaisibudejie.py\\%s.mp4' % path)
    print 'mp4_url is', mp4_url
    urllib.urlretrieve(mp4_url, finalPath)
    print u'download success%s' % path

def get_mpl_url(request):
    reg = r' data-mp4="(.*?.mp4)"'
    mpl_url = re.findall(reg, request)
    print 'mpl_url is ', mpl_url
    return mpl_url

def get_url_name(html_cont):
    soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')#str ='<div class="hd"><h2 class="l">Hibernate注解</h2></div>'
    name = soup.find('div' ,class_ = "j-r-list-c-desc").get_text()
    url  = soup.find('div' ,class_ = " j-video").get('data-mp4')
    print "len(name)-->", len(name), 'name is ', name
    print "len(url)-->", len(url), 'url is ', url
    dict_data = {}
    dict_data[name] = url
    return dict_data

def get_name(html_cont):
    soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')#str ='<div class="hd"><h2 class="l">Hibernate注解</h2></div>'
    name = soup.find('div',class_ = "j-r-list-c-desc").get_text()
    print '\nget_name-->%s\n' % name
    return (url, name)

def get_name2(request):
    reg = re.compile(r'<div class="j-r-list-c-desc">(.*?)</div>', re.S)
    a_tag = re.findall(reg, request)
    reg2 = re.compile(r'>(.*?)<', re.S)
    name = re.findall(reg2, '%s' % re.findall(reg, request))
    print '\nget_name%s\n' % name
    #.replace("\r\n","").replace(' ', '')
    return name

def main(url, index):
    html = get_html(url)
    saveFile(html, index)
    dict2 = get_url_name(html)
    #print 'html is', html
    #mp4_url = get_mpl_url(html)

    #print 'mp4_url is', mp4_url
    #mp4_name = get_name(html)
    #print 'mp4_name is', mp4_name

    try:
        #for x, y in zip(mp4_url, mp4_name):
        for name in dict2.items():
            print "\n"
            #print '\n(x,y)===>(%s, %s)' % (x, dict2[x])
            #print dict2[name], name
            #if '/' in y:
            #    continue
            download(dict2[name], name)
            break
    except IOError as e:
        print "have IO issue in file download", e

def saveFile(content,name):
    fileName = str(name) + ".html"
    f = open(fileName,"w")
    print u"正在写入文件",fileName
    f.write(content.encode('utf-8'))

if __name__ == "__main__":
    number = raw_input(u'请输入您期望的页面下标(大于1的整数):'.encode('gbk'))
    number = int(number)
    i=1
    for i in range(i, number):
        url = 'http://www.budejie.com/video/%d' % i
        print 'url-->', url
        time.sleep(random.randint(0, 5))
        print u'download %dth path' %i
        main(url, i)
        i +=1
    print u"download complete"








