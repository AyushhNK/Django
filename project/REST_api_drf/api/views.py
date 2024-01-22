from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import Book,Author
from .serializers import BookSerializer,AuthorSerializer


# Create your views here.
def home(request):
	return HttpResponse("hello world")

class BookViewset(viewsets.ModelViewSet):
	queryset=Book.objects.all()
	serializer_class=BookSerializer

class AuthorViewset(viewsets.ModelViewSet):
	queryset=Author.objects.all()
	serializer_class=AuthorSerializer