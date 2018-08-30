#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = 'davidzhang'

from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
from flask_blog.models import Entries
from flask_blog.database import db

def index():
    entries = [dict(title=row.title,text=row.text) for row in Entries.query.all()]
    return render_template('front/show_entries.html',entries=entries)
index.provide_automatic_options = False
index.methods = ['GET', 'OPTIONS']
    
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    entries_insert_data = Entries(request.form['title'],request.form['text'])
    db.session.add(entries_insert_data)
    db.session.commit()

    flash('New Entry was successfully posted')
    return redirect(url_for('show_entries'))
add_entry.provide_automatic_options = False
add_entry.methods = ['POST', 'OPTIONS']