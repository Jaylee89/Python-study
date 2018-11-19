# -*- coding:utf8 -*-

import re, random, time, datetime
import urllib
from bs4 import BeautifulSoup

import importlib, sys, os, io
# import common.log as log
from common.db import DB
from common.hashcode import SHA
import common.util as util
from common.nosqldb import NoSqlDB as nosqldb

from config.config import DBConfig as dbconfig
from config.config import NoSQLConfig as nosqlconfig

from functions.dao.Moment import Moment

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
importlib.reload(sys)

# public_url = r"http://www.gzedu.gov.cn/gzsjyj/tzgg/"
# FQDN = r"http://www.gzedu.gov.cn{}"

"""
Guang Zhou Education
"""


class Education(object):
    def __init__(self, host, id):
        self._host = host
        self._id = id

    def path_absolution(self):
        return "{}{}".format(self._host, "/gzsjyj/tzgg/{}")

    def get_html(self, page):
        headers = {
            "Host": self._host[7:],
            "User-Agent": util.get_useragent_random(),
            # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "keep-alive"
        }

        req = urllib.request.Request(page, headers=headers)
        resp = urllib.request.urlopen(req)
        data = resp.read()
        data = data.decode('utf-8')
        return data

    def main(self, index, v):
        html = self.get_html(v)
        data = self.parserHtml(html)
        log.debug(r'main-->method-->urls\'s length is', len(data))
        self.update_database(data)

    def parserHtml(self, content):
        # soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8').decode('gbk')
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        # soup = BeautifulSoup(content,'html.parser')
        data_list = []
        # soup.find_all("div", attrs={"class":"j-r-list"}) #list
        log.debug("page title is %s" % soup.find("head").title.get_text())
        li_list = soup.find_all("div", attrs={"id": "pagediv"})  # li list
        # li_list = soup.find_all(attrs={"type": "false"})
        main_page = soup.find("div", attrs={"class": "news_list"})
        li_list = main_page.find_all("li")
        log.debug('parserHtml-->method-->li_list is ', len(li_list))

        for li in li_list:
            a_tag = li.find("a")
            a_tag_href = a_tag.get("href")
            a_tag_title = a_tag.get("title")
            publish_time = li.span.get_text()
            data_list.append((a_tag_title, self.get_full_address(a_tag_href), publish_time.strip()[1:-1]))
            log.debug("result is (%s, %s, %s)" % (a_tag_title, a_tag_href, publish_time))
        return data_list

    def update_database(self, data):
        insertDB = DB(dbconfig())
        fetchDB = DB(dbconfig())
        insert = """INSERT INTO education(type, priority, title, url, create_time, update_time, hashcode, city_id) \
        VALUES ('1', 'm', '{}', '{}', '{}', '{}', '{}', '{}')"""
        fetch = """select * from education where hashcode='%s'"""

        dicts = []  # for mongo data
        for (title, href, publish) in data:
            t = time.strftime("%Y-%m-%d", time.localtime())
            publish_date = publish.strip()
            temp = """{},{}""".format(title, publish_date)
            hashcode = SHA().getSha512(temp)
            fetchScript = fetch % hashcode
            retult = fetchDB.get_existing_data(fetchScript)
            if retult is not None:
                continue
            insertScript = insert.format(title, href, t, publish_date, hashcode, self._id)
            log.debug("insertScript is %s" % insertScript)
            log.debug("insertScript is %s" % insertScript)
            insertDB.update_data(insertScript)
            log.debug("operation done")
            log.debug("insert data to mongo, prepare data")
            dicts.append(Moment(self._id, title, href, publish_date).get_dict())
            break

        log.debug('data operation successfully to mysql')
        insertDB.close_connection()
        log.debug("insert data to mongo, start")
        nosql = nosqldb(nosqlconfig())
        nosql.insert_many("News", dicts)
        log.debug("insert data to mongo, end")

    def get_full_address(self, href):
        return "{}{}".format(self._host, "{}".format(href[5:]))

    def getMaxPage(self, url):
        # final_url = "http://%s/gzsjyj/tzgg/%s" % (self._host, url)
        file_content, html = None, None
        data_list = []
        html = self.get_html(url)
        # html = get_load_html(url)
        # log.debug("content is ", html)
        util.saveFile(html, "home")  # "home".encode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')  # BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        log.debug(soup.find("head").title.get_text())

        scripts = soup.find_all("script")
        pattern = re.compile(r'\d+')
        retult = [-1]
        for script in scripts:
            text = script.get_text()
            if text is "":
                continue
            if re.search(r"createPageHTML", text, re.M | re.I):
                pattern = re.compile(r'\d+')
                retult = pattern.findall(text)
                break
        return int(retult[0]) + 1

    def start(self):
        begin = datetime.datetime.now()
        public_url = self.path_absolution()
        final_url = public_url.format("list.shtml")
        max_page = self.getMaxPage(final_url)
        for i in list(range(1, max_page)):
            if i is not 1:
                final_url = public_url.format("list_%d.shtml" % (i))
                break
            log.debug('final_url--->' + final_url)
            time.sleep(random.randint(0, 2))
            self.main(i, final_url)

        end = datetime.datetime.now()
        k = end - begin
        log.debug("complete spider, usage time is %s" % k)


# if __name__ == "__main__":
#     begin = datetime.datetime.now()
#     # edu = gz_education(r"http://www.gzedu.gov.cn/gzsjyj/tzgg/")
#     edu = gz_education(r"http://www.gzedu.gov.cn", 1)
#     public_url = edu.path_absolution()
#     final_url = public_url.format("list.shtml")
#
#     max_page = edu.getMaxPage(final_url)
#     # max_page = 5
#     for i in list(range(1, max_page)):
#         if i is not 1:
#             final_url = public_url.format("list_%d.shtml" % (i))
#             break
#         log.debug('final_url--->' + final_url)
#         time.sleep(random.randint(0, 2))
#         edu.main(i, final_url)
#     end = datetime.datetime.now()
#     k = end - begin
#     log.debug("complete spider, usage time is %s" % k)
