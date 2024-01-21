from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


# Create your views here.
def home(request):
	return HttpResponse("hello world")

class UserViewset(viewsets.ModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
