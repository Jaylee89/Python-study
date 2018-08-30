#!/usr/bin/env python
# -*- coding: utf8 -*-


#https://docs.python.org/2/howto/regex.html#repeating-things
#http://www.cnblogs.com/chuxiuhong/p/5885073.html
#http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

import re

key = r"<html><body><h1>hello world</h1></body></html>"#这段是你要匹配的文本
p1 = r"(?<=<h1>).+?(?=</h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern1 = re.compile(p1)#我们在编译这段正则表达式
matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
print matcher1.group(0)#打印出来



key = r"javapythonhtmlvhdl"#这是源文本
p1 = r"python"#这是我们写的正则表达式
pattern1 = re.compile(p1)#同样是编译
matcher1 = re.search(pattern1,key)#同样是查询
print matcher1.group(0)

key = r"chuxiuhong@hit.edu.cn"
p1 = r"@.+?\."#我想匹配到@后面一直到“.”之间的，在这里是hit
pattern1 = re.compile(p1)
print pattern1.findall(key)

key = r"saas and sas and saaas"
p1 = r"sa{1,2}s"
pattern1 = re.compile(p1)
print pattern1.findall(key)
