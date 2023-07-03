from django.urls import path
from . import views		# importing views.py from the same directory

urlpatterns = [
    path('',views.article_list)	
]
