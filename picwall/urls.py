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
)
