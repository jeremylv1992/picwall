from django.http import HttpResponse
from django.shortcuts import render

from photoWall.models import PhotoWall, PhotoImformation
from django.core import serializers

def index(request):
	return render(request, 'photoWall/index.html')

def get_photo_information_of_photo_wall(request, photo_wall_id):
	if request.method == 'POST':
		wall = PhotoWall.objects.get(pk=photo_wall_id)
		picture_information = PhotoImformation.objects.filter(photo_wall=wall)
		return HttpResponse(serializers.serialize("json", picture_information))
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
