var APP_NAME = 'picwall';
var ROOT_DIR = '/' + APP_NAME + '/';

var GOTO_PICTURE_INFO = ROOT_DIR+'picture/info/';

var GET_PICUTRE = ROOT_DIR+'picture/image/';
var GET_USER_PICTURES = ROOT_DIR+'user/pics/';

var GET_PIC_INFO = ROOT_DIR+'picture/info/'

var GET_PW_INFO = ROOT_DIR+'photowall/info/'
var GET_PW_PERMISSION = ROOT_DIR+'photowall/get_permission/'
var GET_PHOTOWALL_PICTURES = ROOT_DIR+'photowall/pics/'
var SAVE_PHOTOWALL = ROOT_DIR+'photowall/save/';

jQuery(document).ajaxSend(function(event, xhr, settings) {  
    function getCookie(name) {  
        var cookieValue = null;  
        if (document.cookie &&document.cookie != '') {  
            var cookies= document.cookie.split(';');  
            for (var i =0; i < cookies.length; i++) {  
               var cookie = jQuery.trim(cookies[i]);  
               // Does this cookie string begin with the name we want?  
               if (cookie.substring(0, name.length + 1) == (name + '=')) {  
                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));  
                   break;  
               }  
            }  
        }  
        return cookieValue;  
    }  
    function sameOrigin(url) {  
        // url could be relative or schemerelative or absolute  
        var host = document.location.host;// host + port  
        var protocol =document.location.protocol;  
        var sr_origin = '//' + host;  
        var origin = protocol + sr_origin;  
        // Allow absolute or scheme relativeURLs to same origin  
        return (url == origin ||url.slice(0, origin.length + 1) == origin + '/') ||  
            (url ==sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||  
            // or anyother URL that isn't scheme relative or absolute i.e relative.  
           !(/^(\/\/|http:|https:).*/.test(url));  
    }  
    function safeMethod(method) {  
        return(/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));  
    }  
    if(!safeMethod(settings.type) && sameOrigin(settings.url)) {  
       xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));  
    }  
});  
