from django import forms
from django.contrib.auth.models import User
from .models import Profile, Comments




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comments
        exclude=['img','user']

        