from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate,logout
from .forms import SignUpForm

# Create your views here.
def home(request):
	
	user=request.user
	return render(request,"home.html",{"name":user})



def log_in(request):
	if request.method=="POST":
		form=AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username=form.cleaned_data["username"]
			password=form.cleaned_data["password"]
			user=authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect("home")
	else:
		form=AuthenticationForm()
	return render(request,"login.html",{"form":form})


def signup(request):
	if request.method=="POST":
		form=SignUpForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect("home")
	else:
		form=SignUpForm()
	return render(request,"signup.html",{"form":form})

def log_out(request):
	logout(request)
	return redirect('home')
