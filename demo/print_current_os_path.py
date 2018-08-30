#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import re
import logging
from sys import argv
logging.basicConfig(level=logging.DEBUG)


def print_path(a_str, a_dir=os.path.abspath('.')):
    _file = [x for x in os.listdir(a_dir) if os.path.isfile(os.path.join(a_dir,x))]
    logging.DEBUG('_file is-->', _file)
    for i in _file:
        if re.search(a_str, i):
            print os.path.join(a_dir, i)
    _dir = [x for x in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, x))]
    if _dir == []:
        return 0
    for i in _dir:
        sub_dir = os.path.join(a_dir, i)
        print_path(a_str, sub_dir)


#this file has issue, will handle next time
if __name__ == '__main__':

    a_str = argv
    print a_str
    logging.DEBUG('a_str is -->%d', len(a_str)
    print_path(a_str)