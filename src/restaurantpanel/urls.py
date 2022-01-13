from django.urls import path,include
from .views import *

urlpatterns = [
    path('', MangerProfile.as_view(), name='mangerprofile'),
    path('department/<int:pk>/', DepartmentView.as_view(), name='department_view'),
    path("updatebranch/<int:pk>/",UpdateDepartment.as_view(),name="update_branch"), 
    path("foodmenu/<int:pk>/",FoodMenuView.as_view(),name="foodmenu_view"),
    path("createfood/<int:pk>/",create_foodmenu,name="create_food"), 
    path("updatefood/<int:pk>/",UpdateFoodMenu.as_view(),name="update_food"), 
    path("deletefoodmenu/<int:pk>/",deletefoodmenu,name = "delete_foodmenu"),
    path("orderstatus/",order_status,name = "order_status"),
    path("updatestatus/<int:pk>/",UpdateStatus.as_view(),name="update_status"), 




 


    
]