from django.db import models
from django.core.validators import (MinValueValidator, MaxValueValidator, MinLengthValidator)
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from account.models import *

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Department(Restaurant):
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    manager_id = models.OneToOneField('Manager',on_delete=models.CASCADE)
    category_id=models.OneToOneField("Category",on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name



class Food(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='foodimg', null=True, blank=True, default=None)
    discreption = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_add_now=True)
    category_id = models.ForeignKey("Category",on_delete=models.CASCADE)
    menu_id = models.ManyToManyField('Menu',through='Food_Menu' ,related_name='menu')

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self) -> str:
        self.category


class Menu(models.Model):
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.department_id} Menu'

class Food_Menu(models.Model):
    Food_id = models.ForeignKey(Food, on_delete= models.CASCADE)
    Menu_id = models.ForeignKey(Menu, on_delete=models.PROTECT)
    price = models.IntegerField()
    number = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.Menu_id}'


class Meal(models.Model):
    name = models.CharField(max_length=100)
    food_id = models.ManyToManyField(Food)
    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    ORDER_STATUS = (
        ('order', 'order'),
        ('order_registration', 'order_registration'),
        ('Send', 'Send'),
        ('Delivery', 'Delivery'),
        
    )
    number = models.IntegerField()
    total_price = models.IntegerField()
    delivery_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices= ORDER_STATUS, default='order_registration')
    created_date = models.DateTimeField(auto_now_add=True)
    customer_id=models.OneToOneField(Customer,on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department ,on_delete=CASCADE)

    def __str__(self) :
        return f'{self.department_id}_{self.customer_id} order'


