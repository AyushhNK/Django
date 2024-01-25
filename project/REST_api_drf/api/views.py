from django.shortcuts import render,HttpResponse
from rest_framework import viewsets,status
from .models import Book,Author
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.models import Token
from .serializers import BookSerializer,AuthorSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


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
	

class SignupView(APIView):
	permission_classes=[AllowAny]
	def post(self,request):
		username=request.data.get("username")
		email=request.data.get("email")
		password=request.data.get("password")
		if not username or not email or not password:
			return Response({"error":"please provide username email and password"})
		user=User.objects.create_user(username=username,password=password,email=email)
		serializer=UserSerializer(user)
		return Response(serializer.data,status=status.HTTP_201_CREATED)

@swagger_auto_schema(
    operation_description="login to your account.",
    responses={200: 'OK'},
)
class LoginView(APIView):
	def post(self,request):
		username=request.data.get("username")
		password=request.data.get("password")
		user=authenticate(request,username=username,password=password)

		if user:
			login(request,user)
			serializer=UserSerializer(user)
			return Response(serializer.data,status=status.HTTP_201_CREATED)

# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# class YourApiView(APIView):
#     def get(self, request, *args, **kwargs):
#         # Your view logic here
#         return Response({"message": "Authenticated API view"})
