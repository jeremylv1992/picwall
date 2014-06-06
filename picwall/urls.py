#########################################################################
# File Name: urls.py
# Author: Jeremy
# mail: Jeremy19921115@gmail.com
# Created Time: Sun 01 Jun 2014 11:26:11 AM CST
#########################################################################
#!/usr/bin/env python
#coding=utf-8
from django.conf.urls import patterns, include, url
from picwall import views
urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),		
    url(r'^logout/$', views.log_out),
    url(r'^login/$', views.log_in),
    url(r'^home/$', views.index_pic),
    url(r'^register/$', views.register),
    url(r'^upload_pic/$', views.upload_pic),		
    url(r'^pics/(?P<pic_id>\w+)/$', views.find_pic),
    url(r'^pic_info/(?P<pic_id>\w+)/$', views.pic_info),
    url(r'^publish_comment/$', views.publish_comment),
    url(r'^home_walls/$', views.index_picWall),
    url(r'^get_pics/$', views.return_pics),
    url(r'^picwall_info/(?P<picwall_id>\d+)$', views.picwall_info),
    url(r'^create_picwall/$', views.create_picwall),
    
    url(r'^get_photo_wall/$', views.get_photo_information_of_photo_wall, name='get_photo_information_of_photo_wall'),
    url(r'^photo_wall/(?P<photo_wall_id>\d+)/$', views.view_photo_wall, name='view_photo_wall'),
    url(r'^save_photo_wall/$', views.save_photo_wall, name='save_photo_wall')

)
