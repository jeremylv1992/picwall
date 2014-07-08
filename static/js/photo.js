//global
var g_selected = "";
var g_deltaX = 0;
var g_deltaY = 0;
var BARWIDTH = 200;
var PHOTOPADDING = 7;
var PHOTOPADDINGDOWN = 35;
var PHOTOWIDTH;

var GET_PICUTRE = '/picwall/picture/image/';
var SAVE_PHOTOWALL = '/picwall/photowall/save/'
var GET_USER_PICTURES = '/picwall/get_user_pics/';
var GET_PHOTOWALL_PICTURES = '/picwall/photowall/pics/'

$(function() { 
	init();
	loadBarPhotos();
	loadWallPhotos();
});

function init()
{
	//≥ı ºªØCSS
	var height = $(window).height() - 45;
	$("#down").css("height", height);

	$("#topbarleft>button").attr("disabled", true);
	$("#topbarleft>button").click(function(){
		$(g_selected).remove();
		cancelSelect();
	});

	//**********************************************
	// set mouse
	//**********************************************
	$("body").mouseup(function(ev){
		mouseUp(ev);
	});

	//button
	$("#savebutton").click(function(){
		save();
	});

}

function loadBarPhotos()
{
	$.getJSON(GET_USER_PICTURES, function(data){
		var str="";
		for(var i=0; i<data.length; i++)
	{
		str+="<img class='barphotos' class='list-group-item' src='"+GET_PICUTRE+data[i]["file_name"]+
		"/' id='photo" + i.toString() + "'alt='404' onmousedown='mouseDown(event)' >";
	}
	$("#sidebar").append(str);
	});
}

function loadWallPhotos()
{
	var url = window.location.href;
	var wid = url.split("/");
	wid = wid[wid.length-2];
	$.getJSON(GET_PHOTOWALL_PICTURES+"?wid="+wid, function(data){
		var str="";
		for(var i=0; i<data.length; i++)
	{
		var src = GET_PICUTRE+data[i]["picture"];
		var top = data[i]["top"];
		var left = data[i]["left"];
		var width = data[i]["width"];
		var height = data[i]["height"];
		appendWallPhotos("body",src, top, left, width, height);
	}
	$("#sidebar").append(str);
	});
}

function appendWallPhotos(dest, src, top, left, width, height)
{
	$(dest).append("<canvas id='floatCanvas'></canvas>");
	var canvas = $("#floatCanvas");

	width = parseInt(width);
	height = parseInt(height);

	//canvas Ù–‘…Ë÷
	var photoID = src.split("/");
	photoID = photoID[photoID.length-1];
	var shadowWidth = 6;
	canvas.css("top", top);
	canvas.css("left", left);
	canvas.css("width", width);
	canvas.css("height", height);
	canvas.attr("width", width);
	canvas.attr("height", height);
	canvas.draggable({ containment:"#main"});
	var newclass = canvas.attr("class");
	newclass = photoID+" "+newclass;
	canvas.attr("class", photoID+" "+newclass);
	canvas.mousedown(function(ev){
		setSelect(ev);
	});
	canvas.attr("id", "");
	var oriClass = canvas.attr("class");
	canvas.attr("class", oriClass + " wallphotos");
	canvas.css("z-index", "0");

	//ªÊ÷∆canvas
	var ctx = canvas[0].getContext("2d");

	var img = new Image();
	img.src = src;
	img.onload = function()
	{
		ctx.shadowColor = "#000000"; 
		ctx.shadowOffsetX = 1;    
		ctx.shadowOffsetY = 1;  
		ctx.shadowBlur = 10;
		ctx.fillStyle="#FFFFFF";
		ctx.fillRect(0,0,width-shadowWidth,height-shadowWidth);
		ctx.shadowBlur = 0;
		ctx.shadowOffsetX = 0;
		ctx.shadowOffsetY = 0;
		ctx.drawImage(img,PHOTOPADDING,PHOTOPADDING, width - PHOTOPADDING*2 - shadowWidth, height - PHOTOPADDINGDOWN - PHOTOPADDING - shadowWidth); 
	}

}

function mouseDown(ev)
{
	ev.preventDefault();
	cancelSelect();
	addCanvas(ev.target.src, "body", ev);

	//ø™∆Ù Û±Í∏˙◊Ÿ
	$("body").mousemove(function(ev){
		ev.preventDefault();
		var x = ev.pageX - g_deltaX;
		var y = ev.pageY - g_deltaY;
		$("#floatCanvas").css("top", y);
		$("#floatCanvas").css("left", x);
	})
}

