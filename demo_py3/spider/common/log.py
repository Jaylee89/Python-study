#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Level	Numeric Value    Function	Used to
CRITICAL	50	logging.critical()	Show a serious error, the program may be unable to continue running
ERROR	    40	logging.error()	    Show a more serious problem
WARNING	    30	logging.warning()	Indicate something unexpected happened, or could happen
INFO	    20	logging.info()	    Confirm that things are working as expected
DEBUG	    10	logging.debug()	    Diagnose problems, show detailed information
"""

import logging
from logging.handlers import RotatingFileHandler

filename = './autolog.log'

#logging.basicConfig(level=logging.DEBUG) #print log in console
#logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename=filename,
    filemode='w')

Rthandler = RotatingFileHandler(filename, maxBytes=10*1024*1024,backupCount=5, encoding="utf-8")
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)

def debug(info):
	logging.debug(info)

def info(info):
	logging.info(info)