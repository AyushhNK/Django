from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import Book,Author
from .serializers import BookSerializer,AuthorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response


# Create your views here.
def home(request):
	return HttpResponse(request.user)

class BookViewset(viewsets.ModelViewSet):
	queryset=Book.objects.all()
	serializer_class=BookSerializer
	
	authentication_classes=[TokenAuthentication,]
	permission_classes=[IsAuthenticated,]
	

class AuthorViewset(viewsets.ModelViewSet):
	queryset=Author.objects.all()
	serializer_class=AuthorSerializer
	authentication_classes=[TokenAuthentication,]
	permission_classes=[IsAuthenticated,]
	


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class YourApiView(APIView):
    def get(self, request, *args, **kwargs):
        # Your view logic here
        return Response({"message": "Authenticated API view"})
