from django.contrib import admin
from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomeUser
    list_display = ['email', 'username', 'is_staff', ]
    list_display_links = ['email']


admin.site.register(CustomeUser,CustomUserAdmin)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name', 'email']
    list_display_links = ['email']
    search_fields = ['email']

    def get_queryset(self, request):
        return Customer.objects.filter(is_staff=False)



@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    list_display = ['city', 'street', 'plaque']
    list_display_links = ['city']
    search_fields = ['city']

@admin.register(Manager)
class managerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_display_links = ['email']
    search_fields = ['email']



    def get_queryset(self, request):
        return Manager.objects.filter(is_staff=True, is_superuser=False)



@admin.register(Admin)
class AdminProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['username']
    list_editable = ['email']
    search_fields = ['username', 'email']

    def get_queryset(self, request):
            return Admin.objects.filter(is_superuser=True)


@admin.register(CustomerAdress)
class CustomerAdressAdmin(admin.ModelAdmin):
    list_display = ['customer','address','main_adress']
    list_display_links = ['customer']
    empty_value_display = "---"