from django.urls import path
from . import views

urlpatterns=[
	path('',views.home,name="home"),
	path("login/",views.LoginView,name="login"),
	path("signup/",views.SignupView,name="signup"),
	path("logout/",views.LogoutView,name="logout"),
	path("like/<int:post_id>/",views.LikeView,name="like"),
	path("createpost/",views.CreatePostView,name="createpost"),
	path("deletepost/<int:post_id>/",views.DeletePostView,name="deletepost"),
	path("sendrequest/<int:receiver_id>/",views.SendRequestView,name="sendrequest"),
	path("acceptrequest/<int:sender_id>/",views.AcceptRequestView,name="acceptrequest"),
	path("friendrequest/",views.FriendRequestView,name="friendrequest"),
]