from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Upload, ArtworkDetails


class ArtUploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['title' ,'image']


class ArtworkDetail(forms.ModelForm):
    class Meta:
        model = ArtworkDetails
        fields = ['category', 'description']
