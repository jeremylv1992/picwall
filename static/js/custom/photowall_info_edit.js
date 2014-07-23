// by hiukin 

//global
var g_selected = "";
var g_deltaX = 0;
var g_deltaY = 0;
var g_mainWidth; 

// static data
var PHOTOPADDING = 0.00013;
var PHOTOPADDINGBOTTOM = 0.0007;
var PHOTOSHADOW = 0.0002;
var PHOTOAREA = 50000;

$(function() {
	$(window).resize(onResize);
	init();
	loadBarPhotos();
	loadWallPhotos();
});

function init()
{
	onResize();

	$("#delete-btn").attr("disabled", true);
	$("#delete-btn").click(function(){
		$(g_selected).remove();
		cancelSelect();
	});

	$("body").mouseup(function(ev){
		mouseUp(ev);
	});

	//button
	$("#save-btn").click(function(){
		save();
	});

}

function onResize()
{
	// set css of the elements
	var height = $(window).height() - 98;
	$("#down").css("height", height);
	$("#sidebar").css("height", height);
	$("#main").css("height", height);
	g_mainWidth = parseFloat($("#main").css("width"));
}


function loadBarPhotos()
{
	$.getJSON(GET_USER_PICTURES, function(data){
		var str="";
		for(var i=0; i<data.length; i++)
		{

			str+="<img class='barphotos' class='list-group-item' src='"+GET_PICUTRE+data[i]["id"]+
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
		for(var i=0; i<data.length; i++)
		{
			var src = GET_PICUTRE+data[i]["picture"];
			var top = data[i]["top"];
			var left = data[i]["left"];
			var width = data[i]["width"];
			var height = data[i]["height"];

			appendWallPhotos("#board",src, top, left, width, height);
		}
	});
}

function appendWallPhotos(dest, src, top, left, width, height)
{
	$(dest).append("<canvas id='floatCanvas'></canvas>");
	var canvas = $("#floatCanvas");

	width = parseFloat(width);
	height = parseFloat(height);

	//canvasÊôÐÔÉèÖ
	var photoID = src.split("/");
	photoID = photoID[photoID.length-1];
	canvas.css("top", top);
	canvas.css("left", left);
	canvas.css("width", width);
	canvas.css("height", height);
	canvas.attr("width", width);
	canvas.attr("height", height);
	
	canvas.attr("pid", photoID);
	canvas.attr("id", "");
	canvas.attr("class", "wallphotos");
	canvas.css("z-index", "0");

	canvas.mousedown(function(ev){
		setSelect(ev);
	});

	// jquery ui
	canvas.draggable({ containment:"#board"});

	// calculate canvas data
	var photoPadding = PHOTOAREA * PHOTOPADDING;
	var photoPaddingBottom = PHOTOAREA * PHOTOPADDINGBOTTOM;
	var photoShadow = PHOTOAREA * PHOTOSHADOW;

	// draw canvas
	var ctx = canvas[0].getContext("2d");
	var img = new Image();
	img.src = src;
	img.onload = function()
	{
		ctx.shadowColor = "#000000"; 
		ctx.shadowOffsetX = photoShadow*0.15;
		ctx.shadowOffsetY = photoShadow*0.15;
		ctx.shadowBlur = photoShadow*1.3;
		ctx.fillStyle="#FFFFFF";
		ctx.fillRect(0,0,width-photoShadow,height-photoShadow);
		ctx.shadowOffsetX = 0;
		ctx.shadowOffsetY = 0;
		ctx.shadowBlur = 0;
		ctx.drawImage(img,photoPadding,photoPadding, width-photoPadding*2-photoShadow, height-photoPaddingBottom-photoPadding-photoShadow); 
	}
}

function mouseDown(ev)
{
	ev.preventDefault();
	cancelSelect();
	generateFloatCanvas(ev.target.src, "#main", ev);

	//¿ªÆôÊó±ê¸ú×Ù
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
	var img = $("#board>img");
	if(     $(ev.target).offset().left <= img.offset().left 
			||  $(ev.target).offset().top <= img.offset().top 
			||  $(ev.target).offset().left + parseFloat($(ev.target).css("width")) >= img.offset().left + parseFloat(img.css("width"))
			||  $(ev.target).offset().top + parseFloat($(ev.target).css("height")) >= img.offset().top + parseFloat(img.css("height"))
	  )
	{
		$("#floatCanvas").remove();
	}
	else
	{
		//calculate relative position
		//alert($(ev.target).offset().left);
		var left = $(ev.target).offset().left - $("#board").offset().left;
		var top = $(ev.target).offset().top - $("#board").offset().top;

		var canvas = $("#floatCanvas");
		canvas.attr("id", "");
		canvas.attr("class", "wallphotos");
		canvas.css("z-index", "0");
		canvas.css("left", left);
		canvas.css("top", top);

		// jquery ui
		canvas.draggable({ 
			containment:"#board"
		});

		$("#board").append(canvas);
		//setSelect(ev.target);
	}

	//¹Ø±ÕÊó±ê¸ú×Ù
	$("body").mousemove();
}

function generateFloatCanvas(src, dest, event)
{
	// calculate photo data
	var k = event.target.height/event.target.width;
	var width = Math.sqrt(PHOTOAREA/k);
	var photoPadding = PHOTOAREA * PHOTOPADDING;
	var photoPaddingBottom = PHOTOAREA * PHOTOPADDINGBOTTOM;
	var photoShadow = PHOTOAREA * PHOTOSHADOW;
	var height = (width-photoPadding*2-photoShadow)*k
		 + photoPadding + photoPaddingBottom + photoShadow;

	// calculate canvas data
	$(dest).append("<canvas id='floatCanvas'></canvas>");
	var canvas = $("#floatCanvas");
	var left = event.pageX - width/2;
	var top  = event.pageY - height/2;
	//var left = $(event.target).offset().left;
	g_deltaX = width/2;
	g_deltaY = height/2;

	// set canvas data
	var photoID = src.split("/");
	photoID = photoID[photoID.length-2];
	canvas.css("top", top);
	canvas.css("left", left);
	canvas.css("width", width);
	canvas.css("height", height);
	canvas.attr("width", width);
	canvas.attr("height", height);
	var newclass = canvas.attr("class");
	canvas.attr("pid", photoID);
	canvas.mousedown(function(ev){
		setSelect(ev);
	});

	// draw canvas
	var ctx = $("#floatCanvas")[0].getContext("2d");
	var img = new Image();
	img.src = src;
	img.onload = function()
	{
		ctx.shadowColor = "#000000"; 
		ctx.shadowOffsetX = photoShadow*0.15;
		ctx.shadowOffsetY = photoShadow*0.15;
		ctx.shadowBlur = photoShadow*1.3;
		ctx.fillStyle="#FFFFFF";
		ctx.fillRect(0,0,width-photoShadow,height-photoShadow);
		ctx.shadowOffsetX = 0;
		ctx.shadowOffsetY = 0;
		ctx.shadowBlur = 0;
		ctx.drawImage(img,photoPadding,photoPadding, width-photoPadding*2-photoShadow, height-photoPaddingBottom-photoPadding-photoShadow); 
	}
}


function setSelect(ev)
{
	g_selected = ev.target;
	$("#delete-btn").attr("disabled", false);
}

function cancelSelect()
{
	g_selected = "";
	$("#delete-btn").attr("disabled", true);
}

function save()
{
	// generate the json string
	var jsonStr = "[";
	var first = true;

	$(".wallphotos").each(function(){

		var pid 	= 	$(this).attr("pid");
		var left 	= 	$(this).css("left");
		var top 	= 	$(this).css("top");
		var width 	=	$(this).css("width");
		var height 	=	$(this).css("height");

		if (first)
		{
			first = false;
		}
		else
		{
			jsonStr += ",";
		}	

		jsonStr += "{\"pid\":\"" + pid + 
		"\",\"left\":\"" + left + 
		"\",\"top\":\"" + top + 
		"\",\"width\":\"" + width + 
		"\",\"height\":\"" + height + 
		"\"}";
	});
	jsonStr += "]";

	// generate img data
	var imgCanvas = saveWallImg();
	var imgData = imgCanvas[0].toDataURL("image/jpeg");
    var b64 = imgData.substring(22);

	var url = window.location.href;
	var wid = url.split("/");
	wid = wid[wid.length-2];

	$.ajax({ url : SAVE_PHOTOWALL,
		type: "POST",
		data : {"wid":wid,"text":jsonStr,"data":b64 },
		success: function(data){
			alert(data);
		}});

}

function saveWallImg()
{
	// generate canvas
	var	bgWidth = parseFloat($("#board>img").css("width"));
	var bgHeight = parseFloat($("#board>img").css("height"));

	var canvas = $("<canvas></canvas>");
	canvas.css("width", bgWidth);
	canvas.css("height", bgHeight);
	canvas.attr("width", bgWidth);
	canvas.attr("height", bgHeight);

	// draw background
	var ctx = canvas[0].getContext("2d");
	var img = new Image();
	img.src = $("#board>img").attr("src");
	ctx.drawImage(img, 0, 0, bgWidth, bgHeight); 

	//draw image
	$(".wallphotos").each(function(){
		// draw canvas
		var wallphoto = $(this);

		var newimg = new Image();
		newimg.src = GET_PICUTRE + $(this).attr("pid") + '/';
		// calculate canvas data
		var left = parseInt(wallphoto.css("left"));
		var top = parseInt(wallphoto.css("top"))
		var height = parseFloat(wallphoto.css("height"));
	var width = parseFloat(wallphoto.css("width"));

	var photoPadding = PHOTOAREA * PHOTOPADDING;
	var photoPaddingBottom = PHOTOAREA * PHOTOPADDINGBOTTOM;
	var photoShadow = PHOTOAREA * PHOTOSHADOW;

	ctx.shadowColor = "#000000"; 
	ctx.shadowOffsetX = photoShadow*0.15;
	ctx.shadowOffsetY = photoShadow*0.15;
	ctx.shadowBlur = photoShadow*1.3;
	ctx.fillStyle="#FFFFFF";
	ctx.fillRect(left,top,width-photoShadow,height-photoShadow);
	ctx.shadowOffsetX = 0;
	ctx.shadowOffsetY = 0;
	ctx.shadowBlur = 0;
	ctx.drawImage(newimg,left+photoPadding,top+photoPadding, width-photoPadding*2-photoShadow, height-photoPaddingBottom-photoPadding-photoShadow); 
	});

	return canvas;
}
