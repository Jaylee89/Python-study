#-*- coding:utf8 -*-

from flask import Flask,render_template,request
from flask_blog.database import mongo
from flask_blog.models import Itunes
from flask_blog import app
import time,os

def itunes():
	page = int(request.args.get('page')) if request.args.get('page') else 1
	pagesize = 20
	prev_page = page - 1 if page - 1 else 1
	next_page = page + 1

	# 关键字查询
	keywords = request.args.get('keywords')
	start_date = request.args.get('start_date') 
	end_date = request.args.get('end_date')

	params = []
	params_query = {}
	if keywords:
		params.append({'title':{'$regex':'^%s' %keywords }})
		params_query['keywords'] = keywords

	if start_date and end_date:
		start = '%s 00:00:00' % start_date
		end = '%s 23:59:59' % end_date
		start = int(time.mktime(time.strptime(start,'%Y-%m-%d %H:%M:%S')))
		end = int(time.mktime(time.strptime(end,'%Y-%m-%d %H:%M:%S')))
		params.append({'create_time':{'$gt':start}})
		params.append({'create_time':{'$lte':end}})

		params_query['start_date'] = start_date
		params_query['end_date'] = end_date

	if params:
		# if len(params) == 1:
		# 	where = params
		# else:
		where = {'$and':params} 
		itunes_sum = mongo.db.itunes.find(where).count()
		itunes = mongo.db.itunes.find(where).skip((page - 1) * pagesize).sort('create_time',-1).limit(pagesize)
	else:
		itunes_sum = mongo.db.itunes.count()
		itunes = mongo.db.itunes.find().skip((page - 1) * pagesize).sort('create_time',-1).limit(pagesize)
	
	return render_template(
			'front/spider_itunes.html',
			itunes=itunes,
			itunes_sum=itunes_sum,
			title=u"iTunes爬虫",
			prev_page=prev_page,
			next_page=next_page,
			params=params_query
	)
itunes.provide_automatic_options = False
itunes.methods = ['GET','POST','OPTIONS']

def apple():
	page = int(request.args.get('page')) if request.args.get('page') else 1
	pagesize = 20
	prev_page = page - 1 if page - 1 else 1
	next_page = page + 1
	
	# 关键字查询
	keywords = request.args.get('keywords')
	start_date = request.args.get('start_date') 
	end_date = request.args.get('end_date')
	export_sql = request.args.get('export_sql')
	export_state_code = 1
	export_message = ''

	params_query = {}
	export_query = []
	query = Itunes.query

	if export_sql:
		export_sql = bool(int(export_sql))
	if keywords:
		query = query.filter(Itunes.title.startswith(keywords))
		params_query['keywords'] = keywords
		export_query.append('title like "%s%"' % keywords)

	if start_date and end_date:
		start = '%s 00:00:00' % start_date
		end = '%s 23:59:59' % end_date
		start = int(time.mktime(time.strptime(start,'%Y-%m-%d %H:%M:%S')))
		end = int(time.mktime(time.strptime(end,'%Y-%m-%d %H:%M:%S')))
		
		query = query.filter(Itunes.create_time > start)
		query = query.filter(Itunes.create_time <= end)

		export_query.append('create_time >= %s' % start)
		export_query.append('create_time < %s' % end)

		params_query['start_date'] = start_date
		params_query['end_date'] = end_date

	time_string = time.time()
	if params_query: 
		itunes_sum = query.count()
		itunes = query.offset((page-1)*pagesize).limit(pagesize).all()
		if export_sql:
			#导出sql数据
			
			shell_conent = 'mysqldump qeeniao itunes --where="%s" > %s/itunes_%s.sql' % (' and '.join(export_query),app.config['UPLOAD_FOLDER'],int(time_string))
			export_state_code = os.system(shell_conent)
			export_message = u'导出成功！文件路径为：%s/itunes_%s.sql' % (app.config['UPLOAD_FOLDER'],int(time_string))

	else:
		itunes_sum = Itunes.query.count()
		itunes = Itunes.query.offset((page-1)*pagesize).limit(pagesize).all()
		if export_sql:
			#导出sql数据
			export_state_code = os.system('mysqldump qeeniao itunes > %s/itunes_%s.sql' % (app.config['UPLOAD_FOLDER'],int(time_string)))
			export_message = u'导出成功！文件路径为：%s/itunes_%s.sql' % (app.config['UPLOAD_FOLDER'],int(time_string))
	
	return render_template(
			'front/spider_apple.html',
			itunes=itunes,
			itunes_sum=itunes_sum,
			title=u"Apple爬虫",
			prev_page=prev_page,
			next_page=next_page,
			params=params_query,
			export_state=export_state_code,
			export_message=export_message
	)
apple.provide_automatic_options = False
apple.methods = ['GET','POST','OPTIONS']