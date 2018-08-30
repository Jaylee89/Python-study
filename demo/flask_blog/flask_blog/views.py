__author__ = 'davidzhang'
# -*- coding: UTF-8 -*-

from flask_blog import app
from flask import url_for

#导入控制器
from controller import Entries
from controller import Default
from controller import User
from controller import Post
from controller import Spider
from controller.admin import Default as AdminDefault

#路由控制
app.add_url_rule('/','index',Default.index)
app.add_url_rule('/entries','show_entries',Entries.index)
app.add_url_rule('/add','add_entry',Entries.add_entry)
app.add_url_rule('/login/','login',Default.login)
app.add_url_rule('/login/','logout',Default.logout)
app.add_url_rule('/user/','user',User.index)
app.add_url_rule('/user/','post',Post.index,defaults={'page':'index'})
app.add_url_rule('/itunes','spider_itunes',Spider.itunes)
app.add_url_rule('/apple','spider_apple',Spider.apple)

app.add_url_rule('/admin','admin',AdminDefault.index)