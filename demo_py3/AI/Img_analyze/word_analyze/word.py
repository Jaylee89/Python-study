#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aip import AipOcr
import json
import win32com.client as wincl
from tkinter import *

APP_ID = '14433219'
API_KEY = 'uh1SnFZ2AvvCLcUxkR4VOkYk'
SECRET_KEY = 'PFxBMIfajiHGCtsG5NWuXWcwUhEGUvSu'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('微信图片_20181014164817.jpg')

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
resp = client.basicGeneral(image, options)

json_data = json.dumps(resp, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
print("json_data is", json_data)
data = json.loads(json_data)

titles = data['words_result']          #获取问题
ans = ''
for title in titles:
    ans = ans + title['words']

def text2Speech(text):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)

print("ans is ", ans)
if ans is not '':
    text2Speech(ans)