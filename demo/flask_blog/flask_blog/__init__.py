#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
from contextlib import closing

#Import Configuration
from flask_blog import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

#=======================SQLite数据库配置=========================#
# def init_db():
#     with closing(connect_db()) as db:
#         with app.open_resource("schema.sql",mode="r") as f:
#             db.cursor().executescript(f.read())
#         db.commit()
#
# def connect_db():
#     return sqlite3.connect(app.config['DATABASE'])
#
# @app.before_request
# def before_request():
#     g.db = connect_db()
#
# @app.teardown_request
# def teardown_request(exception):
#     db = getattr(g,'db',None)
#     if db is None:
#         db.close()
#     g.db.close()

from flask_blog.database import db
@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
    
#=======================邮件日志=========================#
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    from logging import Formatter
    mail_handler = SMTPHandler('127.0.0.1',
                               'zhangdapeng89@126.com',
                               app.config['ADMINS'],
                               'Your Application Error!')
    mail_handler.setFormatter(Formatter('''
    Message type:       %(levelname)s
    Location:           %(pathname)s:%(lineno)d
    Module:             %(module)s
    Function:           %(funcName)s
    Time:               %(asctime)s

    Message:

    %(message)s
    '''))
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

#=======================日志文件=========================#
if not app.debug:
    import logging
    from logging.handlers import WatchedFileHandler
    from logging import Formatter
    file_handler = WatchedFileHandler(app.config['LOGGER_FILE'])
    file_handler.setFormatter(Formatter('''
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
    '''))
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

#=======================订阅信号=========================#
from flask import template_rendered
from contextlib import contextmanager

@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender,template,context,**extra):
        recorded.append((template,context))

    template_rendered.connect(record,app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record,app)


#=======================视图程序逻辑=======================#
import flask_blog.views
    
#=======================注册过滤器=========================#
import flask_blog.filter

#=======================静态资源管理器======================#
import flask_blog.assets

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3031,debug=True)