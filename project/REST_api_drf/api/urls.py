from django.urls import path,include
from . import views
from .views import UserViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('users',views.UserViewset,basename='Userst')

urlpatterns=[
	path("home/",views.home,name="home"),
	path('',include(router.urls))
]