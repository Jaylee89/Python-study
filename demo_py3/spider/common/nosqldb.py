# !/usr/bin/python3
# -*- coding:utf8 -*-

import pymongo
import common.log as log
from config.config import NoSQLConfig as nosqlconfig


class NoSqlDB(nosqlconfig):
    def __init__(self, nosqlconfig):
        self.__config = nosqlconfig.get_config()
        self.__client = pymongo.MongoClient(("%s" % (self.__config[0])), self.__config[4])
        self.__db = self.__client[self.__config[3]]

    def get_db_obj(self):
        return self.__db

    def get_client_obj(self):
        return self.__client

    def insert_one(self, *args, **kwargs):
        topic = self.get_db_obj()[args[0]]
        result = None
        if len(kwargs) is 0:
            return None
        try:
            r = topic.insert_one(kwargs)
            result = r.inserted_ids
            print("insert_one -> result is %d" % result)
        except:
            print("insert_one have except")
            log.debug("have except")
        finally:
            return result

    def insert_many(self, *args):
        topic = self.get_db_obj()[args[0]]
        result = None
        if len(args[1]) is 0:
            return None
        try:
            r = topic.insert_many(args[1])
            result = r.inserted_ids
            log.debug("insert_many -> result is %d" % result)
        except:
            log.debug("insert_many have except")
            log.debug("have except")
        finally:
            return result

    def fetch_collections(self, *args, **kwargs):
        """
        :param args: topic
        :return: array
        :sort: .sort("alexa"), .sort("alexa", -1)
        :condiftional:
            1. return special col, { "_id": 0, "name": 1, "alexa": 1 }
            2. search special col, { "name": "RUNOOB" }
            3. $gt, { "name": { "$gt": "H" } }
            4. $regex, { "name": { "$regex": "^R" } }
        """
        topic = self.get_db_obj()[args[0]]
        array_list = []
        if kwargs is not None:
            limit = kwargs.get("limit") if kwargs.get("limit") is not None else 1000
        try:
            if kwargs is None:
                result = topic.find().limit(limit)
                if isinstance(result, []) is not True:
                    array_list.append(result)
                for x in result:
                    log.debug("fetch_collections -> one of data -> ", x)
            else:
                array_list = topic.find().limit(limit)
        except:
            log.debug("fetch_collections have except")
            log.debug("have except")
        finally:
            return array_list

    def update_many(self, *args, **kwargs):
        """
        :param args:  topic
        :param kwargs:  query and new
        :return:
        : conditional
            1. query: { "$get": { "alexa": "10000" } }
               new:   { "$set": { "$set": { "alexa": "12345" } } }
        """
        topic = self.get_db_obj()[args[0]]
        is_change = False
        try:
            # topic.update_one(kwargs["$get"], "$set")
            topic.update_many(kwargs["$get"], "$set")
            is_change = True
        except:
            is_change = False
            log.debug("update_many have except")
            log.debug("have except")
        finally:
            return is_change

    def delete_many(self, *args, **kwargs):
        """
        :param args:  topic
        :param kwargs:  query and new
        :return:
        : conditional
            1. query: { { "alexa": "10000" } }
        """
        topic = self.get_db_obj()[args[0]]
        is_delete = False
        try:
            # topic.update_one(kwargs["$get"], "$set")
            result = topic.delete_many(kwargs)
            log.debug("delete_many -> result is %d" % result.deleted_count)
            is_delete = True
        except:
            is_delete = False
            log.debug("delete_many have except")
            log.debug("have except")
        finally:
            return is_delete


if __name__ == "__main__":
    nosql = NoSqlDB(nosqlconfig())
    client = nosql.get_client_obj()
    dblist = client.list_database_names()
    for it in dblist:
        log.debug("database name is %s" % it)
    db = nosql.get_db_obj()
    # dicts = [{'cityId': 1, 'message': '广州市教育局转发关于严禁商业广告、商业活动进入中小学校和幼儿园的紧急通知', 'link': 'http://www.gzedu.gov.cn/gzsjyj/tzgg/201811/7e4f759a3c8949d4b5dcad90e0be5c56.shtml', 'createTime': '2018-11-15'}]
    # nosql.insert_many("News", dicts)
    collist = db.list_collection_names()
    for col in collist:
        log.debug("collects name is %s" % col)
        array = nosql.fetch_collections(col, {})
        for data in array:
            log.debug("col is {}, data is ".format(col), data)
