# -*- coding:utf8 -*-

import re, random, time, datetime
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import importlib, sys, os, io
import spider.common.log as log
from spider.common.db import DB
from spider.common.hashcode import SHA
from spider.config.config import DBConfig as dbconfig

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
importlib.reload(sys)

public_url = r"http://www.gzedu.gov.cn/gzsjyj/tzgg/"
FQDN = r"http://www.gzedu.gov.cn{}"

def get_html(page):
    headers = {
        "Host": "www.gzedu.gov.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive"
    }

    req = urllib.request.Request(page, headers=headers)
    resp = urllib.request.urlopen(req)
    data = resp.read()
    data = data.decode('utf-8')
    return data

def main(index, v):
    html = get_html(v)
    data = parserHtml(html)
    print(r'main-->method-->urls\'s length is', len(data))
    update_database(data)

def parserHtml(content):
    # soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8').decode('gbk')
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    # soup = BeautifulSoup(content,'html.parser')
    data_list = []
    # soup.find_all("div", attrs={"class":"j-r-list"}) #list
    print("page title is %s" % soup.find("head").title.get_text())
    li_list = soup.find_all("div", attrs={"id": "pagediv"})  # li list
    # li_list = soup.find_all(attrs={"type": "false"})
    main_page = soup.find("div", attrs={"class": "news_list"})
    li_list = main_page.find_all("li")
    print('parserHtml-->method-->li_list is ', len(li_list))

    for li in li_list:
        a_tag = li.find("a")
        a_tag_href = a_tag.get("href")
        a_tag_title = a_tag.get("title")
        publish_time = li.span.get_text()
        data_list.append((a_tag_title, get_full_address(a_tag_href), publish_time.strip()[1:-1]))
        print("result is (%s, %s, %s)" % (a_tag_title, a_tag_href, publish_time))
    return data_list

def update_database(data):
    insertDB = DB(dbconfig())
    fetchDB = DB(dbconfig())
    insert = """INSERT INTO education(type, priority, title, url, create_time, update_time, hashcode) \
    VALUES ('1', 'm', '{}', '{}', '{}', '{}', '{}')"""
    fetch = """select * from education where hashcode='%s'"""

    for (title, href, publish) in data:
        t = time.strftime("%Y-%m-%d", time.localtime())
        publish_date = publish.strip()
        temp = """{},{}""".format(title, publish_date)
        hashcode = SHA().getSha512(temp)
        fetchScript = fetch % hashcode
        retult = fetchDB.get_existing_data(fetchScript)
        if retult is not None:
            continue
        insertScript = insert.format(title, href, t, publish_date, hashcode)
        print("insertScript is %s" % insertScript)
        log.debug("insertScript is %s" % insertScript)
        insertDB.update_data(insertScript)
        log.debug("operation done")

    print('data operation successfully')
    insertDB.close_connection()

def get_full_address(href):
    return FQDN.format(href[5:])

def saveFile(content, name):
    fileName = str(name) + ".html"
    with open(fileName, "w", 1024, "utf8") as f:
        print("正在写入文件", fileName)
        f.write(content)  # content.encode('utf-8')


def getMaxPage(url):
    file_content, html = None, None
    data_list = []
    html = get_html(url)
    # html = get_load_html(url)
    print("content is ", html)
    saveFile(html, "home")  # "home".encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')  # BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    print(soup.find("head").title.get_text())

    scripts = soup.find_all("script")
    pattern = re.compile(r'\d+')
    retult = [-1]
    for script in scripts:
        text = script.get_text()
        if text is "":
            continue
        if re.search(r"createPageHTML", text, re.M|re.I):
            pattern = re.compile(r'\d+')
            retult=pattern.findall(text)
            break
    return int(retult[0])+1

if __name__ == "__main__":
    begin = datetime.datetime.now()
    max_page = getMaxPage(public_url + "list.shtml")
    # max_page = 5
    for i in list(range(1, max_page)):
        if i is 1:
            final_url = public_url + ("list.shtml")
        else:
            final_url = public_url + ("list_%d.shtml" % (i))
            break
        print('final_url--->', final_url)
        time.sleep(random.randint(0, 2))
        main(i, final_url)
    end = datetime.datetime.now()
    k = end - begin
    print("complete spider, usage time is %s" % k)