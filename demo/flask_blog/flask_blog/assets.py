#-*- coding:utf-8 -*-

from flask.ext.assets import Bundle, Environment
from flask_blog import app

bundles = {
	'home_css': Bundle(
		'css/bootstrap.min.css', 
		'css/bootstrap-theme.min.css',
		'js/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min.css',
		'css/main.css',
		output='gen/home.css'
		),

	'home_js': Bundle(
		'js/jquery/dist/jquery.min.js',
		'js/bootstrap/dist/js/bootstrap.min.js',
		'js/bootstrap-datetimepicker/js/bootstrap-datetimepicker.js',
		'js/bootstrap-datetimepicker/js/locales/bootstrap-datetimepicker.zh-CN.js',
		'js/public.js',
		output='gen/home.js')
}

assets = Environment(app)

assets.register(bundles)