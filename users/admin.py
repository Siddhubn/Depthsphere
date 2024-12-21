from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register the default User model for managing users in the admin interface.
admin.site.register(CustomUser, UserAdmin)
