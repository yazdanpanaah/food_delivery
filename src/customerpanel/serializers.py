from django.contrib.auth.models import User 
from rest_framework import serializers
from accounts.models import *
from restaurant.models import Order
 
        
class CustomerSerializer(serializers.ModelSerializer):
    read_only_fields = ["email"]
    class Meta:
        model = Customer
        fields=['id','username','last_name','first_name']
        
class AddressSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Adress
        fields=['id','city','street','plaque','owner']

class CustomerOrdeSerializer(serializers.ModelSerializer):
    customer=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Order
        fields='__all__'