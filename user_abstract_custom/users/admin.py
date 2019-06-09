from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # url admin/ list_display is email last name etc...
    list_display = ['username', 'email', 'is_staff', 'last_login']


admin.site.register(CustomUser, CustomUserAdmin)
