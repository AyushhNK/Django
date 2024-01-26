from rest_framework import viewsets,generics
from rest_framework.views import APIView
from .models import UserProfile, Post, Comment
from .serializers import UserProfileSerializer, PostSerializer, CommentSerializer

class UserProfileListCreateView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateView(APIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
