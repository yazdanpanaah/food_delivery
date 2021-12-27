from django.db import models
from django.core.validators import (MinValueValidator, MaxValueValidator, MinLengthValidator)
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Department(models,Model):
    name =models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    resturant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    manager_id = models.OneToOneField('Manager',on_delete=models.CASCADE)
    order_id = models.ForeignKey("Order",on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class DepartmentCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Food(models.Model):
    name=models.CharField(max_length=30)
    photo = models.ImageField(upload_to='foodimg', null=True, blank=True, default=None)
    discreption=models.TextField(max_length=200)
    created_date=models.DateTimeField(auto_add_now=True)
    category_id=models.ForeignKey("Category",on_delete=models.CASCADE)
    # cart_id=models.ManyToManyField("Cart")
    menu_id=models.ManyToManyField('Menu',through='Food_Menu')

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

class Food_Menu(models.Model):
    Food_id = models.ForeignKey(Food, on_delete= models.CASCADE)
    Menu_id = models.ForeignKey(Menu, on_delete=models.PROTECT)
    price = models.IntegerField()
    number = models.IntegerField()

class Meal(models.Model):
    name = models.CharField(max_length=100)
    food_id = models.ManyToManyField(Food)

    def __str__(self) -> str:
        return self.name



