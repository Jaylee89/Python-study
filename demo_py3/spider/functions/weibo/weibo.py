#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# https://github.com/dataabc/weiboSpider

import os, random, re, requests, sys
import time as Time
import traceback
from datetime import datetime
from datetime import timedelta
from lxml import etree

import common.log as log
import common.util as util

from common.db import DB
from functions.dao.Moment import Moment

from common.hashcode import SHA
from config.config import DBConfig as dbconfig
from common.nosqldb import NoSqlDB as nosqldb
from config.config import NoSQLConfig as nosqlconfig

class Weibo:
    cookie = {
        "Cookie": "_T_WM=32574a5519a6b59a7325d3fcc2854360; MLOGIN=0; SUB=_2A252yBshDeRhGeVG41sW9yvEyTWIHXVSMqVprDV6PUJbkdAKLXLekW1NT5MT_1Z3Vy7m4pbf3lSyI4CuqBi2XLdF; SUHB=0mxkQvdVGbY0Nb; SCF=Au_O8r-aSPdhiIknzYsEKNQmLtHVyLkQDIZ0WeWOnR_qCTjuG1wPTgDY-a7RO39pfUQDh-LAo69Co5ip_xuxrAo.; SSOLoginState=1540123505; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803"}

    # Weibo类初始化
    def __init__(self, user_id, city_id, filter=0):
        self.user_id = user_id  # 用户id，即需要我们输入的数字，如昵称为“Dear-迪丽热巴”的id为1669879400
        self.city_id = city_id
        self.filter = filter  # 取值范围为0、1，程序默认值为0，代表要爬取用户的全部微博，1代表只爬取用户的原创微博
        self.username = ''  # 用户名，如“Dear-迪丽热巴”
        self.weibo_num = 0  # 用户全部微博数
        self.weibo_num2 = 0  # 爬取到的微博数
        self.following = 0  # 用户关注数
        self.followers = 0  # 用户粉丝数
        self.weibo_content = []  # 微博内容
        self.weibo_place = []  # 微博位置
        self.publish_time = []  # 微博发布时间
        self.up_num = []  # 微博对应的点赞数
        self.retweet_num = []  # 微博对应的转发数
        self.comment_num = []  # 微博对应的评论数
        self.publish_tool = []  # 微博发布工具
        self.headers = {
            "Host": "weibo.cn",
            "User-Agent": util.get_useragent_random(),
            # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "keep-alive"
        }

    def get_username(self):
        try:
            url = "https://weibo.cn/%s/info" % (self.user_id)
            html = requests.get(url, cookies=self.cookie).content
            selector = etree.HTML(html)
            username = selector.xpath("//title/text()")[0]
            self.username = username[:-3]
            log.debug("用户名: ", self.username)

        except Exception as e:
            log.debug("Error: ", e)
            traceback.print_exc()

    def get_user_info(self):
        try:
            url = "https://weibo.cn/u/%s?filter=%d&page=1" % (
                self.user_id, self.filter)
            html = requests.get(url, cookies=self.cookie, headers=self.headers).content
            selector = etree.HTML(html)
            pattern = r"\d+\.?\d*"

            # 微博数
            str_wb = selector.xpath(
                "//div[@class='tip2']/span[@class='tc']/text()")[0]
            guid = re.findall(pattern, str_wb, re.S | re.M)
            for value in guid:
                num_wb = int(value)
                break
            self.weibo_num = num_wb
            log.debug("微博数: ", str(self.weibo_num))

            # 关注数
            str_gz = selector.xpath("//div[@class='tip2']/a/text()")[0]
            guid = re.findall(pattern, str_gz, re.M)
            self.following = int(guid[0])
            log.debug("关注数: ", str(self.following))

            # 粉丝数
            str_fs = selector.xpath("//div[@class='tip2']/a/text()")[1]
            guid = re.findall(pattern, str_fs, re.M)
            self.followers = int(guid[0])
            log.debug("粉丝数: " + str(self.followers))
            log.debug("===========================================================================")

        except Exception as e:
            log.debug("Error: ", e)
            traceback.print_exc()

    # 获取"长微博"全部文字内容
    def get_long_weibo(self, weibo_link):
        try:
            html = requests.get(weibo_link, cookies=self.cookie).content
            selector = etree.HTML(html)
            info = selector.xpath("//div[@class='c']")[1]
            wb_content = info.xpath("div/span[@class='ctt']")[0].xpath(
                "string(.)").encode(sys.stdout.encoding, "ignore").decode(
                sys.stdout.encoding)
            img = info.xpath("div/a/img[@class='ib']")[0]
            img_link = ""
            if img is not None:
                img_link = img.xpath("@src")[0].encode(sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)
            wb_content = wb_content[1:]

            return (wb_content, img_link)
        except Exception as e:
            log.debug("Error: ", e)
            traceback.print_exc()
            return ("", "")

    # 获取用户微博内容及对应的发布时间、点赞数、转发数、评论数
    def get_weibo_info(self):
        try:
            url = "https://weibo.cn/u/%s?filter=%d&page=1" % (
                self.user_id, self.filter)
            html = requests.get(url, cookies=self.cookie).content
            selector = etree.HTML(html)
            if selector.xpath("//input[@name='mp']") == []:
                page_num = 1
            else:
                page_num = (int)(selector.xpath(
                    "//input[@name='mp']")[0].attrib["value"])
            pattern = r"\d+\.?\d*"
            for page in range(1, page_num + 1):
                Time.sleep(random.randint(4, 6))
                url2 = "https://weibo.cn/u/%s?filter=%d&page=%d" % (
                    self.user_id, self.filter, page)
                html2 = requests.get(url2, cookies=self.cookie).content
                selector2 = etree.HTML(html2)
                info = selector2.xpath("//div[@class='c']")
                is_empty = info[0].xpath("div/span[@class='ctt']")
                data_list = []
                if is_empty:
                    for i in range(0, len(info) - 2):
                        # 微博内容
                        str_t = info[i].xpath("div/span[@class='ctt']")
                        weibo_content = str_t[0].xpath("string(.)").encode(
                            sys.stdout.encoding, "ignore").decode(
                            sys.stdout.encoding)
                        weibo_content = weibo_content[:-1]
                        weibo_id = info[i].xpath("@id")[0][2:]
                        a_link = info[i].xpath(
                            "div/span[@class='ctt']/a/@href")
                        wb_long_content = None
                        if a_link:
                            if (a_link[-1] == "/comment/" + weibo_id or
                                                "/comment/" + weibo_id + "?" in a_link[-1]):
                                weibo_link = "https://weibo.cn" + a_link[-1]
                                wb_long_content = self.get_long_weibo(weibo_link)
                                if wb_long_content[0]:
                                    weibo_content = wb_long_content[0]
                        self.weibo_content.append(weibo_content)
                        log.debug("微博内容: " + weibo_content)

                        # attachment img
                        img_link = ""
                        if wb_long_content is None:
                            a_link = info[i].xpath("div/a/@href")
                            if len(a_link) != 0:
                                img_link = a_link[0]
                        else:
                            img_link = wb_long_content[1]
                        log.debug("微博img link: " + img_link)

                        # 微博位置
                        div_first = info[i].xpath("div")[0]
                        a_list = div_first.xpath("a")
                        weibo_place = u"无"
                        for a in a_list:
                            if ("http://place.weibo.com/imgmap/center" in a.xpath("@href")[0] and
                                        a.xpath("text()")[0] == u"显示地图"):
                                weibo_place = div_first.xpath(
                                    "span[@class='ctt']/a")[-1]
                                if u"的秒拍视频" in div_first.xpath("span[@class='ctt']/a/text()")[-1]:
                                    weibo_place = div_first.xpath(
                                        "span[@class='ctt']/a")[-2]
                                weibo_place = weibo_place.xpath("string(.)").encode(
                                    sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)
                                break
                        self.weibo_place.append(weibo_place)
                        log.debug("微博位置: " + weibo_place)

                        # 微博发布时间
                        str_time = info[i].xpath("div/span[@class='ct']")
                        str_time = str_time[0].xpath("string(.)").encode(
                            sys.stdout.encoding, "ignore").decode(
                            sys.stdout.encoding)
                        publish_time = str_time.split(u'来自')[0]
                        if u"刚刚" in publish_time:
                            publish_time = datetime.now().strftime(
                                '%Y-%m-%d %H:%M')
                        elif u"分钟" in publish_time:
                            minute = publish_time[:publish_time.find(u"分钟")]
                            minute = timedelta(minutes=int(minute))
                            publish_time = (
                                datetime.now() - minute).strftime(
                                "%Y-%m-%d %H:%M")
                        elif u"今天" in publish_time:
                            today = datetime.now().strftime("%Y-%m-%d")
                            _time = publish_time[3:]
                            publish_time = today + " " + _time
                        elif u"月" in publish_time:
                            year = datetime.now().strftime("%Y")
                            month = publish_time[0:2]
                            day = publish_time[3:5]
                            _time = publish_time[7:12]
                            publish_time = (
                                year + "-" + month + "-" + day + " " + _time)
                        else:
                            publish_time = publish_time[:16]
                        self.publish_time.append(publish_time)
                        log.debug("微博发布时间: " + publish_time)

                        # 微博发布工具
                        if len(str_time.split(u'来自')) > 1:
                            publish_tool = str_time.split(u'来自')[1]
                        else:
                            publish_tool = u"无"
                        self.publish_tool.append(publish_tool)
                        log.debug("微博发布工具: " + publish_tool)

                        str_footer = info[i].xpath("div")[-1]
                        str_footer = str_footer.xpath("string(.)").encode(
                            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)
                        str_footer = str_footer[str_footer.rfind(u'赞'):]
                        guid = re.findall(pattern, str_footer, re.M)

                        # 点赞数
                        up_num = int(guid[0])
                        self.up_num.append(up_num)
                        log.debug("点赞数: " + str(up_num))

                        # 转发数
                        retweet_num = int(guid[1])
                        self.retweet_num.append(retweet_num)
                        log.debug("转发数: " + str(retweet_num))

                        # 评论数
                        comment_num = int(guid[2])
                        self.comment_num.append(comment_num)
                        log.debug("评论数: " + str(comment_num))
                        log.debug("===========================================================================")

                        self.weibo_num2 += 1

                        data_list.append((weibo_content, img_link, publish_time))
                # DB data insert
                self.update_database(data_list)

            if not self.filter:
                log.debug("共" + str(self.weibo_num2) + u"条微博")
            else:
                log.debug("共" + str(self.weibo_num) + "条微博，其中" +
                      str(self.weibo_num2) + "条为原创微博"
                      )
        except Exception as e:
            log.debug("Error: ", e)
            traceback.print_exc()

    # a_tag_title, a_tag_href, publish_time
    def update_database(self, data):
        insertDB = DB(dbconfig())
        fetchDB = DB(dbconfig())
        insert = """INSERT INTO education(type, priority, title, url, create_time, update_time, hashcode, city_id) \
            VALUES ('1', 'm', '{}', '{}', '{}', '{}', '{}', '{}')"""
        fetch = """select * from education where hashcode='%s'"""

        dicts = []  # for mongo data
        reproduce_index = 0
        has_reproduce = False
        for (title, href, publish) in data:
            if has_reproduce:
                break
            t = Time.strftime("%Y-%m-%d", Time.localtime())
            publish_date = publish.strip()
            temp = """{},{}""".format(title, publish_date)
            hashcode = SHA().getSha512(temp)
            fetchScript = fetch % hashcode
            retult = fetchDB.get_existing_data(fetchScript)
            if retult is not None:
                reproduce_index += 1
                if reproduce_index == 3:
                    has_reproduce = True
                continue
            insertScript = insert.format(title, href, t, publish_date, hashcode, self.city_id)
            log.debug("insertScript is %s" % insertScript)
            try:
                insertDB.update_data(insertScript)
                log.debug("operation done")
            except Exception as e:
                log.debug("Error: ", e)
                traceback.print_exc()
            log.debug("insert data to mongo, prepare data")
            dicts.append(Moment(self.city_id, title, href, publish_date).get_dict())

        log.debug('data operation successfully')
        insertDB.close_connection()

        log.debug("insert data to mongo, start")
        try:
            if len(dicts) is not 0:
                nosql = nosqldb(nosqlconfig())
                nosql.insert_many("News", dicts)
        except Exception as e:
            log.debug("Error: ", e)
            traceback.print_exc()
        log.debug("insert data to mongo, end")

    # 将爬取的信息写入文件
    def write_txt(self):
        try:
            if self.filter:
                result_header = u"\n\n原创微博内容: \n"
            else:
                result_header = u"\n\n微博内容: \n"
            result = (u"用户信息\n用户昵称：" + self.username +
                      u"\n用户id: " + str(self.user_id) +
                      u"\n微博数: " + str(self.weibo_num) +
                      u"\n关注数: " + str(self.following) +
                      u"\n粉丝数: " + str(self.followers) +
                      result_header
                      )
            for i in range(1, self.weibo_num2 + 1):
                text = (str(i) + ":" + self.weibo_content[i - 1] + "\n" +
                        u"微博位置: " + self.weibo_place[i - 1] + "\n" +
                        u"发布时间: " + self.publish_time[i - 1] + "\n" +
                        u"点赞数: " + str(self.up_num[i - 1]) +
                        u"	 转发数: " + str(self.retweet_num[i - 1]) +
                        u"	 评论数: " + str(self.comment_num[i - 1]) + "\n"
                                                                       u"发布工具: " + self.publish_tool[i - 1] + "\n\n"
                        )
                result = result + text
            file_dir = os.path.split(os.path.realpath(__file__))[
                           0] + os.sep + "weibo"
            if not os.path.isdir(file_dir):
                os.mkdir(file_dir)
            file_path = file_dir + os.sep + "%d" % self.user_id + ".txt"
            f = open(file_path, "wb")
            f.write(result.encode(sys.stdout.encoding))
            f.close()
            log.debug("微博写入文件完毕，保存路径:")
            log.debug(file_path)
        except Exception as e:
            log.debug("Error: ", e)
            traceback.print_exc()

    # 运行爬虫
    def start(self):
        try:
            # self.get_username()
            # self.get_user_info()
            self.get_weibo_info()
            # self.write_txt()
            log.debug("信息抓取完毕")
            log.debug("===========================================================================")
        except Exception as e:
            log.debug("Error: ", e)


