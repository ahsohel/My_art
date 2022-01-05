from django.contrib.auth.models import User
from django.db import models
# from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Create your models here.
categories = (
    ('Abstract', 'Abstract'),
    ('Animals', 'Animals'),
    ('Cityscape', 'Cityscape'),
    ('Portrait', 'Portrait'),
    ('Still Life', 'Still Life')
)


# class Design(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=120)
#     category = models.CharField(max_length=20, choices=categories)
#
#     def __str__(self):
#         return f'{self.user.username} Design'
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'img/user_{0}/{1}'.format(instance.user.username, filename)


class Upload(models.Model):
    # design = models.ForeignKey(Design, on_delete=models.CASCADE, related_name="upload", default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="upload", default="")
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="upload", default="")
    title = models.CharField(max_length=120, default="")
    image = models.ImageField(default='default.jpg',upload_to=user_directory_path)
    # up_description = models.TextField(max_length=500, blank=True)
    is_uploaded = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self) -> str:
        # return f'{self.user.username} {self.image.url}'
        return self.title
#
#

# @receiver(post_save, sender=User)
# def create_upload(sender, instance, created, **kwargs):
#     if created:
#         Upload.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_upload(sender, instance,**kwargs):
#     instance.upload.save()


class ArtworkDetails(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="artwork_details", default="")
    title = models.CharField(
        max_length=255, blank=False, null=True, default="")
    tag = models.CharField(max_length=255, blank=False, null=True, default="")
    category = models.CharField(max_length=20, blank=False, choices=categories, default=None)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(default='default.jpg', upload_to=user_directory_path)

    def __str__(self):
        return f"{self.user}={self.category}"

# @receiver(post_save, sender=User)
# def create_artwork_details(sender, instance, created, **kwargs):
#     if created:
#         ArtworkDetails.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_artwork_details(sender, instance, **kwargs):
#     instance.artwork_details.save()
