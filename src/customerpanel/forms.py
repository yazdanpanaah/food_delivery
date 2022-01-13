from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import models
from accounts.models  import *

class EditProfileForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ('username','first_name','last_name')
      