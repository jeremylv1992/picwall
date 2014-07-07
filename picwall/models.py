from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Picture(models.Model):
	pic_id   = models.CharField(max_length = 100)
	pic_name = models.CharField(max_length = 50)
	pic_desc = models.CharField(max_length = 100)
	pic_url  = models.CharField(max_length = 200)
	pic_upload_time = models.DateTimeField()
	pic_author = models.ForeignKey(User)     
	def __unicode__(self):
		return self.pic_id
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
	author = models.ForeignKey(User, related_name="commenter")
	pic = models.ForeignKey(Picture)
	published_date = models.DateField()
	def __unicode__(self):
		return self.content + '@' + str(self.pic)
	class Meta:
		ordering = ('published_date',)


class PhotoWall(models.Model):
	name = models.CharField(max_length=32)
	creator = models.ForeignKey(User, related_name="creator+")
	create_data = models.DateField(default=datetime.now())
	access_users = models.ManyToManyField(User, related_name="access_user_+")
	description = models.CharField(max_length=256)
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
	photo_wall = models.ManyToManyField(PhotoWall)
	left = models.CharField(max_length=16)
	top = models.CharField(max_length=16)
	width = models.CharField(max_length=16)
	height = models.CharField(max_length=16)
	def __unicode__(self):
		return str(self.picture) + " of " + str(self.photo_wall)
	def toDICT(self):
		ff = []
		for f in self._meta.fields:
			ff.append(f.name)
		d = {}
		for attr in ff:
			d[attr] = str(getattr(self, attr))
		return d