function mouseUp(ev)
{
	var barwidth =parseInt($("#sidebar").css("width"));
	var mouseX = ev.pageX;
	if(     $(ev.target).offset().left <= barwidth  
			||  $(ev.target).offset().top <= $("#sidebar").offset().top
			||  $(ev.target).offset().left + parseInt($(ev.target).css("width")) >= $(window).width()
			||  $(ev.target).offset().top + parseInt($(ev.target).css("height")) >= $(window).height()
	  )
	{
		$("#floatCanvas").remove();
	}
	else
	{
		var canvas = $("#floatCanvas");
		canvas.attr("id", "");
		var oriClass = canvas.attr("class");
		canvas.attr("class", oriClass + " wallphotos");
		canvas.css("z-index", "0");
		$("body").append(canvas);
		//setSelect(ev.target);
	}

	//πÿ±’ Û±Í∏˙◊Ÿ
	$("body").mousemove();
}

function addCanvas(src, dest, event)
{
	$(dest).append("<canvas id='floatCanvas'></canvas>");
	var canvas = $("#floatCanvas");
	var top = $(event.target).offset().top;
	var left = $(event.target).offset().left;
	var width = event.target.width + PHOTOPADDING * 2;
	var height = event.target.height + PHOTOPADDINGDOWN + PHOTOPADDING;
	g_deltaX = event.pageX - left + PHOTOPADDING;
	g_deltaY = event.pageY - top + PHOTOPADDING;

	//canvas Ù–‘…Ë÷√
	var photoID = src.split("/");
	photoID = photoID[photoID.length-2];
	var shadowWidth = 6;
	canvas.css("top", top - PHOTOPADDING);
	canvas.css("left", left - PHOTOPADDING);
	canvas.css("width", width + shadowWidth);
	canvas.css("height", height + shadowWidth);
	canvas.attr("width", width + shadowWidth);
	canvas.attr("height", height + shadowWidth);
	canvas.draggable({ containment:"#main"});
	var newclass = canvas.attr("class");
	newclass = photoID+" "+newclass;
	canvas.attr("class", photoID+" "+newclass);
	canvas.mousedown(function(ev){
		setSelect(ev);
	});


	//ªÊ÷∆canvas
	var ctx = $("#floatCanvas")[0].getContext("2d");

	var img = new Image();
	img.src = src;
	img.onload = function()
	{
		ctx.shadowColor = "#000000"; 
		ctx.shadowOffsetX = 1;    
		ctx.shadowOffsetY = 1;  
		ctx.shadowBlur = 10;
		ctx.fillStyle="#FFFFFF";
		ctx.fillRect(0,0,width,height);
		ctx.shadowBlur = 0;
		ctx.shadowOffsetX = 0;
		ctx.shadowOffsetY = 0;
		ctx.drawImage(img,PHOTOPADDING,PHOTOPADDING, width - PHOTOPADDING*2, height - PHOTOPADDINGDOWN - PHOTOPADDING); 
	}
}





function setSelect(ev)
{
	g_selected = ev.target;
	$("#topbarleft>button").attr("disabled", false);
}

function cancelSelect()
{
	g_selected = "";
	$("#topbarleft>button").attr("disabled", true);
}

function save()
{
	var jsonStr = "[";
	var first = true;

	$(".wallphotos").each(function(){

		var pid = ($(this).attr("class").split(" "))[0];
		var left = $(this).css("left");
		var top = $(this).css("top");
		var width = $(this).css("width");
		var height = $(this).css("height");

		if (first)
		first = false;
		else
		jsonStr += ","

		jsonStr += "{\"pid\":\"" + pid + 
		"\",\"left\":\"" + left + 
		"\",\"top\":\"" + top + 
		"\",\"width\":\"" + width + 
		"\",\"height\":\"" + height + 
		"\"}";
	});
	jsonStr += "]";

	var url = window.location.href;
	var wid = url.split("/");
	wid = wid[wid.length-2];
	theurl = SAVE_PHOTOWALL;

	$.ajax({ url : theurl,
		data : {"wid":wid,"text":jsonStr},
		success: function(data){
			alert(data);
		}});
}
