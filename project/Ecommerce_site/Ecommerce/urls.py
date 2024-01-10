from django.urls import path
from . import views

urlpatterns=[
	path("",views.home,name="home"),
	path("login/",views.log_in,name="log_in"),
	path("signup/",views.signup,name="signup"),
	path("logout/",views.log_out,name="log_out")
]