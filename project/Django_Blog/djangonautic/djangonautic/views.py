from django.http import HttpResponse

def home(Response):
	return HttpResponse("Home Page")

def about(Response):
	return HttpResponse("about page")