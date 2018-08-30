# -*- coding:utf8 -*-

import re, random, time, datetime
import urllib
# import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# import requests as req

import importlib, sys, os, io
import spider.common.log as log
from spider.common.db import DB
from spider.config.config import DBConfig as dbconfig

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
importlib.reload(sys)
# sys.setdefaultencoding('utf-8')

public_url = r"http://www.gzedu.gov.cn/gzsjyj/tzgg/"
FQDN = r"http://www.gzedu.gov.cn{}"

# local = u'd:/video/视频/'

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


def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


def download(index, title, url):
    print('download url is', url)

    name = title + '.mp4'
    # tmp_path = local + str(index)
    tmp_path = cur_file_dir()
    print('current path is-->', tmp_path)
    tmp_path = tmp_path + u"/视频/" + str(index)
    print('local path is-->', tmp_path)
    print('download method-->tmp_path is', tmp_path)

    if os.path.exists(tmp_path) == False:
        # os.mkdir(tmp_path)
        os.makedirs(tmp_path)
    local_path = os.path.join(tmp_path, name)
    print('download method--->local_path is---->', local_path)
    # urllib.urlretrieve(url, local_path, cbk)

    f = urllib.request.urlopen(url)
    with open(local_path, "wb") as code:
        code.write(f.read())


def main(index, v):
    html = get_html(v)
    # saveFile(html, "第一页".encode('gbk'))
    # saveFile(html)
    data = parserHtml(html)

    print(r'main-->method-->urls\'s length is', len(data))

    update_database(data)


def parserHtml(content):
    # soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8').decode('gbk')
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    # soup = BeautifulSoup(content,'html.parser')
    # saveFile(soup, u"第一页-副本".encode('gbk'))
    # print r"sperateaVideo====>", soup

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
    db = DB(dbconfig())
    sql = """INSERT INTO education(type, priority, title, url, create_time, update_time) \
    VALUES ('1', 'm', '{}', '{}', '{}', '{}')"""
    for (title, href, pulish) in data:
        t = time.strftime("%Y-%m-%d", time.localtime())
        script = sql.format(title, href, t, pulish.strip())
        print("script is %s" % script)
        log.debug("script is %s" % script)
        db.update_data(script)
        log.debug("operation done")

    print('data operation successfully')
    db.close_connection()

def get_full_address(href):
    return FQDN.format(href[5:])

def saveFile(content, name):
    fileName = str(name) + ".html"
    with open(fileName, "w", 1024, "utf8") as f:
        print("正在写入文件", fileName)
        f.write(content)  # content.encode('utf-8')


def getMaxPage(url):
    # main(final_url)
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

    """
    span_list = soup.find_all("span", attrs={"class": "arrow"})  # li list
    with open('home.html', 'r', 1024, "utf8") as f:
        file_content = f.read()  # read all content of file

    # if file_content != None:
    #     span_list = file_content.find_all("span", attrs={"class": "arrow"})  # li list

    for i in range(1, len(span_list)):
        if (span_list[i].find("a") is None or ""):
            continue
        else:
            data_list.append(span_list[i].find("a").get("href"))
    # pattern = '\d+'
    final_list = []
    for i in range(1, len(data_list)):
        match = re.search(pattern='\d+', string=i)
        if (match is not None):
            final_list.append(int(match))

    final_list.sort(reverse=True)
    retult = None
    if len(final_list) > 0:
        result = final_list[0]
    """
    return int(retult[0])+1


def get_load_html(url):
    # browser = webdriver.PhantomJS(executable_path='D:\software\preinstall\DevelopTool\python\module\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    # browser.get(url)
    # time.sleep(3)
    # html = browser.execute_script("return document.documentElement.outerHTML")

    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    chrome_options.binary_location = 'C:\\Users\\Jaylee\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    html = driver.page_source
    driver.close()
    return html

if __name__ == "__main__":
    begin = datetime.datetime.now()
    max_page = getMaxPage(public_url + "list.shtml")
    # max_page = 5
    # main(0, public_url + ("list.shtml"))
    for i in list(range(1, max_page)):
        if i is 1:
            final_url = public_url + ("list.shtml")
        else:
            final_url = public_url + ("list_%d.shtml" % (i))
        print('final_url--->', final_url)
        time.sleep(random.randint(0, 2))
        main(i, final_url)
    end = datetime.datetime.now()
    k = end - begin
    print("complete spider, usage time is %s" % k)