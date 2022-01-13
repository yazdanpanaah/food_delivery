from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name= 'home'),
    path('detail/<int:id>', food_detail, name='food_detail'),
    path("search/" , search , name="search"),
    
]
