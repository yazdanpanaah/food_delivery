from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomeUser(AbstractUser):
    email=models.EmailField(unique=True)
    

class Admin(CustomeUser):
    class Meta:
        proxy = True
        verbose_name="superuser"

class Staff(CustomeUser):
    class Meta:
        proxy = True
        verbose_name = 'restaurant'
        verbose_name_plural = 'resurants' 

class Manager(CustomeUser):
    class Meta:
        verbose_name="resturant_manager"

class Customer(CustomeUser):
    address_id = models.ManyToManyField("Adress",related_name='address')

class Adress(models.Model):
    city = models.CharField(max_length=10)
    street = models.CharField(max_length=10)
    plaque = models.ImageField()