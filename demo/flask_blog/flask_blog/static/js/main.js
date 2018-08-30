'use strict';

require.config({
	baseUrl: "static/js",
	urlArgs: "v=" + (new Date()).getTime(),
	paths: {
		"jquery": "jquery/dist/jquery.min",
		"bootstrap": "bootstrap/dist/js/bootstrap.min",
		"bootstrap-datetimepicker": "bootstrap-datetimepicker/js/bootstrap-datetimepicker",
		"bootstrap-datetimepicker-zh": "bootstrap-datetimepicker/js/locales/bootstrap-datetimepicker.zh-CN",
	},
	shim:{
		'bootstrap-datetimepicker-zh':{
			deps:[
				'bootstrap-datetimepicker'
			]
		},
		'bootstrap':{
			deps:[
				'jquery',
				'css!../css/bootstrap.min',
				'css!../css/bootstrap-theme.min'
			]
		},
		'bootstrap-datetimepicker':{
			deps:[
				'bootstrap',
				'css!../js/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min'
			]
		}
	},
	map:{
		'*':{
			'css':'require-css/css.min'
		}
	}
});

require(['jquery','bootstrap','bootstrap-datetimepicker','bootstrap-datetimepicker-zh'],function($,bootstrap,datetimepicker,datetimepickerZh){
	//日期插件
	$('#start_date').datetimepicker({
        language:'zh-CN',
        weekStart: 1,
        todayBtn:  1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        minView: 2
    }).on('changeDate',function(ev){
        $('#end_date').datetimepicker('setStartDate',ev.date);
    }).on('outOfRange',function(){

    });

    $('#end_date').datetimepicker({
        language:'zh-CN',
        weekStart: 1,
        todayBtn:  1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        minView: 2
    }).on('changeDate',function(ev){
        $('#start_date').datetimepicker('setEndDate',ev.date);
    }).on('outOfRange',function(){

    });
});