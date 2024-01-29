from django.urls import path
from . import views

urlpatterns=[

	# home route
	path('',views.home,name="home"),

	# authentication routes
	path("login/",views.LoginView,name="login"),
	path("signup/",views.SignupView,name="signup"),
	path("logout/",views.LogoutView,name="logout"),

	# post related routes
	path("like/<int:post_id>/",views.LikeView,name="like"),
	path("comment/<int:post_id>/",views.CommentView,name="comment"),
	path("commentslookup/<int:post_id>/",views.CommentLookupView,name="comments"),
	path("createpost/",views.CreatePostView,name="createpost"),
	path("deletepost/<int:post_id>/",views.DeletePostView,name="deletepost"),

	# friend request related routes
	path("sendrequest/<int:receiver_id>/",views.SendRequestView,name="sendrequest"),
	path("acceptrequest/<int:sender_id>/",views.AcceptRequestView,name="acceptrequest"),
	path("friendrequest/",views.FriendRequestView,name="friendrequest"),
]