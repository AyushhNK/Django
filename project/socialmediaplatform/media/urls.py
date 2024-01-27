from django.urls import path
from . import views

urlpatterns=[
	path('home/',views.home,name="home"),
	path("login/",views.LoginView,name="login"),
	path("signup/",views.SignupView,name="signup"),
	path("logout/",views.LogoutView,name="logout")
]