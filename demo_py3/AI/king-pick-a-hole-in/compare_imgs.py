"""
reference doc: https://www.jianshu.com/p/ca343a441e6d
"""
import cv2
import imutils
# DEPRECATED: skimage.measure in version 0.18 and previously.
# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as compare_ssim
import shutil, time, os
from PIL import Image

def backup_screenshot(name, backup_dir, ts):
    shutil.copy('./imgs/%s.png' % name, '{}{}.png'.format(backup_dir, ts))

"""
========capture imgs start========
"""

start = time.time()
os.system("adb shell /system/bin/screencap -p /sdcard/1/1.png")
os.system("adb pull /sdcard/1/1.png ./imgs/1.png")

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

end1 = time.time()

"""
========capture imgs end========
"""

screenshot_backup_dir_diff = 'imgs/backups/diff/'
if not os.path.isdir(screenshot_backup_dir_diff):
    os.mkdir(screenshot_backup_dir_diff)

image1 = cv2.imread('./imgs/up.png')
image2 = cv2.imread('./imgs/down.png')

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(gray2, gray1, full=True)
diff = (diff * 255).astype('uint8')
print('SSIM: {}'.format(score))

thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# solution in https://www.jianshu.com/p/f7930023dc62
# cnts = cnts[0] if imutils.is_cv2() else cnts[1] #opencv_image 2
cnts = cnts[1] if imutils.is_cv3() else cnts[0] #opencv_image 2

for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(image1, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.rectangle(image2, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('Modified: ', image2)
cv2.imwrite('imgs/diff.png', image2)
next=cv2.waitKey(0)

end2 = time.time()

print('程序用时：'+str(end2-start)+'秒')
if next == 110: #if type 'n' means 'next', will store diff file
    backup_screenshot('1', screenshot_backup_dir, int(end1))
    backup_screenshot('diff', screenshot_backup_dir_diff, int(end2))