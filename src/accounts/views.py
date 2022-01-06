from django.shortcuts import render
from .forms import *
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUpView(generic.CreateView): 
    form_class = CostumRegisterForm 
    success_url = reverse_lazy('restaurant:home') 
    template_name = 'registrations/customer_signup.html'

    
class SignUpView2(generic.CreateView): 
    form_class = ManagerRegisterForm 
    success_url = reverse_lazy('restaurant:home') 
    template_name = 'registrations/manager_signup.html'

# class Login(generic.CreateView): 
#     success_url = reverse_lazy('home') 
#     template_name = 'registrations/login.html'

# def address_create(request):
#     if request.method == 'POST':
#         city = request.POST['city']
#         street = request.POST['street']
#         plaque = request.POST['plaque']

#         device = request.COOKIES['device']
#         customer = request.user
#         address  = Address.objects.create(city = city,street = street,plaque=plaque)
#         customeraddress = CustomerAdress.objects.create(customer = customer , address = address )
#     return render(request , "address.html")

# def address_create(request):
#     if request.method == 'POST':
#         city = request.POST['city']
#         street = request.POST['street']
#         plaque = request.POST['plaque']

#         device = request.COOKIES['device']
#         customer = request.user
#         customer , create = Customer.objects.get_or_create(email = customer)
#         address  = Address.objects.create(city = city,street = street,plaque=int(plaque))
#         customeraddress = CustomerAdress.objects.create(customer = customer , address = address )
#         return redirect("cart")
#     return render(request , "address.html")