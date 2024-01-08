from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth.models import User

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
