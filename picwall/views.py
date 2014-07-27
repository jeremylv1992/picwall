from __future__ import division
import django
from django.db import models
from django.utils.timezone import utc
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core import serializers
from datetime import datetime
from datetime import date

from picwall.models import Picture, PictureComment, PhotoWall, PhotoInformation, PhotoInformation, WebSiteUser, PictureLabel, AskForFriendMessage, PhotowallComment

from myForms import Login_Form

import time
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'files/images/')
PICTURE_DIR = os.path.join(IMAGE_DIR, 'picture/')
PHOTOWALL_DIR = os.path.join(IMAGE_DIR, 'photowall/')

APP_NAME = 'picwall'
ROOT_PATH = '/'+APP_NAME+'/'

LOGIN_PAGE = ROOT_PATH+'login/'
INDEX_PAGE = ROOT_PATH

TEMPLATES = {
		'index': APP_NAME+'/index.html',
		'login': APP_NAME+'/login.html',
		'register': APP_NAME+'/register.html',

		'user_index': APP_NAME+'/user_index.html',
		'pic_index': APP_NAME+'/picture_index.html',
		'pw_index': APP_NAME+'/photowall_index.html',
		'friend_index': APP_NAME+'/friend_index.html',
		'pic_info': APP_NAME+'/picture_info.html',
		'pw_info': APP_NAME+'/photowall_info_edit.html',
		'pw_view': APP_NAME+'/photowall_info.html',
}

class CJsonEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj, date):
			return obj.strftime('%Y-%m-%d')
		elif isinstance(obj, models.Model):
			return obj.__unicode__()
		else:
			return json.JSONEncoder.default(self, obj)

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
		return HttpResponseRedirect(LOGIN_PAGE)

	hot_pws = PhotoWall.objects.get_hot_photowalls(user)
	random_pws = PhotoWall.objects.get_random_photowalls(user)
	new_pws = PhotoWall.objects.get_new_photowalls(user)

	context = {}
	context['user'] = user
	context['hot_pws'] = hot_pws
	context['random_pws'] = random_pws
	context['new_pws'] = new_pws

	return render(request, TEMPLATES['index'], context)

