#from _typeshed import Self
from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework import generics, permissions, response, status
from rest_framework import permissions
# Create your views here.




class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(id=self.request.user)
    def get_queryset(self):
        queryset = Customer.objects.filter(id = self.request.user.id)
        return queryset
        
    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            obj = self.get_object()
            self.perform_destroy(obj)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return response.Response(status=status.HTTP_400_BAD_REQUEST, data="You are not allowed to delete!")


class AddressView(viewsets.ModelViewSet):
    serializer_class=AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset=Adress.objects.all()
    def get_queryset(self):
        owner=self.request.user
        queryset=Adress.objects.filter(owner=owner)
        return queryset
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class OrderView(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset=Order.objects.all()
    def get_queryset(self):
        owner=self.request.user
        queryset=Order.objects.filter(customer=owner.id)
        return queryset
    def perform_create(self,serializer):
        serializer.save(customer=self.request.user)