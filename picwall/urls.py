from django.conf.urls import patterns, include, url
from picwall import views

urlpatterns = patterns('',
	url(r'^$', views.index),

	# user maintain
	url(r'^login/$', views.log_in),
	url(r'^logout/$', views.log_out),
	url(r'^register/$', views.register),


	# picture maintain
	url(r'^picture/upload/$', views.upload_pic),
	url(r'^picture/delete/(?P<file_name>\w+)/$', views.delete_pic),
	url(r'^picture/image/(?P<file_name>\w+)/$', views.pic_image),
	url(r'^picture/info/(?P<file_name>\w+)/$', views.pic_info),

	# comment
	url(r'^picture/comment/$', views.pic_comment),

	## POST
	url(r'^get_user_pics/$', views.get_user_pics),
	url(r'^photowall/info/(?P<wid>\d+)/$', views.pw_info),
	url(r'^photowall/create/$', views.create_pw),
	
	url(r'^photowall/pics/$', views.get_pics_of_pw),
	url(r'^photowall/(?P<wid>\d+)/$', views.view_pw),
	url(r'^photowall/save/$', views.save_pw),
	url(r'^photowall/delete/(?P<wid>\d+)/$', views.delete_pw),

	# friend
	## url(r'^friend/create/$', vies.make_friend),
	## url(r'^friend/delete/$', vies.delete_friend),
)
