from django import forms 
from django.contrib.auth.forms import UserChangeForm,UserCreationForm 
from django.forms import fields 
from django.core.validators import MinValueValidator
from restaurant.models import *
from django.contrib.auth.hashers import make_password





class CreateFoodMenuForm(forms.ModelForm):
    class Meta:
        model = FoodMenu
        exclude = ('department',)
       

    

        
        