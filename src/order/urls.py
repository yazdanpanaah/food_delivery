from django.urls import path
from .views import *

urlpatterns=[
    # path('addtodb/',item_create,name="itemcreate"),
    path('finish_order/',order_create,name="finish_order"),




]