# -*- coding:utf8 -*-
__author__ = 'Jaylee'

from Tkinter import *
from ScrolledText import ScrolledText
import urllib, re, threading, sys
import requests
import random, time
#import io

reload(sys)
sys.setdefaultencoding('utf-8')

#python3
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #'改变标准输出的默认编码'.encode('gbk')

url_name = [] #
index = 1 # page index
def get():
    global index
    hd = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.5.0.15179"}
    url = "http://www.budejie.com/video/"+str(index)
    #UnicodeEncodeError: 'gbk' codec can't encode character u'\xa9' in position 597331: illegal multibyte sequence
    html = requests.get(url, headers=hd).text.encode('GB18030')
    index+=1
    print html
    saveFile(html, index)
    url_content = re.compile(r'<div class="j-r-list-c">(.*?)</div>', re.S)
    url_contents = re.findall(url_content, html)
    print url_contents
    print 'len is ', len(url_contents)

    for i in url_contents:
        url_reg = r'data-mp4="(.*?)"'
        url_items = re.findall(url_reg, i)
        print url_items
        if url_items:
            name_reg = re.compile(r'<a href="/detail-.{8}?.html">(.*?)</\w>', re.S)
            name_items = re.findall(name_reg, i)
            for j, k in zip(name_items, url_items):
                url_name.append([j, k])
                print j, k
    return url_name

def saveFile(content,name):
    fileName = str(name) + ".html"
    f = open(fileName,"w")
    print u"正在写入文件",fileName
    #f.write(content.encode('utf-8'))
    f.write(content.decode('GB18030').encode("utf-8"))

d=get()

id = 1 #video
def write():
    global id
    while id<10:
        url_name = get()
        for i in url_name:
            urllib.urlretrieve(i[1], 'video\\%s.mp4' % (i[0].decode('utf-8').encode('gbk')))
            text.insert(END, str(id)+'.'+i[1])
    text.insert(END, u"爬取结束")


root = Tk();

root.title("Mobile1.5 Deployment")
root.geometry("+600+100")

text = ScrolledText(root, font=(u'微软雅黑', 10))
text.grid()

def callback():
    global var
    var.set(u'开始爬虫')
    #write()
    time.sleep(random.randint(0, 5))
    var.set(u'爬取结束')
button = Button(root, text="Start", font=(u'微软雅黑', 10), command=callback)
button.grid()#.pack()
var = StringVar()
label = Label(root, font=(u'微软雅黑', 10), fg="red", textvariable=var)
label.grid()
var.set('it\'s ready...')

root.mainloop()
