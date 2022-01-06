from django.urls import path
from .views import *

urlpatterns=[
    path('',cart_detail,name="carts_detail"),
    path('add/<int:foodmenu_id>/',cart_add,name="cart_add"),
    path('remove/<int:foodmenu_id>/',cart_remove,name="cart_remove"),


]