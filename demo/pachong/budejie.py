# -*- coding:utf8 -*-

import re, random, time
import urllib
import urllib2
from bs4 import BeautifulSoup
#import requests as req

import sys, os

reload(sys)
sys.setdefaultencoding('utf-8')

public_url = r"http://www.budejie.com/video/"

local = u'd:/video/视频/'

def get_html(page):

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


def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per

def download(index, title, url):
    print 'download url is', url

    name = title+'.mp4'
    #tmp_path = local + str(index)
    tmp_path = cur_file_dir()
    print 'current path is-->', tmp_path
    tmp_path = tmp_path + u"/视频/" + str(index)
    print 'local path is-->', tmp_path
    print 'download method-->tmp_path is', tmp_path

    if os.path.exists(tmp_path) == False:
        #os.mkdir(tmp_path)
        os.makedirs(tmp_path)
    local_path = os.path.join(tmp_path, name)
    print 'download method--->local_path is---->', local_path
    #urllib.urlretrieve(url, local_path, cbk)

    f = urllib2.urlopen(url) 
    with open(local_path, "wb") as code:
       code.write(f.read())

def main(index, v):
    html = get_html(v)
    saveFile(html, u"第一页".encode('gbk'))
    #saveFile(html)
    urls = sperateaVideo(html)

    print r'main-->method-->urls\'s length is', len(urls)

    try:
        for (t, v) in urls:
            print('{t}:{v}'.format(t = t, v = v))
            download(index, t, v)
    except IOError as e:
        print "have IO issue in file download", e

def sperateaVideo(content):
    #soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8').decode('gbk')
    soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8')
    #soup = BeautifulSoup(content,'html.parser')
    saveFile(soup, u"第一页-副本".encode('gbk'))
    #print r"sperateaVideo====>", soup

    data_list = []
    
    #soup.find_all("div", attrs={"class":"j-r-list"}) #list
    print soup.find("head").title.get_text()
    li_list = soup.find_all("li", attrs={"type":"false"}) #li list
    #li_list = soup.find_all(attrs={"type": "false"})

    print 'sperateaVideo-->method-->li_list is ', len(li_list)

    file_content = None
    if len(li_list) == 0:
        with open(ur'D:\software\preinstall\DevelopTool\python\demo\pachong\第一页.html', 'r') as f:
            file_content = f.read() #read all content of file

        if file_content != None:
            li_list = file_content.find_all("li", attrs={"type":"false"}) #li list
    for div in li_list:
        title_tag = div.find("div", attrs={"class":"j-r-list-c-desc"})
        title = title_tag.a.get_text()
        #video = li_list.find("video").get("src")
        video_tag = div.find("div", attrs={"class":" j-video"})
        video = video_tag.get("data-mp4")
        
        data_list.append((title, video))
    return data_list

def saveFile(content, name):
    fileName = str(name) + ".html"
    f = open(fileName,"w")
    print u"正在写入文件",fileName
    f.write(content.encode('utf-8'))

if __name__ == "__main__":

    number = raw_input(u'请输入您期望的页面下标(大于1的整数):'.encode('gbk'))
    number = int(number) + 1

    for i in range(1, number):
        if i==2:
            break
        final_url = public_url + str(i)
        print 'final_url--->', final_url
        time.sleep(random.randint(0, 1))
        main(i, final_url)
        
    print u"download complete"








