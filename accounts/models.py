from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import widgets
from django.core.validators import FileExtensionValidator

prefered_payment_choices= [
    ('PayPal', 'PayPal'),
    ('Mobile Money (MTN/Airtel)', 'Mobile Money (MTN/Airtel)'),
    ('Bank Transfer', 'Bank Transfer'),
    ]

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=120)
    name = models.CharField(max_length=120)  # max_length = required
    email = models.EmailField(max_length=120)
    prefered_payment = models.CharField(max_length = 120, choices=prefered_payment_choices , default= 'paypal')
    payment_account_details = models.CharField(max_length=120)
    # social_media_handles = models.CharField(max_length=120, blank= True)
    bio = models.TextField(blank=True)  # blank = True means it is not required
    profile_video = models.FileField(upload_to='video' ,blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['WEBM', 'MPG', 'MP2', 'MPEG', 'MPE', 'MP4', 'FLV', 'WMV','WEBM', 'MKV','FLV','VOB','GIF','AVI','MTS','M2TS','TS','M4P','M4V','SVI','3GP','3G2','MXF','NSV','FLV','F4V','F4P',])], help_text="Choose Only .WEBM, .MPG, .MP2, .MPEG, .MPE, .MP4, .FLV, 'WEBM', 'MKV','FLV','VOB','GIF','AVI','MTS','M2TS','TS','M4P','M4V','SVI','3GP','3G2','MXF','NSV','FLV','F4V','F4P', .WMV and files PLease..")
    profile_pic = models.FileField(upload_to='profile_image', max_length=255, blank=True, null=True, default='')

    def __str__(self):
        return f'{self.user.username} Profile'


class urls_social(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete = models.CASCADE, blank=True, null=True , default='1')
    social_media_handles_name = models.CharField(max_length=120, blank=True, null=True)
    social_media_handles_url = models.URLField(max_length=120, blank=True, null=True)
    def __str__(self):
        return self.social_media_handles_name


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
