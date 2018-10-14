#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import urllib.request
import importlib, sys #, base64
import json, io, os, time, baiduSearch
from PIL import Image
import shutil
import subprocess

from aip import AipOcr

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
importlib.reload(sys)

screenshot_backup_dir = 'screenshot_backups2/'
if not os.path.isdir(screenshot_backup_dir):
    os.mkdir(screenshot_backup_dir)

start = time.time()
def pull_screenshot2():
    screencap = "adb shell screencap -p /sdcard/screenshot.png"
    pull = r"adb pull /sdcard/screenshot.png ./screenshot2.png"
    process = subprocess.Popen(screencap, shell=True)
    time.sleep(2)
    close_process(process, 0.1)
    process2 = subprocess.Popen(pull, shell=True)
    time.sleep(1)
    close_process(process2, 0.2)

def close_process(process, i):
    if process.stdin:
        process.stdin.close()
    if process.stdout:
        process.stdout.close()
    if process.stderr:
        process.stderr.close()
    try:
        process.kill()
    except OSError:
        pass
    print('%s================close================%s' % (str(i), str(i)))

# pull_screenshot2()

'''
汉王ocr 涨价涨价了。。
host = 'http://text.aliapi.hanvon.com'
path = '/rt/ws/v1/ocr/text/recg'
method = 'POST'
appcode = 'a962e94260ee4043b824d2f40c126d8e'    #汉王识别appcode（填你自己的）
querys = 'code=74e51a88-41ec-413e-b162-bd031fe0407e'
bodys = {}
url = host + path + '?' + querys
'''
""" （百度ocr）你的 APPID AK SK """
APP_ID = '10673785'
API_KEY = 'FqRvrpPwhSNXt2FhT6d3dXfc'
SECRET_KEY = 'UIu2qOPHXENScjr1yzAyXQgNkLQzkcdc'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

options = {
	'detect_direction': 'true',
	'language_type': 'CHN_ENG'
}

# im = Image.open(r"./微信图片_20181014164817.jpg")
im = Image.open(r"./screenshot.png")

img_size = im.size
w = im.size[0]
h = im.size[1]
# print("image's w*h:(%d, %d)".format(img_size))

#region = im.crop((70,300, w-70,700))    #裁剪的区域
# region = im.crop((70,600, w-70,900))    #裁剪的区域
region = im.crop((0,0,w,h))
region.save(r"./crop_test2.png")



""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content(r"./crop_test2.png")
#respon = client.basicGeneral(image)   #用完500次后可改respon = client.basicAccurate(image)
options["mask"] = image
respon = client.general(image, options)
json_data = json.dumps(respon, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
print("json_data is", json_data)
data = json.loads(json_data)

titles = data['words_result']          #获取问题
ans = ''
for title in titles:
    ans = ans + title['words']
#ans = ans.encode("utf-8")
#ans = ans.decode("unicode-escape")
#tissue = ans[1:2]
#if str.isdigit(tissue):            #去掉题目索引
#     ans = ans[3:]
#else:
#     ans = ans[2:]

print(ans)       #打印问题

keyword = ans    #识别的问题文本

convey = 'n'

if convey == 'y' or convey == 'Y':
    results = baiduSearch.search(keyword, convey=True)
elif convey == 'n' or convey == 'N' or not convey:
    results = baiduSearch.search(keyword)
else:
    print('输入错误')
    exit(0)
count = 0
for result in results:
    #print('{0} {1} {2} {3} {4}'.format(result.index, result.title, result.abstract, result.show_url, result.url))  # 此处应有格式化输出
	print('{0}'.format(result.abstract))  # 此处应有格式化输出
	count=count+1
	if(count == 2):      #这里限制了只显示2条结果，可以自己设置
		break

end = time.time()
print('程序用时：'+str(end-start)+'秒')
def backup_screenshot(ts):
    # 为了方便失败的时候 debug
    if not os.path.isdir(screenshot_backup_dir):
        os.mkdir(screenshot_backup_dir)
    shutil.copy('screenshot2.png', '{}{}.png'.format(screenshot_backup_dir, ts))
backup_screenshot(int(end))
