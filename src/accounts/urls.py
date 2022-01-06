from django.urls import path,include
from .views import *

urlpatterns = [ 
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup2/', SignUpView2.as_view(), name='signup2'),
    # path('login/', Login.as_view(), name='login'),


     
    ]