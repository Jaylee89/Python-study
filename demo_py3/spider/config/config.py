#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3

class DBConfig():
    def __init__(self):
        self.__address = "gz-cdb-mwf6t4r1.sql.tencentcdb.com"
        self.__port = 62214
        self.__username = "root"
        self.__password = "P@ssw0rd@"
        self.__db_name = "spider"

    def get_config(self):
        return [self.__address, self.__username, self.__password, self.__db_name, self.__port]

