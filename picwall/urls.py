from django.conf.urls import patterns, include, url
from picwall import views

urlpatterns = patterns('',
	url(r'^$', views.index),

	# user maintain
	url(r'^login/$', views.log_in),
	url(r'^logout/$', views.log_out),
	url(r'^register/$', views.register),
	url(r'^user/info/$', views.get_user_info),
	url(r'^user/pics/$', views.get_user_pics),

	# pic
	url(r'^picture/$', views.picture_index),
	url(r'^picture/upload/$', views.upload_pic),
	url(r'^picture/delete/(?P<pid>\w+)/$', views.delete_pic),
	url(r'^picture/image/(?P<pid>\w+)/$', views.pic_image),
	url(r'^picture/info/(?P<pid>\w+)/$', views.pic_info),
	url(r'^picture/info/$', views.get_pic_info),
	url(r'^picture/comment/$', views.pic_comment),
	url(r'^picture/edit/$', views.edit_pic),

	# pw
	url(r'^photowall/$', views.photowall_index),
	url(r'^photowall/info/(?P<wid>\d+)/$', views.pw_info),
	url(r'^photowall/create/$', views.create_pw),
	url(r'^photowall/pics/$', views.get_pics_of_pw),
	url(r'^photowall/info/$', views.get_pw_info),
	url(r'^photowall/save/$', views.save_pw),
	url(r'^photowall/delete/(?P<wid>\d+)/$', views.delete_pw),
	url(r'^photowall/edit/$', views.edit_pw),

	# friend
	url(r'^friend/create/(?P<user_name>/w+)/$', views.make_friend),
	url(r'^friend/delete/(?P<user_name>/w+)/$', views.delete_friend),
)
