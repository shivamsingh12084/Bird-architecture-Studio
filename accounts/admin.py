from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

#Local imports 
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Register your models here.
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    """Here we are overidding the default useradmin to use our custom created forms"""
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['email', 'username']

admin.site.register(CustomUser, CustomUserAdmin)