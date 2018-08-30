# -*- coding:utf8 -*-

import re, random, time
import urllib
import urllib2
from bs4 import BeautifulSoup
#import requests as req

import sys, os

reload(sys)
sys.setdefaultencoding('utf-8')

emp = {
    #'Quality_Management' : r'http://pbox.chinasoftinc.com:8080/dokuwiki/doku.php?id=%E7%9F%A5%E8%AF%86%E5%BA%93:%E8%B4%A8%E9%87%8F:pm%E4%BB%BB%E8%81%8C%E8%AE%A4%E8%AF%81:%E4%B8%93%E9%A1%B9%E5%9F%B9%E8%AE%AD:%E8%B4%A8%E9%87%8F%E7%AE%A1%E7%90%86',
    #'Project_Plan_and_Control' : r'http://pbox.chinasoftinc.com:8080/dokuwiki/doku.php?id=%E7%9F%A5%E8%AF%86%E5%BA%93:%E8%B4%A8%E9%87%8F:pm%E4%BB%BB%E8%81%8C%E8%AE%A4%E8%AF%81:%E4%B8%93%E9%A1%B9%E5%9F%B9%E8%AE%AD:%E9%A1%B9%E7%9B%AE%E8%AE%A1%E5%88%92%E4%B8%8E%E6%8E%A7%E5%88%B6',
    #'PM_Role_Recognition' : r'http://pbox.chinasoftinc.com:8080/dokuwiki/doku.php?id=%E7%9F%A5%E8%AF%86%E5%BA%93:%E8%B4%A8%E9%87%8F:pm%E4%BB%BB%E8%81%8C%E8%AE%A4%E8%AF%81:%E4%B8%93%E9%A1%B9%E5%9F%B9%E8%AE%AD:pm%E8%A7%92%E8%89%B2%E8%AE%A4%E7%9F%A5',
    #'Summary_of_Project_Management' : r'http://pbox.chinasoftinc.com:8080/dokuwiki/doku.php?id=%E7%9F%A5%E8%AF%86%E5%BA%93:%E8%B4%A8%E9%87%8F:pm%E4%BB%BB%E8%81%8C%E8%AE%A4%E8%AF%81:%E4%B8%93%E9%A1%B9%E5%9F%B9%E8%AE%AD:%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86%E6%A6%82%E8%BF%B0',
    #'Review_and_Practice' : r'http://pbox.chinasoftinc.com:8080/dokuwiki/doku.php?id=%E7%9F%A5%E8%AF%86%E5%BA%93:%E8%B4%A8%E9%87%8F:pm%E4%BB%BB%E8%81%8C%E8%AE%A4%E8%AF%81:%E4%B8%93%E9%A1%B9%E5%9F%B9%E8%AE%AD:review%E5%8F%8A%E5%AE%9E%E8%B7%B5',
    #'Team_Development': r'http://pbox.chinasoftinc.com:8080/dokuwiki/doku.php?id=%E7%9F%A5%E8%AF%86%E5%BA%93:%E8%B4%A8%E9%87%8F:pm%E4%BB%BB%E8%81%8C%E8%AE%A4%E8%AF%81:%E4%B8%93%E9%A1%B9%E5%9F%B9%E8%AE%AD:%E5%8F%91%E5%B1%95%E5%9B%A2%E9%98%9F',
    'Quality_Planning':r'http://pbox.chinasoftinc.com:8080/dokuwiki/doku.php?id=%E7%9F%A5%E8%AF%86%E5%BA%93:%E8%B4%A8%E9%87%8F:pm%E4%BB%BB%E8%81%8C%E8%AE%A4%E8%AF%81:%E4%B8%93%E9%A1%B9%E5%9F%B9%E8%AE%AD:%E8%B4%A8%E9%87%8F%E7%AD%96%E5%88%92'

}

local = 'd:/ppt/20171212/'

def get_html(page):

    headers = {
        "Host":"pbox.chinasoftinc.com:8080",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Connection":"keep-alive",
        "Cookie":"DokuWiki=ifaade5nap3ld32466da1ks142; tpg_lang=zh-cn; tpg_ST_ACTIVE_TIME=1513090143; tpg_STLU=b4QNR8ew53MM-GrPj",
        "Cache-Control":"max-age=0",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Upgrade-Insecure-Requests": "1"
    }

    print "page is -->", page
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

def download(k, url, index):
    print 'download url is', url
    #name = get_name(url)
    name = index+'.png'
    #tmp_path = os.path.join(local, k)
    tmp_path = local + k
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

def get_name(url):
    return url[-19:]


def main(k, v):
    html = get_html(v)
    #saveFile(html)
    urls = sperateImgs(html)

    print r'main-->method-->urls\'s length is', len(urls)
    time = 0;
    try:
        for url in urls:
            time = time + 1;
            print "\n"+str(time)+"\n"
            download(k, url, str(time))
    except IOError as e:
        print "have IO issue in file download", e

def sperateImgs(content):
    soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8')#str ='<div class="hd"><h2 class="l">Hibernate注解</h2></div>'
    #dw_content = soup.find('div' ,class_ = "dw-content")
    #img_urls  = dw_content.find('img' ,class_ = "media img-responsive").get('src')
    img_urls = []
    for div in soup.find_all("div", attrs={"class":"dw-content"}):
        print "div--->", div
        for img in div.find_all('img'):
            print "img--->", img
            img_urls.append("http://pbox.chinasoftinc.com:8080"+img.get('src'))
    return img_urls

def saveFile(content):
    #fileName = str(name) + ".html"
    f = open(fileName,"w")
    print u"正在写入文件",fileName
    f.write(content.encode('utf-8'))

if __name__ == "__main__":

    for k, v in emp.items():
        print('{v}:{k}'.format(v = v, k = k))
        time.sleep(random.randint(0, 1))

        #url = r'http://pbox.chinasoftinc.com:8080/dokuwiki/doku.php?id=%E7%9F%A5%E8%AF%86%E5%BA%93:%E8%B4%A8%E9%87%8F:pm%E4%BB%BB%E8%81%8C%E8%AE%A4%E8%AF%81:%E4%B8%93%E9%A1%B9%E5%9F%B9%E8%AE%AD:%E9%A3%8E%E9%99%A9%E7%AE%A1%E7%90%86'
        print 'url-->', v
        main(k, v)
    print u"download complete"








