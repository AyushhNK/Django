from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import UserProfile,Post,Comment
from django.contrib.auth.models import User

class UserProfileForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        bio = self.cleaned_data.get('bio')
        profile_picture = self.cleaned_data.get('profile_picture')

        UserProfile.objects.create(user=user, bio=bio, profile_picture=profile_picture)

        return user

class CreatePostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=["content"]

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=["content"]