def picture_index(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	labels = user.user_labels

	context = {}
	context['user'] = user
	context['labels'] = labels
	return render(request, TEMPLATES['pic_index'], context)

def photowall_index(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	private_pws = PhotoWall.objects.get_private_photowall(user)
	temp_pws = PhotoWall.objects.get_manage_photowalls(user)
	manage_pws = PhotoWall.objects.get_manage_photowalls(user)
	access_pws = PhotoWall.objects.get_access_photowalls(user)
	friends = user.friends

	context = {}
	context['user'] = user
	context['private_pws'] = private_pws
	context['manage_pws'] = manage_pws
	context['access_pws'] = access_pws
	context['friends'] = friends
	return render(request, TEMPLATES['pw_index'], context)

def friend_index(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	friends = user.friends

	recommend_users = WebSiteUser.objects.get_recommend(user)

	context = {}
	context['user'] = user
	context['friends'] = friends
	context['recommend_users'] = recommend_users
	return render(request, TEMPLATES['friend_index'], context)

def user_index(request, uid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	owner = get_object_or_404(WebSiteUser, pk=uid)
	pws = user.access_pws.filter(creator=owner)

	received_messages = user.received_messages
	sent_messages = user.sent_messages

	context = {}
	context['user'] = user
	context['pws'] = pws
	context['owner'] = owner
	context['received_messages'] = received_messages
	context['sent_messages'] = sent_messages
	return render(request, TEMPLATES['user_index'], context)

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
						return HttpResponseRedirect(INDEX_PAGE)
					else:
						login_promt = 'Invalid user'
				else:
					login_prompt = 'Password is wrong'
			else:
				login_prompt = 'E-mail is invalid'

		context = {}
		context['user'] = ''
		context['login_prompt'] = login_prompt;
		return render(request, TEMPLATES['login'], context)
	else:
		return HttpResponseRedirect(INDEX_PAGE)

def log_out(request):
	logout(request)
	return HttpResponseRedirect(LOGIN_PAGE)

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
					return HttpResponseRedirect(INDEX_PAGE)
				else:
					register_prompt = 'The name have been registered!'
			else:
				register_prompt = 'Your email have been registered!'

		context = {}
		context['user'] = ''
		context['register_prompt'] = register_prompt
		return render(request, TEMPLATES['register'], context)
	else:
		return HttpResponseRedirect(INDEX_PAGE)

def upload_pic(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'POST':
		name = request.POST['name']
		description = request.POST['description']
		author = WebSiteUser.objects.get(user=request.user)
		lid = request.POST['label']
		label = PictureLabel.objects.get(pk=lid)

		pic = Picture.objects.create_picture(name, author, description, label)

		# save image file
		image = request.FILES['image']
		url = os.path.join(PICTURE_DIR, str(pic.id))
		fp = open(url, "ab")
		for chunk in image.chunks():  
			fp.write(chunk)  
		fp.close()   

	return return_origin_page(request)

def edit_pic(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'POST':
		pic = get_object_or_404(Picture, pk=request.POST['pid'])
		name = request.POST['name']
		description = request.POST['description']
		lid = request.POST['label']
		label = PictureLabel.objects.get(pk=lid)

		if user != pic.author:
			return return_origin_page(request);

		Picture.objects.save_picture(pic, name, description, label)

	return return_origin_page(request)

def delete_pic(request, pid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	pic = get_object_or_404(Picture, pk=pid)

	if user != pic.author:
		return return_origin_page(request)

	pic_file = os.path.join(PICTURE_DIR, str(pid))
	if os.path.isfile(pic_file):
		os.remove(pic_file)
	pic.delete()

	return return_origin_page(request)

def pic_image(request, pid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	image = open(os.path.join(PICTURE_DIR, str(pid)), "rb").read()
	return HttpResponse(image)

def pw_image(request, wid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	image = open(os.path.join(PHOTOWALL_DIR, str(wid)), "rb").read()
	return HttpResponse(image)

def get_user_pics(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	pics = []

	if not request.user.is_authenticated():
		return HttpResponseRedirect(LOGIN_PAGE)
	try:
		user = WebSiteUser.objects.get(user=request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	for pic in Picture.objects.filter(author=user):
		pics.append(pic.toDICT())

	return HttpResponse(json.dumps(pics, cls=CJsonEncoder))

def pic_info(request, pid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	pic = get_object_or_404(Picture, pk=pid)
	comments = PictureComment.objects.filter(pic=pic)

	context = {}
	context['pic'] = pic
	context['comments'] = comments
	context['user'] = user
	return render(request, TEMPLATES['pic_info'], context)

def pic_comment(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'POST':
		pid = request.POST['pid']
		content = request.POST['content']
		comment = PictureComment.objects.create_picture_comment(user, pid, content)

	return return_origin_page(request)

def pw_comment(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'POST':
		pw = get_object_or_404(PhotoWall, pk=request.POST['wid'])
		content = request.POST['content']

		if user not in pw.access_users.all():
			return return_origin_page(request)

		comment = PhotowallComment.objects.create_photowall_comment(user, pw, content)
	
	return return_origin_page(request)


def pw_info(request, wid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	pw = get_object_or_404(PhotoWall, pk=wid)

	if user not in pw.access_users.all():
		return return_origin_page(request);

	context = {}
	context['user'] = user
	return render(request, TEMPLATES['pw_info'], context)

def pw_view(request, wid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	pw = get_object_or_404(PhotoWall, pk=wid)

	if user not in pw.access_users.all():
		return return_origin_page(request);

	PhotoWall.objects.access_photowall(pw)

	comments = PhotowallComment.objects.filter(pw=pw)

	context = {}
	context['user'] = user
	context['pw'] = pw
	context['comments'] = comments
	return render(request, TEMPLATES['pw_view'], context)

def create_pw(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

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
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'POST':
		wid = request.POST['wid']
		name = request.POST['name']
		description = request.POST['description']
		pw = get_object_or_404(PhotoWall, pk=wid)

		if user not in pw.access_users.all():
			return return_origin_page(request)

		PhotoWall.objects.save_photowall(pw, name, description)

	return return_origin_page(request)

def get_pics_of_pw(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'GET':
		pw = get_object_or_404(PhotoWall, pk=request.GET['wid'])

		if user not in pw.access_users.all():
			return HttpResponse("")

		l = []
		for pic_in in PhotoInformation.objects.filter(photowall=pw):
			l.append(pic_in.toDICT())
		return HttpResponse(json.dumps(l, cls=CJsonEncoder))

	return HttpResponse("")

def save_pw(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'GET' or request.method == 'POST':
		import base64
		if request.method == 'GET':
			text = request.GET['text'];
			wid = request.GET['wid']
			imageData = base64.b64decode(request.GET['data'])
		else:
			text = request.POST['text'];
			wid = request.POST['wid']
			imageData = base64.b64decode(request.POST['data'])
		pw = PhotoWall.objects.get(pk=wid)

		if user not in pw.manage_users.all():
			return HttpResponse("You can't save the photowall!");

		imageFile = open(PHOTOWALL_DIR+wid, "wb")
		imageFile.write(imageData)
		imageFile.close()

		PhotoInformation.objects.filter(photowall=pw).delete()

		l = json.loads(text)
		for pic in l:
			left = pic['left']
			top = pic['top']
			width = pic['width']
			height = pic['height']
			pic = Picture.objects.get(pk=pic['pid'])
			PhotoInformation.objects.create_photowall_information(pic, pw, left, top, width, height)

		pw.modify_date = datetime.now()
		pw.save()
		return HttpResponse("Save OK!")
	return HttpResponse("Not valid method!")

def delete_pw(request, wid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	wall = get_object_or_404(PhotoWall, pk=wid)

	if user != wall.creator:
		return return_origin_page(request);

	imageUrl = os.path.join(PHOTOWALL_DIR, str(wall.id))
	if os.path.isfile(imageUrl):
		os.remove(imageUrl)
	wall.delete()

	return return_origin_page(request)

def delete_friend(request, uid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	user1 = get_object_or_404(WebSiteUser, user=request.user)
	user2 = get_object_or_404(WebSiteUser, pk=uid)

	if user1 is not None and user2 is not None:
		if user2 in user1.friends.all():
			user1.friends.remove(user2)
			user2.friends.remove(user1)
			for pw in user1.photowalls.all():
				if pw.access_permission == PhotoWall.FRIEND:
					pw.access_users.remove(user2)
				if user2 in pw.manage_users.all():
					pw.manage_users.remove(user2)
			for pw in user2.photowalls.all():
				if pw.access_permission == PhotoWall.FRIEND:
					pw.access_users.remove(user1)
				if user1 in pw.manage_users.all():
					pw.manage_users.remove(user1)

	return return_origin_page(request)

def get_user_info(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)
	return HttpResponse(user.toDICT())

def get_pic_info(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'POST':
		pid = request.POST['pid']
		pic = get_object_or_404(Picture, pk=pid)
		return HttpResponse(json.dumps(pic.toDICT(), cls=CJsonEncoder))

	return HttpResponse("")

def get_pw_info(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'POST':
		pw = get_object_or_404(PhotoWall, pk=request.POST['wid'])

		if user not in pw.manage_users.all():
			return return_origin_page(request)

		return HttpResponse(json.dumps(pw.toDICT(), cls=CJsonEncoder))

	return HttpResponse("")

def get_users(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'GET':
		text = request.GET['username']
		users = User.objects.filter(username__icontains=text).exclude(username='root')
		recommend_users = WebSiteUser.objects.get_recommend(user)

		context = {}
		context['user'] = user;
		context['search_users'] = users
		context['recommend_users'] = recommend_users
		return render(request, TEMPLATES['friend_index'], context)

	return return_origin_page(request)

def get_pw_permission(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'POST':
		wid = request.POST['wid']
		pw = get_object_or_404(PhotoWall, pk=wid)

		if user != pw.creator:
			return return_origin_page(request)

		if user == pw.creator:
			data = {
					"access_permission": pw.access_permission,
					}
			l = []
			for manager in pw.manage_users.all():
				if manager != pw.creator:
					l.append({"id": str(manager.id), "isManager": True})
			for friend in user.friends.all():
				if friend not in pw.manage_users.all():
					l.append({"id": str(manager.id), "isManager": False})
			data["managers"] = l
			return HttpResponse(json.dumps(data, cls=CJsonEncoder))

	return return_origin_page(request)

def set_pw_permission(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'POST':
		wid = request.POST['wid']
		pw = get_object_or_404(PhotoWall, pk=wid)
		if user != pw.creator:
			return return_origin_page(request)

		pw.access_users.clear()
		access_permission = request.POST['access-permission']
		if access_permission == 'private':
			pw.access_permission = PhotoWall.PRIVATE
			pw.access_users.add(user)
		if access_permission == 'friend':
			pw.access_permission = PhotoWall.FRIEND
			pw.access_users.add(user)
			for friend in user.friends.all():
				pw.access_users.add(friend)
		if access_permission == 'public':
			pw.access_permission = PhotoWall.PUBLIC
			for user in WebSiteUser.objects.all():
				pw.access_users.add(user)

		pw.manage_users.clear()
		pw.manage_users.add(user)
		manage_permission = request.POST.getlist('manager')
		for uid in manage_permission:
			member = get_object_or_404(WebSiteUser, pk=uid)
			pw.manage_users.add(member)

		pw.save()

	return return_origin_page(request);

def create_label(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == 'POST':
		name = request.POST['name']
		label = PictureLabel.objects.create_label(user, name)

	return return_origin_page(request)

def get_user_message(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	rcv_msgs = user.received_messages
	snd_msgs = user.sent_messages

	data = {"rcv_msgs": rcv_msgs, "snd_msgs": snd_msgs}

	return HttpResponse(json.dumps(data, cls=JSONEncoder));

def send_message(request, uid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	sender = user
	receiver = get_object_or_404(WebSiteUser, pk=uid)

	if sender != receiver:
		msg = AskForFriendMessage.objects.create_message(sender, receiver)

	return return_origin_page(request)

def ignore_message(request, mid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	msg = get_object_or_404(AskForFriendMessage, pk=mid)

	sender = msg.sender
	receiver = msg.receiver

	if user != receiver:
		return return_origin_page(request)

	if msg.state == AskForFriendMessage.WAIT:
		msg.state = AskForFriendMessage.REJECT
		msg.save()

	return return_origin_page(request)

def make_friend(request, mid):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	msg = get_object_or_404(AskForFriendMessage, pk=mid)
	sender = msg.sender
	receiver = msg.receiver

	if user != receiver:
		return return_origin_page(request)

	if receiver is not None and sender is not None and msg.state == AskForFriendMessage.WAIT:
		if receiver not in sender.friends.all():
			receiver.friends.add(sender)
			sender.friends.add(receiver)

			receiver.save()
			sender.save()

			for pw in receiver.photowalls.all():
				if pw.access_permission == PhotoWall.FRIEND and sender not in pw.access_users.all():
					pw.access_users.add(sender)
					pw.save()

			for pw in sender.photowalls.all():
				if pw.access_permission == PhotoWall.FRIEND and receiver not in pw.access_users.all():
					pw.access_users.add(receiver)
					pw.save()

			msg.state = AskForFriendMessage.ACCEPT
			msg.save()

	return return_origin_page(request)

def cancel_visble(request):
	try:
		user = get_user(request.user)
	except WebSiteUser.DoesNotExist:
		return HttpResponseRedirect(LOGIN_PAGE)

	if request.method == "POST":
		msg = get_object_or_404(AskForFriendMessage, pk=request.POST['mid'])

		if user == msg.sender:
			msg.sender_visible = False
		elif user == msg.receiver:
			msg.receiver_visible = False

		if not msg.sender_visible and not receiver_visible:
			msg.delete()
		else:
			msg.save()

	return HttpResponse("OK!")
