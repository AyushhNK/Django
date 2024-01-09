from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
	if request.method=="POST":
		form=SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			user=User.objects.get(username=form['username'].value())
			user.is_staff=True
			user.save()
			return redirect('signup')
	else:	
		form=SignUpForm()
	return render(request,"signup.html",{"form":form})

def logins(request):
	if request.method=="POST":
		form=AuthenticationForm(request,data=request.POST)
		
		if form.is_valid():
			username=form.cleaned_data["username"]
			password=form.cleaned_data["password"]
			user=authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				name=request.user.username
				return render(request,"login.html",{"user":name})
	else:	
		form=AuthenticationForm()
	return render(request,"login.html",{"form":form})