def main():
    # https://m.weibo.cn/u/2608649530
    try:
        # 使用实例,输入一个用户id，所有信息都会存储在wb实例中
        user_id = 2608649530  # 可以改成任意合法的用户id（爬虫的微博id除外）
        filter = 0  # 值为0表示爬取全部微博（原创微博+转发微博），值为1表示只爬取原创微博
        city_id = 1
        wb = Weibo(user_id, city_id, filter)  # 调用Weibo类，创建微博实例wb
        wb.start()  # 爬取微博信息
        log.debug("用户名: " + wb.username)
        log.debug("全部微博数: " + str(wb.weibo_num))
        log.debug("关注数: " + str(wb.following))
        log.debug("粉丝数: " + str(wb.followers))
        if wb.weibo_content:
            log.debug("最新/置顶 微博为: " + wb.weibo_content[0])
            log.debug("最新/置顶 微博位置: " + wb.weibo_place[0])
            log.debug("最新/置顶 微博发布时间: " + wb.publish_time[0])
            log.debug("最新/置顶 微博获得赞数: " + str(wb.up_num[0]))
            log.debug("最新/置顶 微博获得转发数: " + str(wb.retweet_num[0]))
            log.debug("最新/置顶 微博获得评论数: " + str(wb.comment_num[0]))
            log.debug("最新/置顶 微博发布工具: " + wb.publish_tool[0])
    except Exception as e:
        log.debug("Error: ", e)
        traceback.print_exc()


if __name__ == "__main__":
    main()
