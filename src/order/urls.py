from django.urls import path
from .views import *

urlpatterns=[
    path('addtodb/',item_create,name="itemcreate"),
    path('finishorder/',order_create,name="finish_order"),




]