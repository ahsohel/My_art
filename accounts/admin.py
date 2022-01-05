from django.contrib import admin
# from .models import Account, Login
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile, urls_social

# Register your models here.

admin.site.register(Profile)
admin.site.register(urls_social)
