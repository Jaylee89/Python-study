#-*- coding:utf-8 -*-

from flask_blog import app
import datetime,time

@app.template_filter('reverse')
def reverse_filter(s):
	return s[::-1]

@app.template_filter('timestamp_to_string')
def timestamp_to_string(s):
	if s:
		s = int(s)
		t = time.localtime(s)
		return time.strftime('%Y-%m-%d %H:%M:%S',t)