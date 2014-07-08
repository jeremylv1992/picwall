# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core import serializers
from datetime import date

from picwall.models import Picture, PictureComment, PhotoWall, PhotoInformation, PhotoInformation, WebSiteUser

from myForms import Login_Form

import time
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'files/images/')

CONTEXT = {
		'picture_page': '/picwall/picture/',
		'photowall_page': '/picwall/photowall/',

		'login_page': '/picwall/login/',
		'logout_page': '/picwall/logout/',
		'register_page': '/picwall/register/',

		'picture_info_page': '/picwall/picture/info/',
		'photowall_info_page': '/picwall/photowall/info/',

		'comment': '/picwall/picture/comment/',
		'create_photowall': '/picwall/photowall/create/',
		'upload_pictrue': '/picwall/picture/upload/'
		}

HOME_PAGE = CONTEXT['picture_page']

TEMPLATE = {
		'login': 'picwall/login.html',
		'register': 'picwall/register.html',
		'picture': 'picwall/picture_index.html',
		'photowall': 'picwall/photowall_index.html',
		'pic_info': 'picwall/picture_info.html',
		'pw_info': 'picwall/photowall_info.html',
		}

def get_user(user):
	if not user.is_authenticated():
		raise WebSiteUser.DoesNotExist
	return WebSiteUser.objects.get(user=user)

def return_origin_page(request):
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def index(request):
	return HttpResponse('Hello Picturewall!')

def log_in(request):

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
					return HttpResponseRedirect(HOME_PAGE)
				else:
					login_promt = 'Invalid user'
			else:
				login_prompt = 'Password is wrong'
		else:
			login_prompt = 'E-mail is invalid'

	context = CONTEXT;
	context['login_prompt'] = login_prompt;
	return render(request, TEMPLATE['login'], context)

def log_out(request):
	logout(request)
	return HttpResponseRedirect(CONTEXT['login_page'])

