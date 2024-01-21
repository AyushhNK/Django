from django.urls import path,include
from . import views
from .views import BookViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('book',views.BookViewset,basename='book')

urlpatterns=[
	path("home/",views.home,name="home"),
	path('',include(router.urls))
]