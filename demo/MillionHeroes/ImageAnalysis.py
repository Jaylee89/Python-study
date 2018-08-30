#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aip import AipOcr 

import json

# 定义常量 
APP_ID ='9851066'
API_KEY ='LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY ='fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

# 初始化AipFace对象 
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY) 


# 读取图片 
filePath ="crop_test1.png"

def get_file_content(filePath): 
    with open(filePath,'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
	'detect_direction': 'true',
	'language_type': 'CHN_ENG'
}



# 调用通用文字识别接口 
#result = aipOcr.basicGeneral(get_file_content(filePath), options)
result = aipOcr.general(get_file_content(filePath), options)

#result = {"log_id": 6417925948223622503, "direction": 0, "words_result_num": 2, "classify_result": {"lottery": "unknown"}, "words_result": [{"location": {"width": 869, "top": 214, "left": 29, "height": 57}, "words": u"2.一杯糖水喝掉一半后,糖水的密度"}, {"location": {"width": 207, "top": 289, "left": 366, "height": 55}, "words": u"变化是?"}]

#, ensure_ascii=False
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 187-195: ordinal not in range(128)
# json_data = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')).decode("unicode-escape")

# "words": "\u53d8\u5316\u662f?"
# json_data = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))

json_data = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)


print json_data
#final_result = "".join(json_data["words_result"]["words"])
array1 = []
#data = json_data["words_result"]
data = json.loads(json_data)["words_result"]

for obj in data:
    #final_result += obj["words"]
    #final_result.join(obj["words"])
    array1.append(obj["words"])
print array1
final_result = "".join(array1)
print "final result is %s" % final_result

"""
{
	"log_id": 6417925948223622503,
	"direction": 0,
	"words_result_num": 2,
	"classify_result": {
		"lottery": "unknown"
	},
	"words_result": [{
		"location": {
			"width": 869,
			"top": 214,
			"left": 29,
			"height": 57
		},
		"words": "2.一杯糖水喝掉一半后,糖水的密度"
	},
	{
		"location": {
			"width": 207,
			"top": 289,
			"left": 366,
			"height": 55
		},
		"words": "变化是?"
	}]
}

"""

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input