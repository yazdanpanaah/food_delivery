from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('addfood/', AddFood.as_view() , name = "addfood"),
    path('updatefood/<int:pk>', UpdateFood.as_view() , name = "updatefood"),
    path('deletefood/<int:pk>', DeleteFood.as_view() , name = "deletefood"),
    path('addcategory/', AddCategory.as_view() , name = "addcategory"),
    path('', adminpanel, name = 'admin'),

]