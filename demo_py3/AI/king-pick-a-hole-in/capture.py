import time, os
from PIL import Image
import shutil

start = time.time()
# os.system("adb shell /system/bin/screencap -p /sdcard/1/1.png")
# os.system("adb pull /sdcard/1/1.png ./imgs/1.png")


screenshot_backup_dir = 'imgs/backups/'
if not os.path.isdir(screenshot_backup_dir):
    os.mkdir(screenshot_backup_dir)

start = time.time()

im = Image.open('./imgs/1.png')

img_size = im.size
w = im.size[0]
h = im.size[1]
print("image's w*h:{}".format(img_size))

#region = im.crop((70,300, w-70,700))    #裁剪的区域
region = im.crop((20,305, w-20,955))    #裁剪的区域
region.save('./imgs/up.png')

region = im.crop((20,987, w-20,1637))    #裁剪的区域
region.save('./imgs/down.png')

end = time.time()

print('程序用时：'+str(end-start)+'秒')
def backup_screenshot(ts):
    # 为了方便失败的时候 debug
    if not os.path.isdir(screenshot_backup_dir):
        os.mkdir(screenshot_backup_dir)
    shutil.copy('./imgs/1.png', '{}{}.png'.format(screenshot_backup_dir, ts))
backup_screenshot(int(end))