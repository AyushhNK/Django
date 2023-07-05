from django.urls import path
from . import views		# importing views.py from the same directory

urlpatterns = [
    path(r'^$', views.article_list),
    path('<slug:slug>/', views.article_detail)
]
