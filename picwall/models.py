from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from datetime import date
import time

class WebSiteUserManager(models.Manager):
	def create_user(self, user):
		webuser = self.create(user=user)
		return webuser

class WebSiteUser(models.Model):
	user = models.ForeignKey(User)
	friends = models.ManyToManyField("self")
	objects = WebSiteUserManager()

	def __unicode__(self):
		return self.user.username

class PictureManager(models.Manager):
	def create_picture(self, name, author, desc):
		upload_time = date.today()
		file_name = '%s_%s_%s'%(str(time.asctime(time.localtime())).replace(' ', '_').replace(':', '_'), name, author)
		picture = self.create(name=name, author=author, desc=desc, upload_time = upload_time, file_name=file_name)
		return picture
	def get_access_pictures(self, user):
		users = [user]
		for friend in user.friends.all():
			user.append(friend)
		pics = [e for e in user.picture_set.all() for user in users]
		return pics

class Picture(models.Model):
	file_name   = models.CharField(max_length = 100)
	name = models.CharField(max_length = 50)
	desc = models.CharField(max_length = 100)
	upload_time = models.DateTimeField()
	author = models.ForeignKey(WebSiteUser)
	url  = models.CharField(max_length = 200)
	objects = PictureManager()

	def __unicode__(self):
		return self.file_name
	def toDICT(self):
		ff = []
		for f in self._meta.fields:
		    ff.append(f.name)
		d = {}
		for attr in ff:
		    d[attr] = str(getattr(self, attr))
		return d

class PictureComment(models.Model):
	content = models.CharField(max_length=100)
	author = models.ForeignKey(WebSiteUser)
	pic = models.ForeignKey(Picture)
	published_date = models.DateField()
	def __unicode__(self):
		return self.content + '@' + str(self.pic)
	class Meta:
		ordering = ('published_date',)

class PhotoWallManager(models.Manager):
	def create_photowall(self, name, description, creator):
		photowall = PhotoWall(name=name, creator=creator, description=description)
		photowall.save()
		photowall.access_users.add(creator)
		photowall.save()
	def get_access_photowalls(self, user):
		users = [user]
		for friend in user.friends.all():
			users.append(friend)
		photowalls = [ e for e in user.photowall_set.all() for user in users]
		return photowalls
	def get_manage_photowalls(self, user):
		users = []

class PhotoWall(models.Model):
	name = models.CharField(max_length=32)
	creator = models.ForeignKey(WebSiteUser, related_name='creator+')
	create_data = models.DateField(default=datetime.now())
	access_users = models.ManyToManyField(WebSiteUser)
	# manage_users = models.ManyToManyField(WebSiteUser)
	description = models.CharField(max_length=256)
	# 

	objects = PhotoWallManager()

	def __unicode__(self):
		return str(self.name)
	def toDICT(self):
		ff = []
		for f in self._meta.fields:
			ff.append(f.name)
		d = {}
		for attr in ff:
			d[attr] = str(getattr(self, attr))
		return d

class PhotoInformation(models.Model):
	picture = models.ForeignKey(Picture)
	photowall = models.ForeignKey(PhotoWall)
	left = models.CharField(max_length=16)
	top = models.CharField(max_length=16)
	width = models.CharField(max_length=16)
	height = models.CharField(max_length=16)
	def toDICT(self):
		ff = []
		for f in self._meta.fields:
			ff.append(f.name)
		d = {}
		for attr in ff:
			d[attr] = str(getattr(self, attr))
		return d
