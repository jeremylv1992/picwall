//global
var g_selected = "";
var g_deltaX = 0;
var g_deltaY = 0;
var BARWIDTH = 200;
var PHOTOPADDING = 7;
var PHOTOPADDINGDOWN = 35;
var IPADDR = "172.18.158.164:8888";


$(function()
{ 
    //div.style.width="40%"; 
    //div.style.height=200; 
    // /div.style.overflow="auto"; 
    init();
    appendBarPhotos();
    alert("finish");
});

function init()
{
    //初始化CSS
    //alert($("#topbar").css("border"));
    //alert(parseInt($("#topbar").css("border-bottom")));
    var height = $(window).height() - 45;
    //var mainWidth = $(window).width() - parseInt($("#sidebar").css("width"));
    //$("#sidebar").css("height", height);
    //$("#main").css("height", height);
    $("#down").css("height", height);

    $("#topbarleft>button").attr("disabled", true);
    $("#topbarleft>button").click(function(){
        g_selected.remove();
        cancelSelect();
    });
    
    //**********************************************
    //注册鼠标事件
    //**********************************************
    /*
    $("body").mousedown(function(){
        cancelSelect();
    });
    */
    $("body").mouseup(function(ev){
        mouseUp(ev);
    });

    //button
    $("#savebutton").click(function(){
        save();
    });

}

function appendBarPhotos()
{
    //IPADDR+"/picwall/get_pics/"
    $.getJSON("http://172.18.158.164:8888/picwall/get_pics/", function(result){
        alert("ok");
        //alert(content.responseText);
        //$("#myDiv").html(htmlobj.responseText);
    });
            
    var str="";
    for(var i=0; i<6; i++)
    {
        str+="<img class='barphotos' class='list-group-item' src='photos/00"+i.toString()+
        ".JPG' id='photo" + i.toString() + "'alt='404' onmousedown='mouseDown(event)' >";
    }
    $("#sidebar").append(str);
}

function mouseDown(ev)
{
    ev.preventDefault();
    cancelSelect();
    addCanvas(ev.target.src, "body", ev);

    //开启鼠标跟踪
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
    //alert($(ev.target).offset().left);
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
        canvas.attr("class", "wallphotos");
        canvas.css("z-index", "0");
        $("body").append(canvas);
        //setSelect(ev.target);
    }
    
    //关闭鼠标跟踪
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

    //canvas属性设置
    var shadowWidth = 6;
    canvas.css("top", top - PHOTOPADDING);
    canvas.css("left", left - PHOTOPADDING);
    canvas.css("width", width + shadowWidth);
    canvas.css("height", height + shadowWidth);
    canvas.attr("width", width + shadowWidth);
    canvas.attr("height", height + shadowWidth);
    canvas.draggable({ containment:"#main"});
    canvas.mousedown(function(ev){
        setSelect(ev);
    });

    //绘制canvas
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
    $(".wallphotos").each(function(){
        alert($(this));
    });

}