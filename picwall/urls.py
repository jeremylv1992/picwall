from django.conf.urls import patterns, include, url
from picwall import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),

	# user maintain
	url(r'^login/$', views.log_in, name='login'),
	url(r'^logout/$', views.log_out, name='logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^user/info/$', views.get_user_info, name='get user info'),
	url(r'^user/pics/$', views.get_user_pics, name='get user pics'),

	# pic
	url(r'^picture/$', views.picture_index, name='pic index'),
	url(r'^picture/info/(?P<pid>\d+)/$', views.pic_info, name='pic info'),
	url(r'^picture/info/$', views.get_pic_info, name='get pic info'),
	url(r'^picture/upload/$', views.upload_pic, name='upload pic'),
	url(r'^picture/delete/(?P<pid>\d+)/$', views.delete_pic, name='delete pic'),
	url(r'^picture/image/(?P<pid>\d+)/$', views.pic_image, name='pic image'),
	url(r'^picture/comment/$', views.pic_comment, name='pic comment'),
	url(r'^picture/edit/$', views.edit_pic, name='edit pic'),

	# pw
	url(r'^photowall/$', views.photowall_index, name='pw index'),
	url(r'^photowall/info/(?P<wid>\d+)/$', views.pw_info, name='pw info'),
	url(r'^photowall/info/$', views.get_pw_info, name='get pw info'),
	url(r'^photowall/create/$', views.create_pw, name='create pw'),
	url(r'^photowall/delete/(?P<wid>\d+)/$', views.delete_pw, name='delete pw'),
	url(r'^photowall/pics/$', views.get_pics_of_pw, name='get pics of pw'),
	url(r'^photowall/save/$', views.save_pw, name='save pw'),
	url(r'^photowall/edit/$', views.edit_pw, name='edit pw'),

)
