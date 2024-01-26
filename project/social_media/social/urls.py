# social_media_app/urls.py
from django.urls import path,include
from .views import UserProfileListCreateView, PostListCreateView, CommentListCreateView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('user-profiles', UserProfileListCreateView, basename='user-profile-list-create')

urlpatterns = [
	path('', include(router.urls)),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]
