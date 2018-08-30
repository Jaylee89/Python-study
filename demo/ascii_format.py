#hello.py
#!/usr/bin/env python
# _*_ coding: utf8 _*_
# _*_ coding: gb2312 _*_
# _*_ coding: gbk _*_ //向下兼容gb2312

print u'中文测试'

print '中文测试2'

print unicode("汉字","utf8")

# print unicode("汉字","gb2312")

print '汉字'.encode("hex")