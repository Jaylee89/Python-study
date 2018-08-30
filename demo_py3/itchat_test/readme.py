
#https://www.cnblogs.com/jiaoyu121/p/6944398.html

#how to transfer between list and str:
list3 = ['www', 'google', 'com']
".".join(list3)

str2 = 'www.baidu.com'
str2.split('.')

import json

with open('json.data', 'r') as f:
    data = json.load(f)

print(data)

json_data = {"name": 'Runoob', 'no': 1, 'url': 'http://www.runoob.com'}
with open('data.json', 'w') as f:
    json.dump(data, f)

#将数据解码为json或者将json转成dict
#json.dumps
#json.loads

#对文件的操作
#json.dump
#json.load