from django import forms 
from django.contrib.auth.forms import UserChangeForm,UserCreationForm 
from django.forms import fields 
from .models import Customer, CustomeUser, Manager 
from django.core.validators import MinValueValidator


class CostumRegisterForm(UserCreationForm): 
    email = forms.EmailField(required=True) 
    class Meta: 
        model = Customer 
        fields = ("username", "email", "password1", "password2") 
        widgets = {  
             'password': forms.PasswordInput(),  
                }  
 
    def save(self, commit=True): 
        user = super().save(commit=False) 
        user.email = self.cleaned_data['email'] 
         
        if commit: 
            user.save() 
        return user 
 
class ManagerRegisterForm(UserCreationForm): 
    email = forms.EmailField(required=True) 
    class Meta: 
        model = Manager 
        fields = ("username", "email", "password1", "password2") 
        widgets = {  
             'password': forms.PasswordInput(),  
                }  
 
    def save(self, commit=True): 
        user = super().save(commit=False) 
        user.email = self.cleaned_data['email'] 
         
        if commit: 
            user.save() 
        return user

class AddressForm(forms.Form):
    state = forms.CharField(label="state",max_length=40,required=True)
    city = forms.CharField(label="city",max_length=30,required=True)
    street = forms.CharField(label="city",max_length=30,required=True)
    pluque = forms.IntegerField(validators=[MinValueValidator(1)],required=True)