#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3

"""
Level	Numeric Value    Function	Used to
CRITICAL	50	logging.critical()	Show a serious error, the program may be unable to continue running
ERROR	    40	logging.error()	    Show a more serious problem
WARNING	    30	logging.warning()	Indicate something unexpected happened, or could happen
INFO	    20	logging.info()	    Confirm that things are working as expected
DEBUG	    10	logging.debug()	    Diagnose problems, show detailed information
"""

import logging

#logging.basicConfig(level=logging.DEBUG) #print log in console
#logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logging.debug("Pizza created: {} (${})".format(self.name, self.price))

    def make(self, quantity=1):
        logging.debug("Made {} {} pizza(s)".format(quantity, self.name))

    def eat(self, quantity=1):
        logging.debug("Ate {} pizza(s)".format(quantity, self.name))

# Modify the parameters of the pizza_01 object
pizza_01 = Pizza("Sicilian", 18)
pizza_01.make(5)
pizza_01.eat(4)

# Modify the parameters of the pizza_02 object
pizza_02 = Pizza("quattro formaggi", 16)
pizza_02.make(2)
pizza_02.eat(2)