from django.db import models

class User(models.Model):
	name = models.CharField('User name', max_length=32)
	password = models.CharField('Password', max_length=32)
	email = models.EmailField()
	def __unicode__(self):
		return self.name

class Picture(models.Model):
	author = models.ForeignKey(User)
	name = models.CharField(max_length=64)
	description = models.CharField('Description', max_length=256)
	src = models.CharField('Src', max_length=128)
	def __unicode__(self):
		return self.name

class PhotoWall(models.Model):
	name = models.CharField('Photo wall name', max_length=32)
	creator = models.ForeignKey(User, related_name="creator+")
	create_data = models.DateField()
	access_users = models.ManyToManyField(User)
	description = models.CharField('Description', max_length=256)
	def __unicode__(self):
		return self.name

class PhotoImformation(models.Model):
	picture = models.ForeignKey(Picture)
	photo_wall = models.ForeignKey(PhotoWall)
	positionX = models.FloatField('Top')
	positionY = models.FloatField('Left')
	def __unicode__(self):
		return str(self.picture) + " of " + str(self.photo_wall)
