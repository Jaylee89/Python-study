#!/usr/bin/env python
# -*- coding: utf8 -*-

import urllib
import sys
import re

if __name__ == '__main__':
    if len(sys.argv) > 1:
        str = sys.argv[1]
        str = unicode(str, 'gbk')
    else:  
        #str = u"中文"
        #str = u'\u8001\u5e08\u7206\u7b11\u5410\u69fd\u5b66\u751f\u53bb\u98df\u5802\uff0c\u8bf4\u7684\u662f\u4e0d\u662f\u5f53\u5e74\u7684\u4f60\uff1f'
        str = u'\\u8001\\u5e08\\u7206\\u7b11'.replace('\\\\', '\\')
        print str.encode("UTF-8")
    print u'%s' % str
    params = {}
    params['name'] = str.encode("UTF-8")
    print urllib.urlencode(params)
