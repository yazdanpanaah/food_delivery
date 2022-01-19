from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name= 'home'),
    path('detail/<int:id>/', food_detail, name='food_detail'),
    path("search/" , search_result, name="search2"),
    path("menu/<int:id>/" ,all_item, name="menu"),
    path("branch_menu/" ,branch_menu, name="branch_menu"),
    path("show_menu/<int:id>/" ,show_menu, name="show_menu"),


    # path("<int:pk>/" , get_info_search , name="get_search"),

    
]
