from rest_framework import serializers
from .models import Author,Book
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
	token= serializers.SerializerMethodField()
	class Meta:
		model=User
		fields=['username','email','password','token']

	def get_token(self,obj):
		token,created=Token.objects.get_or_create(user=obj)
		return token.key

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model=Author
		fields=['id','first_name','last_name','bio']

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model=Book
		fields=['id','title','author','publication_date']