def register(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

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
				webuser = WebSiteUser.objects.create_user(user)
	
				register_prompt = 'Succeed to register! Now Please log in!'
				user = authenticate(username = name, password = pwd)
				login(request, user)
				return HttpResponseRedirect(HOME_PAGE)
			else:
				register_prompt = 'The name have been registered!'
		else:
			register_prompt = 'Your email have been registered!'

	context = CONTEXT
	context['register_prompt'] = register_prompt
	return render(request, TEMPLATE['register'], context)

def upload_pic(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	if request.method == 'POST':
		name = request.POST['title']
		desc = request.POST['desc']
		author = WebSiteUser.objects.get(user=request.user)

		pic = Picture.objects.create_picture(name, author, desc)
		pic.save()

		# save image file
		image = request.FILES['pic']
		url = os.path.join(IMAGE_DIR, pic.file_name)
		fp = open(url, "ab")
		for chunk in image.chunks():  
			fp.write(chunk)  
		fp.close()   

	return return_origin_page(request)

def delete_pic(request, file_name):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	pic = get_object_or_404(Picture, file_name=file_name)
	pic.delete()
	return return_origin_page(request)

def pic_image(request, file_name):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	image = open(os.path.join(IMAGE_DIR, file_name), "rb").read()
	return HttpResponse(image)

def pic_index(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	pics = Picture.objects.filter(author=user)

	context = CONTEXT
	context['pics'] = pics
	context['username'] = str(user)
	return render(request, TEMPLATE['picture'], context)

def pw_index(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])
	else:
		photowalls = PhotoWall.objects.get_access_photowall(user)

		context = CONTEXT
		context['photowalls'] = photowalls
		context['user'] = user
		return render(request, TEMPLATE['photowall'], context)

# pictures
def get_user_pics(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	pics = []

	if not request.user.is_authenticated():
		return HttpResponseRedirect(CONTEXT['login_page'])
	try:
		user = WebSiteUser.objects.get(user=request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	for pic in Picture.objects.filter(author=user):
		pics.append(pic.toDICT())

	return HttpResponse(json.dumps(pics))

def pic_info(request, file_name):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])


	pic = get_object_or_404(Picture, file_name = file_name)
	comments = PictureComment.objects.filter(pic=pic)

	context = CONTEXT
	context['pic'] = pic
	context['comments'] = comments
	return render(request, TEMPLATE['pic_info'], context)

# picture comment
def pic_comment(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	if request.method == 'POST':
		comment = PictureComment()
		comment.content = request.POST['content']
		comment.author = get_object_or_404(WebSiteUser, user=request.user)
		pic = get_object_or_404(Picture, file_name=request.POST['file_name'])
		comment.pic = pic
		comment.published_date = date.today() 	
		comment.save()

	return return_origin_page(request)

# photo wall
def pw_info(request, wid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	photowall = get_object_or_404(PhotoWall, pk=wid)
	return render(request, TEMPLATE['pw_info'], CONTEXT)

def create_pw(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	if request.method == 'POST':
		name = request.POST['name']
		description = request.POST['description']
		creator = get_object_or_404(WebSiteUser, user=request.user)
		PhotoWall.objects.create_photowall(name, description, creator)

	return return_origin_page(request)

def get_pics_of_pw(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	if request.method == 'GET':
		wid = request.GET['wid']
		wall = get_object_or_404(PhotoWall, pk=wid)
		l = []
		for pic_in in PhotoInformation.objects.filter(photowall=wall):
			l.append(pic_in.toDICT())
		return HttpResponse(json.dumps(l))

	return HttpResponse("")

def view_pw(request, photowall_id):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	wall = PhotoWall.objects.get(pk=photowall_id)
	pics = PhotoInformation.objects.filter(photowall=wall)
	l = []
	for pic in pics:
		l.append(pic.toDict())
	return HttpResponse(json.dumps(l))

def save_pw(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	if request.method == 'POST':
		text = request.POST['text'];
		wid = request.POST['wid']
		wall = PhotoWall.objects.get(pk=wid)

		PhotoInformation.objects.filter(photowall=wall).delete()

		l = json.loads(text)
		for pic in l:
			x = pic['left']
			y = pic['top']
			pic = Picture.objects.get(file_name=pic['pid'])
			photo_infomation = PhotoInformation(picture=pic, photowall_id=wid, left=x, top=y)
			photo_infomation.save()
		return HttpResponse("Save OK!")
	elif request.method == 'GET':
		text = request.GET['text'];
		wid = request.GET['wid']
		wall = PhotoWall.objects.get(pk=wid)

		PhotoInformation.objects.filter(photowall=wall).delete()

		l = json.loads(text)
		for pic in l:
			x = pic['left']
			y = pic['top']
			w = pic['width']
			h = pic['height']
			pic = Picture.objects.get(file_name=pic['pid'])
			photo_infomation = PhotoInformation(picture=pic, photowall_id=wid, left=x, top=y, height=h, width=w)
			photo_infomation.save()
		return HttpResponse("Save OK!")
	return HttpResponse("Not valid method!")

def delete_pw(request, wid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	wall = get_object_or_404(PhotoWall, pk=wid)
	wall.delete()

	return return_origin_page(request)

def make_friend(request, user_name):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	user1 = get_object_or_404(WebSiteUser, user=request.user)
	user2 = get_object_or_404(WebSiteUser, name=get_object_or_404(name=user_name))

	if user1 is None or user2 is None:
		return HttpResponse("Not valide")
	else:
		if user2 not in user1.friends.all():
			user1.frinds.add(user2)
		if user1 not in user2.friends.all():
			user2.frinds.add(user1)
		return HttpResponse("Make friend sceuss")

def delete_friend(request, user_name):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	user1 = get_object_or_404(WebSiteUser, user=request.user)
	user2 = get_object_or_404(WebSiteUser, name=get_object_or_404(name=user_name))

	if user1 is None or user2 is None:
		return HttpResponse("Not valide")
	else:
		if user2 in user1.friends.all():
			user1.frinds.remove(user2)
		if user1 in user2.friends.all():
			user2.frinds.remove(user1)
		return HttpResponse("Make friend sceuss")
