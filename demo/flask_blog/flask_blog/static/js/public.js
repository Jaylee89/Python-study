$(function(){
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
})