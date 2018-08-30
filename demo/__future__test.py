#__future__.py
#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import unicode_literals
from __future__ import division
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

from __future__ import unicode_literals
from datetime import datetime

now = datetime.now()
print now.strftime(u'%m月%d日 %H:%M')

#从Python 2.7到Python 3.x就有不兼容的一些改动，比如2.x里的字符串用'xxx'表示str，Unicode字符串用u\'xxx'表示unicode，
#而在3.x中，所有字符串都被视为unicode，因此，写u\'xxx'和'xxx'是完全一致的，而在2.x中以'xxx'表示的str就必须写成b'xxx'，以此表示“二进制字符串

#在Python 3.x中，所有的除法都是精确除法，地板除用//表示

#from __future__ import unicode_literals
#from __future__ imports must occur at the beginning of the file

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'你好\' is unicode?', isinstance(u'你好', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

#在Python 2.7的代码中直接使用Python 3.x的除法，可以通过__future__模块的division实现

#from __future__ import division
#from __future__ imports must occur at the beginning of the file

print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3
