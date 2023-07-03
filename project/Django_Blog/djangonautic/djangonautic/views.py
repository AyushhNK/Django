from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	# return HttpResponse("Home Page")
	return render(request,"homepage.html")

def about(request):
	# return HttpResponse("about page")
	return render(request,"aboutpage.html")