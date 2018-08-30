__author__ = 'davidzhang'
# -*- coding: UTF-8 -*-

import os

class Config(object):
    # 配置
    DATABASE='sqlite:////tmp/app.db'
    LOGGER_FILE='/tmp/logger.log'
    DEBUG=False
    TESTING=False
    SECRET_KEY="z\xe5v\xf1'\xde\x99\xa3P|\xa8 \xe1\xd25op\xdd\xe96\r\xd3\xb7o"
    USERNAME='admin'
    PASSWORD='default'
    ADMINS= ['zhangdapeng89@126.com']
    
    MONGO_HOST='127.0.0.1'
    MONGO_PORT=27017
    MONGO_DBNAME='qeeniao'

    MYSQL_HOST='127.0.0.1'
    MYSQL_USER='qeeniao'
    MYSQL_PASS='123456'
    MYSQL_DB='qeeniao'
    

    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/app.db'
    SQLALCHEMY_BINDS={
        'qeeniao_mysql':'mysql+mysqldb://root:''@127.0.0.1/qeeniao?charset=utf8'
    }
 
    # 文件上传配置
    UPLOAD_FOLDER= os.path.join(os.path.dirname(__file__),'static/uploads')
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

class ProductionConfig(Config):
    
    pass

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True