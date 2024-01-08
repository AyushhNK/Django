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
	city=data["location"]["name"]
	time=data["location"]["localtime"]
	country=data["location"]["country"]
	temperature=data["current"]["temperature"]
	weather_desc=data["current"]["weather_descriptions"][0]
	precip=data["current"]["precip"]


	# return JsonResponse(data)
	return render(request,"weather_detail.html",{"icon":icon,
		"city":city,
		"time":time,
		"country":country,
		"temperature":temperature,
		"weather_desc":weather_desc,
		"precip":precip})



