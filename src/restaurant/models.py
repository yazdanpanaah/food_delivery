from django.db import models
from django.core.validators import (MinValueValidator, MaxValueValidator, MinLengthValidator)
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.db.models.fields import CharField
from accounts.models import *
import jdatetime

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
    manager = models.OneToOneField(Manager,on_delete=models.PROTECT ,related_name='maneger')
    category=models.ForeignKey("Category",on_delete=models.PROTECT ,related_name='category1')
    food = models.ManyToManyField('Food',through='FoodMenu' ,related_name='foodmenu1')
    def __str__(self) -> str:
        return self.name

    @property
    def created_date_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.created_date)

class Food(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='foodimg', null=True, blank=True, default=None)
    discreption = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add =True)
    category = models.ForeignKey("Category",on_delete=models.PROTECT, related_name='category2')#food can not be without category
    meal = models.ManyToManyField("Meal",related_name="meal1")

    def __str__(self) -> str:
        return self.name

    @property
    def created_date_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.created_date)

class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self) -> str:
        return  self.category


# class Menu(models.Model):
#     department_id = models.ForeignKey(Department, on_delete=models.CASCADE ,related_name='menu')
#     # food_menu_id = models.ForeignKey('Food_Menu', on_delete=models.CASCADE ,related_name='menu', null=True)
#     def __str__(self) -> str:
#         return f'{self.department_id} Menu'

class FoodMenu(models.Model):
    food = models.ForeignKey(Food, on_delete= models.PROTECT,related_name='food2')
    department = models.ForeignKey(Department, on_delete=models.CASCADE ,related_name='Department')
    price = models.IntegerField()
    number = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.department_id}-{self.Food_id}'


class Meal(models.Model):
    MEAL_CHOICES=(
        ('breakfast','breakfast'),
        ("lunch",'lunch'),
        ("dinner","dinner")

    )
    meal = models.CharField(choices=MEAL_CHOICES, max_length=100 ,default='dinner')
    def __str__(self) -> str:
        return self.meal

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=CASCADE ,related_name='order')
    foodmenu = models.ForeignKey(FoodMenu, on_delete=SET_NULL,null=True, related_name='foodmenu2')
    number = models.IntegerField()
    price = models.IntegerField()
    def __str__(self) -> str:
        return f'orderitem:{self.food_menu_id}'

    
    def get_cost(self):
        return self.price * self.number
        

class Order(models.Model):
    ORDER_STATUS = (
        ('order', 'order'),
        ('order_registration', 'order_registration'),
        ('Send', 'Send'),
        ('Delivery', 'Delivery'),
        
    )
    total_price = models.IntegerField(null=True, blank=True)
    adress = models.ForeignKey(Adress,on_delete=CASCADE,related_name='adress2',null=True, blank=True) 
    delivery_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices= ORDER_STATUS, default='order_registration')
    created_date = models.DateTimeField(auto_now_add=True)
    customer=models.OneToOneField(Customer,on_delete=models.SET_NULL, related_name='customer1',null=True)
    # department_id = models.ForeignKey(Department ,on_delete=CASCADE, related_name='department')
    order_item = models.ManyToManyField(FoodMenu, through='OrderItem' ,related_name='orederitem1')
    def __str__(self) :
        return f'{self.customer_id} order'

    @property
    def created_date_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.created_date)
