from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import UserProfileForm
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def home(request):
	return render(request,"home.html")

def LoginView(request):
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

def SignupView(request):
	if request.method=="POST":
		form=UserProfileForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form=UserProfileForm()
	return render(request,"signup.html",{"form":form})
def LogoutView(request):
	logout(request)
	return redirect("home")
