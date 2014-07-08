from django.conf.urls import patterns, include, url
from picwall import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),

	url(r'^login/$', views.log_in),
	url(r'^logout/$', views.log_out),
	url(r'^register/$', views.register),

	url(r'^home/$', views.index_pic),
	url(r'^upload_pic/$', views.upload_pic),
	url(r'^delete_pic/(?P<file_name>\w+)/$', views.delete_pic),

	url(r'^pics/(?P<file_name>\w+)/$', views.find_pic),
	url(r'^pic_info/(?P<file_name>\w+)/$', views.pic_info),

	url(r'^publish_comment/$', views.publish_comment),
	url(r'^home_walls/$', views.index_picWall),
	url(r'^get_pics/$', views.return_pics),
	url(r'^picwall_info/(?P<picwall_id>\d+)$', views.picwall_info),
	url(r'^create_picwall/$', views.create_picwall),
	
	url(r'^get_photowall/$', views.get_photo_information_of_photowall),
	url(r'^photowall/(?P<wid>\d+)/$', views.view_photowall),
	url(r'^save_photowall/$', views.save_photowall),
	url(r'^delete_photowall/(?P<wid>\d+)$', views.delete_photowall),
)
