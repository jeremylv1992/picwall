from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class pw_pic(models.Model):
    pic_id   = models.CharField(max_length = 100)
    pic_name = models.CharField(max_length = 50)
    pic_desc = models.CharField(max_length = 100)
    pic_url  = models.CharField(max_length = 200)
    pic_upload_time = models.DateTimeField('date published')
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


class pw_user(models.Model):
    name = models.CharField(max_length = 20, primary_key = True)
    email = models.CharField(max_length = 50)
#   pics = models.ManyToManyField(pw_pic, through = 'pw_user_pic')
    def __unicode__(self):
	return self.name

class pic_comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    pic = models.ForeignKey(pw_pic)
    published_date = models.DateField()
    
    def __unicode__(self):
	return self.content + '@' + str(self.pic)

    class Meta:
	ordering = ('published_date',)

class PhotoWall(models.Model):
	name = models.CharField('Photo wall name', max_length=32)
	creator = models.ForeignKey(User, related_name="creator+")
	create_data = models.DateField(default=datetime.now())
	access_users = models.ManyToManyField(User)
	description = models.CharField('Description', max_length=256)
<<<<<<< HEAD
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
=======
	create_date  = models.DateField()
	def PhotoInformation__unicode__(self):
		return self.name
>>>>>>> 656a8b1290103657703f53ac964758abb5eaa640

class PhotoInformation(models.Model):
	picture = models.ForeignKey(pw_pic)
	photo_wall = models.ForeignKey(PhotoWall)
	positionX = models.FloatField('Top')
	positionY = models.FloatField('Left')
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
