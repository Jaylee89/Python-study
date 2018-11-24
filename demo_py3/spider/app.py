# -*- coding:utf8 -*-

# import importlib, sys, os, io
from functions.education.Education import Education
from functions.weibo.Weibo import Weibo
from lib.SpiderThread import SpiderThread

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# importlib.reload(sys)

def get_education_start(url, id):
    Education(url, id).start()

def get_weibo_start(url, id):
    Weibo(url, id).start()


if __name__ == "__main__":
    import common.util as util
    import common.log as log
    json = util.load_json("cities.json")
    threads = []
    for city in json["cities"]:
        name, id, websites = city["name"], city["id"], city["websites"]
        log.debug("name is {}, id is {}".format(name, id))
        for website in websites:
            type, url = website["type"], website["url"]
            if "education" == type:
                threads.append(SpiderThread(get_education_start, url, id, name = type))
            elif "weibo" == type:
                threads.append(SpiderThread(get_weibo_start, url, id, name = type))

    len = range(len(threads))
    for i in len:
        threads[i].start()
    for i in len:
        threads[i].join()