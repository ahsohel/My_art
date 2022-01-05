from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Upload


@receiver(post_save, sender=User)
def upload_image(sender, instance, created, **kwargs):
    if created:
        Upload.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def update_image(sender, instance, **kwargs):
#     instance.upload.save()
