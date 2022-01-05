from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Textarea
from .models import Profile
from django.utils.translation import gettext_lazy as _

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control",'style':"width:200px;text-align:center;margin-left:520px"}))  # default argument is required=True
    username=forms.CharField(widget= forms.TextInput(attrs={'class': "form-control",'style':"width:200px;text-align:center;margin-left:520px"}))
    password1=forms.CharField(widget= forms.PasswordInput(attrs={'class': "form-control",'style':"width:200px;text-align:center;margin-left:520px"}))
    password2=forms.CharField(widget= forms.PasswordInput(attrs={'class': "form-control",'style':"width:200px;text-align:center;margin-left:520px"}))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px; max-height: 100px;',
                }),
            'password1': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px; max-height: 100px;',
                }),
            'password2': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px; max-height: 100px;',
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'width: 300px; max-height: 100px;',
                })
        }
        # help_texts = {
        #     'username': None,
        # }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # for fieldname in ['username', 'password1', 'password2']:
        #     self.fields[fieldname].help_text = None

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 250px; max-height: 100px;'}))
    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 250px; max-height: 100px;',
                }),
            'email': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 250px; max-height: 100px;',
                })
        }

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None

class ProfileUpdateName(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name"]
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px; max-height: 100px;',
                })}

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        # fields = ["name", "prefered_payment", "payment_account_details","social_media_handles","bio"]
        fields = ["name", "prefered_payment", "payment_account_details", "bio"]
        widgets = {

            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px; max-height: 100px;',
                'placeholder': 'Enter your name',
                'size': '40',

                }),

            'prefered_payment': TextInput(attrs={

                # 'style': 'max-width: 1100px; max-height: 100px;',
                'style': 'width: 300px; max-height: 100px;',

                }),

            'payment_account_details': TextInput(attrs={
                'class': "form-control", 
                # 'style': 'max-width: 1100px; max-height: 100px;',
                'style': 'width: 300px; max-height: 100px;',
                'placeholder': 'Enter your paypal ID/ MM number'
                }),
            # 'social_media_handles': TextInput(attrs={
            #     'class': "form-control",
            #     # 'style': 'max-width: 1100px; max-height: 100px;',
            #     'style': 'width: 300px; max-height: 100px;',
            #     'placeholder': '(Instagram, dribble,Behance, personal website)'
            #     }),
            'bio': Textarea(attrs={
                'class': "form-control", 
                # 'style': 'max-width: 1100px; max-height: 200px;',
                'style': 'width: 300px; max-height: 100px;',
                'placeholder': 'Insert three or more sentences to describe yourself!'
                })
        }
        labels = {
            'name': _('Display Name'),
            'social_media_handles': _('Social Media Handles*'),
        }
        # help_texts = {
        #     'social_media_handles': _('(Instagram, dribble, Behance, personal website)'),
        # }


    # def __init__(self, *args, **kwargs):
    #     super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        # for fieldname in ['name', 'paypal_id', 'bio']:
        #    self.fields[fieldname].help_text = None