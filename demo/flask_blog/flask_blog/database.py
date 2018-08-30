__author__ = 'davidzhang'
# -*- coding:utf-8 -*-

from flask_blog import app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask.ext.pymongo import PyMongo
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# MongoDB链接
mongo = PyMongo(app,config_prefix='MONGO')

def init_db():
    import flask_blog.models
    Base.metadata.create_all(bind=engine)