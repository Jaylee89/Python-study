#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "Jaylee"


import logging

filename = 'autolog.log'

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename=filename,
    filemode='w')


#DEBUG----0
#INFO-----1
#WARN-----2
#ERROR----3
#CRITICAL-4

# 第一步，创建一个logger  
#logger = logging.getLogger()
#def setUp(self, level):
#logger.setLevel(logging.INFO)    # Log等级总开关  
  
# 第二步，创建一个handler，用于写入日志文件  
#logfile = 'autolog.log'  
#fh = logging.FileHandler(logfile, mode='w')  
#fh.setLevel(logging.DEBUG)   # 输出到file的log等级的开关  
  
# 第三步，再创建一个handler，用于输出到控制台  
#ch = logging.StreamHandler()  
#ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关  
  
# 第四步，定义handler的输出格式  
#formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")  
#fh.setFormatter(formatter)  
#ch.setFormatter(formatter)  
  
# 第五步，将logger添加到handler里面  
#logger.addHandler(fh)  
#logger.addHandler(ch)  

# 日志
#logger.debug('this is a logger debug message')  
#logger.info('this is a logger info message')  
#logger.warning('this is a logger warning message')  
#logger.error('this is a logger error message')  
#logger.critical('this is a logger critical message')

from logging.handlers import RotatingFileHandler

#################################################################################################
#定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
Rthandler = RotatingFileHandler(filename, maxBytes=10*1024*1024,backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)
################################################################################################

def debug(info):
	logging.debug(info)