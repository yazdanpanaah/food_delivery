from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import SET_NULL

# Create your models here.
class CustomeUser(AbstractUser):
    email=models.EmailField(unique=True)
    

class Admin(CustomeUser):
    class Meta:
        proxy =True
        verbose_name="superuser"
        verbose_name_plural = 'superusers'

    def save(self,*args, **kwargs):
        if not self.id:
            self.is_superuser = True
        return super(Admin,self).save(*args,**kwargs) 
       

class Manager(CustomeUser):
    class Meta:
        verbose_name = 'restaurant-manager'
        verbose_name_plural = 'resurants_managers' 


    def save(self,*args, **kwargs):
        if not self.id:
            self.is_staff = True
            self.is_superuser = False
        return super(Manager,self).save(*args,**kwargs)

    

class Customer(CustomeUser):
    adress_id = models.ManyToManyField('Adress', through='CustomerAdress', related_name='customeradress')

    class Meta:
        verbose_name="customer"
        verbose_name_plural = 'customers' 
    def save(self,*args, **kwargs):
        if not self.id:
            self.is_staff = False
            self.is_superuser = False
        return super(Customer,self).save(*args,**kwargs)

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(Customer, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
    #     return user

class CustomerAdress(models.Model):
    main_adress = models.BooleanField(default=False)
    customer_id = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True, related_name='customer')
    address_id = models.ForeignKey('Adress', on_delete=models.SET_NULL , null=True,related_name='adress_related')



class Adress(models.Model):
    city = models.CharField(max_length=10)
    street = models.CharField(max_length=10)
    plaque = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.city}-{self.street}-{self.plaque}'