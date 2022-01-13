from django.urls import path,include
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'customer', CustomerView,basename='customer')
router.register(r'address', AddressView,basename='adress')
router.register(r'order', OrderView,basename='order')



urlpatterns = [
    path('api/',include(router.urls)),
    path('', CustomerProfile.as_view(), name='profile'),
    path('update/', update_profile, name='update_profile'),
    path("address/",address,name="adress"), 
    path("history/",history,name="history"), 
 


    
]