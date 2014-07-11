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

APP_NAME = 'picwall'
ROOT_PATH = '/'+APP_NAME+'/'

CONTEXT = {
		'index_page': ROOT_PATH,

		'login_page': ROOT_PATH+'login/',
		'logout_page': ROOT_PATH+'logout/',
		'register_page': ROOT_PATH+'register/',

		'get_user_pics': ROOT_PATH+'user/pics/',
		'get_user_info': ROOT_PATH+'user/info/',

		'pic_index_page': ROOT_PATH+'picture/',
		'pic_info_page': ROOT_PATH+'picture/info/',
		'get_pic_info': ROOT_PATH+'picture/info/',
		'pic_image': ROOT_PATH+'picture/image/',
		'comment': ROOT_PATH+'picture/comment/',
		'upload_pic': ROOT_PATH+'picture/upload/',
		'delete_pic': ROOT_PATH+'picture/delete/',
		'edit_pic': ROOT_PATH+'picture/edit/',

		'pw_index_page': ROOT_PATH+'photowall/',
		'pw_info_page': ROOT_PATH+'photowall/info/',
		'create_pw': ROOT_PATH+'photowall/create/',
		'delete_pw': ROOT_PATH+'photowall/delete/',
		'edit_pw': ROOT_PATH+'photowall/edit/',

		# not used
		'make_friend': ROOT_PATH+'friend/create/',
		'delete_friend': ROOT_PATH+'friend/delete/',

		'base_page': APP_NAME+'/base.html',
		}

HOME_PAGE = CONTEXT['index_page']

TEMPLATE = {
		'index': APP_NAME+'/index.html',
		'login': APP_NAME+'/login.html',
		'register': APP_NAME+'/register.html',

		'pic_index': APP_NAME+'/picture_index.html',
		'pw_index': APP_NAME+'/photowall_index.html',
		'pic_info': APP_NAME+'/picture_info.html',
		'pw_info': APP_NAME+'/photowall_info.html',
		}

def get_user(user):
	if not user.is_authenticated():
		raise WebSiteUser.DoesNotExist
	return WebSiteUser.objects.get(user=user)

def return_origin_page(request):
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def index(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	hot_pws = PhotoWall.objects.get_hot_photowalls()
	random_pws = PhotoWall.objects.get_random_photowalls()
	new_pws = PhotoWall.objects.get_new_photowalls()

	context = CONTEXT
	context['user'] = user
	context['hot_pws'] = hot_pws
	context['random_pws'] = random_pws
	context['new_pws'] = new_pws

	return render(request, TEMPLATE['index'], context)

def picture_index(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	pics = Picture.objects.get_access_pictures(user)

	context = CONTEXT
	context['user'] = user
	context['pics'] = pics
	return render(request, TEMPLATE['pic_index'], context)

def photowall_index(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	private_pws = PhotoWall.objects.get_private_photowall(user)

	context = CONTEXT
	context['user'] = user
	context['private_pws'] = private_pws
	return render(request, TEMPLATE['pw_index'], context)

def log_in(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
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
		context['user'] = ''
		context['login_prompt'] = login_prompt;
		return render(request, TEMPLATE['login'], context)
	else:
		return HttpResponseRedirect(HOME_PAGE)

def log_out(request):
	logout(request)
	return HttpResponseRedirect(CONTEXT['login_page'])

def register(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		register_prompt = ''
		if request.method == 'POST':
			name = request.POST['name']
			email = request.POST['email']
			pwd = request.POST['password']
			users1 = User.objects.filter(email=email)
			users2 = User.objects.filter(username=name)

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
	else:
		return HttpResponseRedirect(HOME_PAGE)

def upload_pic(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	if request.method == 'POST':
		name = request.POST['name']
		description = request.POST['description']
		author = WebSiteUser.objects.get(user=request.user)

		pic = Picture.objects.create_picture(name, author, description)

		# save image file
		image = request.FILES['image']
		url = os.path.join(IMAGE_DIR, pic.pid)
		fp = open(url, "ab")
		for chunk in image.chunks():  
			fp.write(chunk)  
		fp.close()   

	return return_origin_page(request)

def edit_pic(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	if request.method == 'POST':
		pid = request.POST['pid']
		name = request.POST['name']
		description = request.POST['description']

		pic = Picture.objects.save_picture(pid, name, description)

	return return_origin_page(request)

def delete_pic(request, pid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	pic = get_object_or_404(Picture, pid=pid)
	url = os.path.join(IMAGE_DIR, pid)
	if os.path.isfile(url):
		os.remove(url)
	pic.delete()
	return return_origin_page(request)

def pic_image(request, pid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	image = open(os.path.join(IMAGE_DIR, pid), "rb").read()
	return HttpResponse(image)

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

def pic_info(request, pid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	pic = get_object_or_404(Picture, pid=pid)
	comments = PictureComment.objects.filter(pic=pic)

	context = CONTEXT
	context['pic'] = pic
	context['comments'] = comments
	context['user'] = user
	return render(request, TEMPLATE['pic_info'], context)

def pic_comment(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	if request.method == 'POST':
		pid = request.POST['pid']
		content = request.POST['content']
		comments = PictureComment.objects.create_picture_comment(user, pid, content)

	return return_origin_page(request)

def pw_info(request, wid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	photowall = get_object_or_404(PhotoWall, pk=wid)
	PhotoWall.objects.access_photowall(wid)

	context = CONTEXT
	context['user'] = user
	return render(request, TEMPLATE['pw_info'], context)

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

def edit_pw(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	if request.method == 'POST':
		wid = request.POST['wid']
		name = request.POST['name']
		description = request.POST['description']

		PhotoWall.objects.save_photowall(wid, name, description)

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
			pic = Picture.objects.get(pid=pic['pid'])
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
			pic = Picture.objects.get(pid=pic['pid'])
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

def get_user_info(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])
	return HttpResponse(user.toDICT())
	
def get_pic_info(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	if request.method == 'POST':
		pid = request.POST['pid']
		pic = get_object_or_404(Picture, pid=pid)
		return HttpResponse(json.dumps(pic.toDICT()))

	return HttpResponse("")

def get_pw_info(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(CONTEXT['login_page'])

	if request.method == 'POST':
		wid = request.POST["wid"]
		wall = get_object_or_404(PhotoWall, pk=wid)
		return HttpResponse(json.dumps(wall.toDICT()))

	return HttpResponse("")
