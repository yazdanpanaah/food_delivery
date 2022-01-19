from django.urls import path,include
from .views import *

urlpatterns = [ 
    path('signup/', manager, name='signup'),
    path('signup2/', customer, name='signup2'),
    path('login/', custome_login, name='login'),
    # path('signup/', customer_registration, name='signup'),
    #  path('login', Login.as_view(), name='login2'),
    path('signup2/', customer, name='signup2'),
    path('customer/ajax_address',ajax_address,name='ajax_address'),
    path("logout/", custome_logout, name= "logout"),





     
    ]