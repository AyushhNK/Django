from django.contrib import admin
from django.urls import path,include
from . import views		# importing views.py from the same directory
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('articles/',include('articles.urls')),	#registering the urls of the articles app
    path('about/',views.about),		#url route which sends about function from views.py
    path('',views.home)				#url route which sends home function from views.py
]


urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)