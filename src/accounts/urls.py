from django.urls import path,include
from .views import *

urlpatterns = [ 
    path('signup/', manager, name='signup'),
    path('signup2/', customer, name='signup2'),
    # path('login/', Login.as_view(), name='login'),
    # path('signup/', customer_registration, name='signup'),




     
    ]