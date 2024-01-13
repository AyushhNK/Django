from django.shortcuts import render,redirect
from .forms import SignupForm
# Create your views here.
# views.py
from django.contrib.auth.views import PasswordResetDoneView

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


def signup(request):
	if request.method=='POST':
		form=SignupForm(request.POST)
		form.save()
		return redirect('login')
	else:
		form=SignupForm()
	return render(request,'registration/signup.html',{'form':form})