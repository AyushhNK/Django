from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import Book,Author
from .serializers import BookSerializer,AuthorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication


# Create your views here.
def home(request):
	return HttpResponse("hello world")

class BookViewset(viewsets.ModelViewSet):
	queryset=Book.objects.all()
	serializer_class=BookSerializer
	permission_classes=[IsAuthenticated]
	authentication_classes=(TokenAuthentication,)

class AuthorViewset(viewsets.ModelViewSet):
	queryset=Author.objects.all()
	serializer_class=AuthorSerializer
	permission_class=[]
	authentication_class=[]
