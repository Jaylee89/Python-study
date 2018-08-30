#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itchat, logging
from json import dumps, load

logging.basicConfig(level=logging.DEBUG)

#write json to file, not complete
file_name = "GenderStatistics_result"

def print_log_in_file(log):
    with open(file_name, 'a') as file_to_write:
        #file_to_write.write(log.encode('utf-8') + "\n") #os.linesep
        #file_to_write.write(log + "\n")  # os.linesep
        #file_to_write.write(dumps(log, file_to_write, indent=4))
        file_to_write.write(r"\n".join(log))
        file_to_write.close()

# 先登录
itchat.login()

# 获取好友列表
friends = itchat.get_friends(update=True)[0:]

print(r"friends is \n", friends)
print_log_in_file(friends)

# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0

# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# 1表示男性，2女性
for i in friends[1:]: #first one is self
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1


# 总数算上，好计算比例啊～
total = len(friends[1:])

# 好了，打印结果
print(u"男性好友：%.2f%%" % (float(male) / total * 100))
print(u"女性好友：%.2f%%" % (float(female) / total * 100))
print(u"其他：%.2f%%" % (float(other) / total * 100))

from pyecharts import Pie

attr = ["男", "女", "其它"]
va = [male, female, other]

pie = Pie("男女比例分配")
pie.add("", attr, va, is_label_show = True)
pie.render()

# result
"""
男性好友：56.08%
女性好友：35.81%
其他：8.11%
"""

#http://localhost:63342/demo_py3/itchat_test/render.html?_ijt=3tcdq45bnp1hec7rduk8c9j4sc
itchat.logout()