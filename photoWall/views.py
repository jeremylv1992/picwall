from django.http import HttpResponse
from django.shortcuts import render

import simplejson as json

from photoWall.models import PhotoWall, PhotoInformation
from django.core import serializers

def index(request):
	return render(request, 'photoWall/index.html')

def get_photo_information_of_photo_wall(request, photo_wall_id):
	if request.method == 'GET':
		wall = PhotoWall.objects.get(pk=photo_wall_id)
		picture_information = PhotoInformation.objects.filter(photo_wall=wall)
		return HttpResponse(serializers.serialize("json", wall))
	return HttpResponse("")

def create_photo_wall(request):
	if request.method == 'POST':
		wall = PhotoWall()
		wall.name = request.POST['name']
		wall.description = request.POST['description']
		wall.creator = request.user
		wall.access_users.add(request.user)
		wall.save()
		return HttpResponse("create sucess")
	return HttpResponse("create fail")

def view_photo_wall(request, photo_wall_id):
	wall = PhotoWall.objects.get(pk=photo_wall_id)
	pics = PhotoInformation.objects.filter(photo_wall=wall)

	l = []
	for pic in pics:
		l.append(pic.toDict())

	return HttpResponse(json.dumps(l))

def save_photo_wall(request)
	if request.method == 'POST':
		text = request.POST['text'];
		wall_id = request.POST['photo_wall_id']
		wall = request.
		photo_infomation_id = request.POST['id']
		photo_infomation = PhotoInformation.objects.get(pk=photo_infomation_id)
		positionX = request.POST['positionX']
		positionY = request.POST['positionY']
		photo_infomation.positionX = positionX
		photo_infomation.positionX = positionY
		photo_infomation.save()
		return HttpResponse("Save OK!")
	return HttpResponse("Not POST!")
