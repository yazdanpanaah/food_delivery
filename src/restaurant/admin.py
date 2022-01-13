from django.contrib import admin
from .models import *


@admin.register(Department)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['address','city']
    list_display_links =  ['city']
    search_fields = ['city']
    list_filter = ['city']


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name','created_date', 'category']
    list_display_links =  ['name']
    search_fields = ['name']
    list_filter = ['name']



  
    
@admin.register(Category)
class FoodCategoryAdmin(admin.ModelAdmin):
    field_list=['name']
    search_fields = ['name']
  
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    field_list=['meal']
    search_fields = ['meal'] 
    list_filter = ['meal']  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    field_list=['status','total_price']
    search_fields = ['status','created_date'] 
    list_filter = ['status']
    
   

@admin.register(FoodMenu)
class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ['price','number', 'food']
    list_display_links =  ['food']
    search_fields = ['food','price']
    


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','number','foodmenu']
    list_display_links =  ['foodmenu','order']
    search_fields=['foodmenu','order']
    




















