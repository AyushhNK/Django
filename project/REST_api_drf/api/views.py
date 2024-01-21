from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


# Create your views here.
def home(request):
	return HttpResponse("hello world")

class BookViewset(viewsets.ModelViewSet):
	queryset=Book.objects.all()
	serializer_class=BookSerializer
