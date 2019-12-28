"""
reference doc: https://www.jianshu.com/p/ca343a441e6d
"""
import cv2
import imutils
# DEPRECATED: skimage.measure in version 0.18 and previously.
# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as compare_ssim
from datetime import datetime

image1 = cv2.imread('imgs/l1.jpeg')
image2 = cv2.imread('imgs/r1.jpeg')

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(gray1, gray2, full=True)
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
cv2.imwrite('imgs/result-%d.jpeg' % datetime.now().timestamp(), image2)
cv2.waitKey(0)