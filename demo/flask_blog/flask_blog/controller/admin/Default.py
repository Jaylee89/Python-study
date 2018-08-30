__author__ = 'davidzhang'
# -*- coding:utf-8 -*-

from flask import Flask,render_template
def index():

    return render_template('admin/index.html',title='Qeeniao Blog',description='hare')

index.methods = ['POST','GET','OPTIONS']