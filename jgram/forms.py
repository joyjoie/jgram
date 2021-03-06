from django import forms
from django.contrib.auth.models import User
from .models import Profile, Comments,Image,Followers




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comments
        exclude=['img','user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =['pub_date', 'likes']

class FollowersForm(forms.ModelForm):
    class Meta:
        model = Followers
        exclude=['name']
        