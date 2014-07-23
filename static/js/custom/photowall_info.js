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
	loadWallPhotos();
});

function init()
{
	onResize();

	$("body").mouseup(function(ev){
		mouseUp(ev);
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

	canvas.click(function() {
		window.location.assign(GOTO_PICTURE_INFO+photoID);
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
