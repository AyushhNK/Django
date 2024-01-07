from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .form import CityName 

# Create your views here.

import requests,json


def Home(request):
	form=CityName()
	return render(request,"home.html",{"form":form})



def weather_detail(request):

	if request.method=="POST":
		form=CityName(request.POST)
		cityname=form["city"].value()

	url = "http://api.weatherstack.com/current?access_key=0eabdf865a795131eff89ba1511c0baa&query="+cityname
	Response = requests.get(url)
	data=Response.json()
	
	icon=data["current"]["weather_icons"][0]


	# return JsonResponse(data)
	return render(request,"weather_detail.html",{"icon":icon,
		"city":data["location"]["name"]})



