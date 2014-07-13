from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.forms import ModelForm

from datetime import date

import os
import time
import random

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'files/images/')

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
	def toDICT(self):
		ff = []
		for f in self._meta.fields:
		    ff.append(f.name)
		d = {}
		for attr in ff:
		    d[attr] = str(getattr(self, attr))
		return d

class PictureManager(models.Manager):
	def create_picture(self, name, author, description):
		upload_time = datetime.today()
		pid = '%s_%s_%s'%(str(time.asctime(time.localtime())).replace(' ', '_').replace(':', '_'), name, author)
		picture = self.create(pid=pid, name=name, author=author, description=description, upload_time = upload_time)
		return picture
	def save_picture(self, pid, name, description):
		pic = self.get(pid=pid)
		if pic is not None:
			pic.name = name
			pic.description = description
			pic.save()
	def get_access_pictures(self, user):
		pics = user.picture_set.all()
		return pics

class Picture(models.Model):
	pid = models.CharField(max_length = 100, default='')
	name = models.CharField(max_length = 50, default='name')
	description = models.CharField(max_length = 100, default='description')
	# image = models.ImageField(upload_to = IMAGE_DIR, default=IMAGE_DIR+'Christmas.jpg')
	upload_time = models.DateTimeField(datetime.today())
	author = models.ForeignKey(WebSiteUser)

	objects = PictureManager()

	def __unicode__(self):
		return self.pid
	def toDICT(self):
		ff = []
		for f in self._meta.fields:
		    ff.append(f.name)
		d = {}
		for attr in ff:
		    d[attr] = str(getattr(self, attr))
		return d

class PictureCommentManage(models.Manager):
	def create_picture_comment(self, author, pid, content):
		pic = Picture.objects.get(pid=pid)
		published_date = datetime.today()
		pic_comment = self.create(author=author, pic=pic, content=content, published_date=published_date)
		return pic_comment

class PictureComment(models.Model):
	pic = models.ForeignKey(Picture)
	author = models.ForeignKey(WebSiteUser)
	content = models.CharField(max_length=100)
	published_date = models.DateField()

	objects = PictureCommentManage()

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
	def save_photowall(self, wid, name, description):
		pw = self.get(pk=wid)
		if pw is not None:
			pw.name = name
			pw.description = description
			pw.modify_date = date.today()
			pw.save()
	def access_photowall(self, wid):
		pw = self.get(pk=wid)
		if pw is not None:
			pw.access_times += 1
	def get_private_photowall(self, user):
		pws = user.photowall_creator.all()
		return pws
	def get_access_photowalls(self, user):
		pws = user.access_users.all()
		return pws
	def get_manage_photowalls(self, user):
		pws = user.manage_users.all()
		return pws
	def get_random_photowalls(self):
		pws = random.sample(PhotoWall.objects.all(), min(5, PhotoWall.objects.count()))
		return pws
	def get_hot_photowalls(self):
		pws = PhotoWall.objects.order_by('-access_times').all()[:min(5, PhotoWall.objects.count())]
		return pws
	def get_new_photowalls(self):
		pws = PhotoWall.objects.order_by('-modify_date').all()[:min(5, PhotoWall.objects.count())]
		return pws

class PhotoWall(models.Model):
	name = models.CharField(max_length=32, default='')
	creator = models.ForeignKey(WebSiteUser, related_name='photowall_creator')
	description = models.CharField(max_length=256, default='')

	access_users = models.ManyToManyField(WebSiteUser, related_name='access_users')
	manage_users = models.ManyToManyField(WebSiteUser, related_name='manage_users')

	create_date = models.DateField(default=datetime.now())
	modify_date  = models.DateField(default=datetime.now())

	access_times = models.IntegerField(default=0)

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
