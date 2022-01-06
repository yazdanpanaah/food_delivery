from django.contrib import admin
from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomeUser
    list_display = ['email', 'username', 'is_staff', ]

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
    search_fields = ['city']

@admin.register(Manager)
class managerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['email']


    # def save(self,*args, **kwargs):
    #     if not self.id:
    #         self.is_staff = True
    #         self.is_superuser = False
    #     return super(Manager,self).save(*args,**kwargs)

    def get_queryset(self, request):
        return Manager.objects.filter(is_staff=True, is_superuser=False)



@admin.register(Admin)
class AdminProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['username']
    list_editable = ['email']
    search_fields = ['username', 'email']

    #   def save(self,*args, **kwargs):
    #     if not self.id:
    #         self.is_superuser = True
    #     return super(Admin,self).save(*args,**kwargs)
    def get_queryset(self, request):
            return Admin.objects.filter(is_superuser=True)

# Register your models here.
# @admin.register(Address)
# class AdressAdmin(admin.ModelAdmin):
#     list_display = ['city', 'street', 'plaque']
#     search_fields = ['city']
#     empty_value_display = "---"

@admin.register(CustomerAdress)
class CustomerAdressAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'main_adress']
    empty_value_display = "---"