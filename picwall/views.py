# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core import serializers
from datetime import date

from picwall.models import Picture, PictureComment, PhotoWall, PhotoInformation, PhotoInformation

from myForms import Login_Form

import time
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def index(request):
    return HttpResponse('Hello Picturewall!')


def log_in(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/picwall/home/')
	login_prompt = ''
	email = ''
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		users = User.objects.filter(email = email)
		if len(users) > 0:
			user = authenticate(username = users[0].username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/picwall/home/')
				else:
					login_promt = 'Invalid user'
			else:
				login_prompt = 'Password is wrong'
		else:
			login_prompt = 'E-mail is invalid'
	return render(request, 'picwall/login.html',{'login_prompt':login_prompt,})

def log_out(request):
   logout(request)
   return HttpResponseRedirect('/picwall/login/')

def register(request):
    if request.user.is_authenticated():
	return HttpResponseRedirect('/picwall/home/')

    register_prompt = ''
    if request.method == 'POST':
	name = request.POST['name']
	email = request.POST['email']
	pwd = request.POST['password']
	users1 = User.objects.filter(email = email)
	users2 = User.objects.filter(username = name)
	if len(users1) == 0:
	    if len(users2) == 0:
		user = User.objects.create_user(name, email, pwd)
		user.save()
		register_prompt = 'Succeed to register! Now Please log in!'
		user = authenticate(username = name, password = pwd)
		login(request, user)
		return HttpResponseRedirect('/picwall/home/')
	    else:
		register_prompt = 'The name have been registered!'
	else:
	    register_prompt = 'Your email have been registered!'
    return render(request, 'picwall/register.html', {'register_prompt':register_prompt,})
    
def upload_pic(request):
	if request.method == 'POST':
		name = request.POST['title']
		desc = request.POST['desc']
		author = request.user

		pic = Picture.objects.create_picture(name, author, desc)
		pic.save()
	
		# save image file
		image = request.FILES['pic']
		url = os.path.join(BASE_DIR, 'files/images/' + pic.file_name)
		fp = open(url, "ab")
		for chunk in image.chunks():  
			fp.write(chunk)  
		fp.close()   

	return HttpResponseRedirect('/picwall/home/')


def find_pic(request, file_name):
	image = open(os.path.join(BASE_DIR,'files/images/'+file_name), "rb").read()
	return HttpResponse(image)


def index_pic(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/picwall/login')
	pics = request.user.picture_set.all()
	return render(request, 'picwall/index.html', {'pics': pics, 'username': str(request.user),})

def index_picWall(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/picwall/login/')
	picwalls = PhotoWall.objects.filter(creator=request.user)
	return render(request, 'picwall/picwall_index.html', {'picwalls': picwalls, 'username': str(request.user),})

def pic_info(request, file_name):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/picwall/home')
	pic = get_object_or_404(Picture, file_name = file_name)
	comments = PictureComment.objects.filter(pic=pic)
	return render(request, 'picwall/comment.html', {'pic_info':pic,'comments':comments,})

def publish_comment(request):
    if request.method == 'POST':
	comment = PictureComment()
	comment.content = request.POST['content']
	comment.author = request.user
	pic = get_object_or_404(Picture, file_name = request.POST['file_name'])
	comment.pic = pic
	comment.published_date = date.today() 	
	comment.save()
	return HttpResponseRedirect('/picwall/pic_info/'+pic.file_name)

def return_pics(request):
	pics = []

	if request.user.is_authenticated():	
		user = request.user
	for pic in Picture.objects.filter(author=user):
		pics.append(pic.toDICT())
	return HttpResponse(json.dumps(pics))

def picwall_info(request, picwall_id):
    return render(request, 'picwall/photo.html', {})


def create_picwall(request):
	if request.method == 'POST':
		wall = PhotoWall()
		wall.name = request.POST['name']
		wall.description = request.POST['description']
		wall.creator = request.user
		wall.save()
		wall.access_users.add(request.user)
		wall.save()
	return HttpResponseRedirect('/picwall/home_walls/')


def get_photo_information_of_photo_wall(request):
	if request.method == 'GET':
		wid = request.GET['wid']
		wall = PhotoWall.objects.get(pk=wid)
		l = []
		for pic_in in PhotoInformation.objects.filter(photo_wall=wall):
			l.append(pic_in.toDICT())
		return HttpResponse(json.dumps(l))
	return HttpResponse("")

def view_photo_wall(request, photo_wall_id):
	wall = PhotoWall.objects.get(pk=photo_wall_id)
	pics = PhotoInformation.objects.filter(photo_wall=wall)
	l = []
	for pic in pics:
		l.append(pic.toDict())
	return HttpResponse(json.dumps(l))

def save_photo_wall(request):
	print request.method
	if request.method == 'POST':
		text = request.POST['text'];
		wid = request.POST['wid']
		wall = PhotoWall.objects.get(pk=wid)

		PhotoInformation.objects.filter(photo_wall=wall).delete()

		l = json.loads(text)
		for pic in l:
			x = pic['left']
			y = pic['top']
			pic = Picture.objects.get(file_name=pic['pid'])
			photo_infomation = PhotoInformation(picture=pic, photo_wall_id=wid, left=x, top=y)
			photo_infomation.save()
		return HttpResponse("Save OK!")
	elif request.method == 'GET':
		text = request.GET['text'];
		wid = request.GET['wid']
		wall = PhotoWall.objects.get(pk=wid)

		PhotoInformation.objects.filter(photo_wall=wall).delete()

		print text
		l = json.loads(text)
		print l
		cnt = 0
		for pic in l:
			cnt = cnt + 1
			print cnt
			x = pic['left']
			y = pic['top']
			w = pic['width']
			h = pic['height']
			pic = Picture.objects.get(file_name=pic['pid'])
			photo_infomation = PhotoInformation(picture=pic, photo_wall_id=wid, left=x, top=y, height=h, width=w)
			photo_infomation.save()
		return HttpResponse("Save OK!")
	return HttpResponse("Not valid method!")
