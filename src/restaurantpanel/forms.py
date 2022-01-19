from django import forms 
from restaurant.models import *






class CreateFoodMenuForm(forms.ModelForm):
    class Meta:
        model = FoodMenu
        exclude = ('department',)
       

    

        
        