from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

import requests,json


def Home(request):
	url = "http://api.weatherstack.com/current?access_key=0eabdf865a795131eff89ba1511c0baa&query=Kathmandu"
	Response = requests.get(url)
	data=Response.json()
	
	icon=data["current"]["weather_icons"][0]


	# return JsonResponse(data)
	return render(request,"home.html",{"icon":icon,
		"city":data["location"]["name"]})




