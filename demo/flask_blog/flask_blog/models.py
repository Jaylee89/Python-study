__author__ = 'davidzhang'
# -*- coding:utf-8 -*-

from sqlalchemy import Column,Integer,String
from flask_blog.database import db

class User(db.Model):
    __bind_key__ = 'qeeniao_mysql'
    __tablename__='users'
    id = db.Column(Integer,primary_key=True)
    name = db.Column(String(100),unique=True)
    email = db.Column(String(200),unique=True)

    def __init__(self,name=None,email=None):
        self.name = name
        self.email = email


    def __repr__(self):
        return '<User %r>' % (self.name)

class Itunes(db.Model):
    __bind_key__='qeeniao_mysql'
    __tablename__='itunes'

    id = db.Column(Integer,primary_key=True)
    url = db.Column(String(200),unique=False)
    title = db.Column(String(200),unique=False)
    create_time = db.Column(String(100),unique=False)
    
    def __init__(self,url=None,title=None,create_time=None):
        self.url = url
        self.title = title
        self.create_time = create_time
        
    def __repr__(self):
        return '<Itunes %r>' % (self.title)

class Entries(db.Model):
    __bind_key__ = 'qeeniao_mysql'
    __tablename__='entries'
    id = db.Column(Integer,primary_key=True)
    title = db.Column(String(100),unique=True)
    text = db.Column(String(200),unique=True)

    def __init__(self,title,text):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<Entries %r>' % (self.title)