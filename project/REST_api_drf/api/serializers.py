from rest_framework import serializers
from .models import Author,Book

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model=Author
		fields=['first_name','last_name','bio']

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model=Book
		fields=['title','author','publication_date']