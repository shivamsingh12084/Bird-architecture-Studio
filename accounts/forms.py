from webbrowser import get
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import models


class CustomUserCreationForm(UserCreationForm):
    """ We are overiding the User creation form by the CustomUserCreation form"""
    class Meta:
        model = get_user_model()
        fields = ('email' , 'username')

        
class CustomUserChangeForm(UserChangeForm):
    """ Here we are overiding the default UserChangeForm """
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')