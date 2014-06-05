from django.conf.urls import patterns, url

from photoWall import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^get_photo_information_of_photo_wall/$', views.get_photo_information_of_photo_wall, name='get_photo_information_of_photo_wall'),
		url(r'^create_photo_wall/$', views.create_photo_wall, name='create_photo_wall'),
		url(r'^photo_wall/(?P<photo_wall_id>\d+)/$', views.view_photo_wall, name='view_photo_wall'),
)
