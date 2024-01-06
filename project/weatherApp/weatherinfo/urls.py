from django.urls import path
from . import views

urlpatterns=[
	path('',views.Home),
	path('weather_detail/',views.weather_detail)
]