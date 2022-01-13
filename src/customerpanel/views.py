#from _typeshed import Self
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework import generics, permissions, response, status
from rest_framework import permissions
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import *
# Create your views here.



@customer_required()
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

@customer_required()
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


@customer_required()
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


@customer_required()
class CustomerProfile(TemplateView):
    template_name = 'customerpanel/profile.html'

# def profile(req):
#     info = Customer.objects.filter(id = req.user.id)
#     return render(req, 'customerpanel/profile.html', {'info':info})
   
        

def update_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        context = {'form':form}
        return render(request, 'customerpanel/update_profile.html', context)


def address(request): 
    return render(request, 'customerpanel/address.html') 
   
def history(request): 
    return render(request, 'customerpanel/history.html') 
 
