from django.contrib import admin
from django.urls import path
from . import views		# importing views.py from the same directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about),		#url route which sends about function from views.py
    path('',views.home)				#url route which sends home function from views.py
]
