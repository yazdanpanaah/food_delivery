from django import forms 
from django.contrib.auth.forms import UserChangeForm,UserCreationForm 
from django.forms import fields 
from .models import Customer, CustomeUser, Manager 
from django.core.validators import MinValueValidator
from restaurant.models import *
from django.contrib.auth.hashers import make_password




class ManagerRegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput())
    password2 = forms.CharField(required=True,widget=forms.PasswordInput())
    
    class Meta:
        model = Department
        fields = ("email","username","name", "address", "city", "description","category","password","password2",)
        
        widgets = { 
             'password': forms.PasswordInput(), 
             'password2': forms.PasswordInput(),
              
                } 
    def save(self, commit=True):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        password = make_password(self.cleaned_data['password'])
        manager = Manager.objects.create(username = username, password = password,email  = email)
        manager.save()
        name = self.cleaned_data["name"]
        category = self.cleaned_data['category']
        address = self.cleaned_data['address']
        city = self.cleaned_data['city']
        description = self.cleaned_data['description']
        department = Department.objects.create(name = name,manager = manager , category =category ,address = address,city = city ,description = description)
        department.save()


class CustomerRegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput())
    password2 = forms.CharField(required=True,widget=forms.PasswordInput())
    
    class Meta:
        model = Adress
        fields = ( "email","username", "city","street","plaque","password", "password2",)
        widgets = { 
             'password': forms.PasswordInput(), 
             'password2': forms.PasswordInput(),
              
                } 

    def save(self, commit=True):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        password = make_password(self.cleaned_data['password'])
        customer= Customer.objects.create(username = username, password = password,email= email)
        customer.save()
        city = self.cleaned_data['city']
        street = self.cleaned_data['street']
        plaque = self.cleaned_data['plaque']

        adress = Adress.objects.create(city= city, street=street, plaque=plaque)
        adress.save()
        customeradress = CustomerAdress.objects.create(customer= customer , address = adress , main_adress =True)
        customeradress.save()

class AddAddressForm(forms.ModelForm):
    
    class Meta:
        model = Adress
        fields = ('city','street','plaque')

# class CostumRegisterForm(UserCreationForm): 
#     email = forms.EmailField(required=True) 
#     class Meta: 
#         model = Customer 
#         fields = ("username", "email", "password1", "password2") 
#         widgets = {  
#              'password': forms.PasswordInput(),  
#                 }  
 
#     def save(self, commit=True): 
#         user = super().save(commit=False) 
#         user.email = self.cleaned_data['email'] 
         
#         if commit: 
#             user.save() 
#         return user 
 
# class ManagerRegisterForm(UserCreationForm): 
#     email = forms.EmailField(required=True) 
#     class Meta: 
#         model = Manager 
#         fields = ("username", "email", "password1", "password2") 
#         widgets = {  
#              'password': forms.PasswordInput(),  
#                 }  
 
#     def save(self, commit=True): 
#         user = super().save(commit=False) 
#         user.email = self.cleaned_data['email'] 
         
#         if commit: 
#             user.save() 
#         return user

# class AddressForm(forms.Form):
#     state = forms.CharField(label="state",max_length=40,required=True)
#     city = forms.CharField(label="city",max_length=30,required=True)
#     street = forms.CharField(label="city",max_length=30,required=True)
#     pluque = forms.IntegerField(validators=[MinValueValidator(1)],required=True)