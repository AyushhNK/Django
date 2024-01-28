from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import UserProfileForm,CreatePostForm
from django.contrib.auth import login,authenticate,logout
from .models import Post,Like,FriendRequest,UserProfile
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	posts=Post.objects.all()
	user=User.objects.all()
	return render(request,"home.html",{"posts":posts,"user":user})

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

def LikeView(request,post_id):
	user=request.user
	post=get_object_or_404(Post,id=post_id)
	like,created=Like.objects.get_or_create(user=user,post=post)
	if not created:
		like.delete()
	return redirect("home")

def CreatePostView(request):
	if request.method=="POST":
		form=CreatePostForm(request.POST)
		if form.is_valid():
			form=form.save(commit=False)
			form.user=request.user
			form.save()
			return redirect("home")
	else:
		form=CreatePostForm()
	return render(request,"createpost.html",{"form":form})

def DeletePostView(request,post_id):
	post=Post.objects.get(id=post_id)
	post.delete()
	return redirect("home")

def SendRequestView(request,receiver_id):
	from_user=request.user
	to_user=User.objects.get(id=receiver_id)
	FriendRequest.objects.create(from_user=from_user,to_user=to_user)
	return redirect("home")

def AcceptRequestView(request,sender_id):
	from_user=User.objects.get(id=sender_id)
	request=FriendRequest.objects.get(to_user=request.user,from_user=from_user)
	request.accepted=True
	request.save()
	return redirect("friendrequest")


def FriendRequestView(request):
	requests=FriendRequest.objects.filter(to_user=request.user)
	return render(request,"friendrequest.html",{"requests":requests})





