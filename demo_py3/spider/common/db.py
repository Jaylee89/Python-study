# !/usr/bin/python3
# -*- coding:utf8 -*-

import pymysql
import spider.common.log as log
from spider.config.config import DBConfig as dbconfig

class DB(dbconfig):
    def __init__(self, dbconfig):
        self.__config = dbconfig.get_config()
        self.__db = pymysql.connect(host=self.__config[0], user=self.__config[1], password=self.__config[2], database=self.__config[3], port=self.__config[4], connect_timeout=20)
        self.__cursor = self.__db.cursor()

    def close_connection(self):
        self.__db.close()
        self.__cursor.close()

    def update_data(self, sql):
        try:
            self.__cursor.execute(sql)
            self.__db.commit()
            print("self.__db.commit() done")
            log.debug("commit done")
        except:
            print("self.__db.commit() have except")
            log.debug("have except")
            self.__db.rollback()
    def get_existing_data(self, sql):
        data = None
        try:
            self.__cursor.execute(sql)
            data = self.__cursor.fetchone()
            print("get_existing_data method, data is ", data)
            log.debug("commit done")
            return data
        except:
            print("self.__db.commit() have except")
            log.debug("have except")
            self.__db.rollback()