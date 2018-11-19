# -*- coding:utf8 -*-

class Moment(object):
    def __init__(self, cityId, message, link, createTime):
        self._cityId = cityId
        self._message = message
        self._link = link
        self._createTime = createTime

    def get_dict(self):
        return {
            "cityId": self._cityId,
            "message": self._message,
            "link": self._link,
            "createTime": self._createTime
        }
