from django.utils.timezone import utc
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from datetime import date

import os
import time
import random

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'files/images/')

class WebSiteUserManager(models.Manager):
	def create_user(self, user):
		webuser = self.create(user=user)
		webuser.user_labels.add(PictureLabel.objects.create(owner=webuser, name="default"))
		webuser.save()
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

class PictureLabelManager(models.Manager):
	def create_label(self, owner, name):
		label = self.create(owner=owner, name=name)
		return label

class PictureLabel(models.Model):
	name = models.CharField(max_length=10)
	owner = models.ForeignKey(WebSiteUser, related_name="user_labels")

	objects = PictureLabelManager()
	def __unicode__(self):
		return self.name

class PictureManager(models.Manager):
	def create_picture(self, name, author, description, label):
		upload_time = datetime.utcnow().replace(tzinfo=utc)
		picture = self.create(name=name, author=author, description=description, upload_time = upload_time, label=label)
		return picture
	def save_picture(self, pid, name, description, label):
		pic = self.get(pk=pid)
		if pic is not None:
			pic.name = name
			pic.description = description
			pic.label = label
			pic.save()
	def get_access_pictures(self, user):
		pics = user.picture_set.all()
		return pics

class Picture(models.Model):
	name = models.CharField(max_length = 32, default='name')
	description = models.CharField(max_length = 64, default='description')
	upload_time = models.DateTimeField(datetime.today())
	author = models.ForeignKey(WebSiteUser)
	label = models.ForeignKey(PictureLabel, related_name='label_pics')

	objects = PictureManager()

	def __unicode__(self):
		return str(self.id)
	def toDICT(self):
		ff = []
		for f in self._meta.fields:
			ff.append(f.name)
		d = {}
		for attr in ff:
			d[attr] = getattr(self, attr)
		return d

class PictureCommentManage(models.Manager):
	def create_picture_comment(self, author, pid, content):
		pic = Picture.objects.get(pk=pid)
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
		create_date = datetime.utcnow().replace(tzinfo=utc)
		modify_date = datetime.utcnow().replace(tzinfo=utc)
		photowall = PhotoWall(name=name, creator=creator, description=description, create_date=create_date, modify_date=modify_date)
		photowall.save()
		photowall.access_users.add(creator)
		photowall.manage_users.add(creator)
		photowall.save()
	def save_photowall(self, wid, name, description):
		pw = self.get(pk=wid)
		if pw is not None:
			pw.name = name
			pw.description = description
			pw.modify_date = date.today()
			pw.save()
	def access_photowall(self, pw):
		pw.access_times += 1
		pw.save()
	def get_private_photowall(self, user):
		pws = user.photowall_creator.all()
		return pws
	def get_access_photowalls(self, user):
		pws = user.access_pws.all()
		return pws
	def get_manage_photowalls(self, user):
		pws = user.manage_pws.all()
		return pws

	def get_random_photowalls(self, user):
		# pws = random.sample(user.access_pws.all(), min(5, user.access_pws.count()))
		pws = random.sample(PhotoWall.objects.all(), min(5, PhotoWall.objects.count()))
		return pws
	def get_hot_photowalls(self, user):
		pws = user.access_pws.order_by('-access_times').all()[:min(5, PhotoWall.objects.count())]
		return pws
	def get_new_photowalls(self, user):
		pws = user.access_pws.order_by('-modify_date').all()[:min(5, PhotoWall.objects.count())]
		return pws

class PhotoWall(models.Model):
	name = models.CharField(max_length=32, default='')
	creator = models.ForeignKey(WebSiteUser, related_name='photowall_creator')
	description = models.CharField(max_length=256, default='')

	access_users = models.ManyToManyField(WebSiteUser, related_name='access_pws')
	manage_users = models.ManyToManyField(WebSiteUser, related_name='manage_pws')

	PRIVATE = 'private'
	FRIEND = 'friend'
	PUBLIC = 'public'

	PERMISSION_CHOICES = (
		(PRIVATE, 'Private'),
		(FRIEND, 'Friend'),
		(PUBLIC, 'Pulbic'),
	)
	access_permission = models.CharField(max_length=10, choices=PERMISSION_CHOICES, default=PRIVATE)

	create_date = models.DateField(default=datetime.now())
	modify_date  = models.DateField(default=datetime.now())

	access_times = models.IntegerField(default=0)

	objects = PhotoWallManager()

	def __unicode__(self):
		return self.name
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
