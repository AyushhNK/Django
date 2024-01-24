from django.urls import path,include
from . import views
from .views import BookViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('book',views.BookViewset,basename='book')
router.register('author',views.AuthorViewset,basename='author')

urlpatterns=[
	path("home/",views.home,name="home"),
	# path('view/',views.YourApiView.as_view(),name="view"),
	path('api/',include(router.urls))
]


