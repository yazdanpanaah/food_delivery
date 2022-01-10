from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from django.views.decorators.http import require_POST
from django.contrib.auth.hashers import make_password
# Create your views here.
# class SignUpView(generic.CreateView): 
#     form_class = CostumRegisterForm 
#     success_url = reverse_lazy('restaurant:home') 
#     template_name = 'registrations/customer_signup.html'
   

    
# class SignUpView2(generic.CreateView): 
#     form_class = ManagerRegisterForm 
#     success_url = reverse_lazy('restaurant:home') 
#     template_name = 'registrations/manager_signup.html'
    


#--------------registration-----------------------


# def customer_registration(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email= request.POST['email']
#         password = make_password(request.POST['password'])
#         city = request.POST['city']
#         street = request.POST['street']
#         plaque = request.POST['plaque']
#         print('-------------fuc------------------')


#         customer = Customer.objects.create(username = username , email=email, password =password)
#         customer.save()
#         user= Customer.objects.get(id = customer.id)

#         adress = Adress.objects.create(city= city, street=street, plaque= plaque)
#         adress.save()
#         adress_id = Adress.objects.get(id = adress.id)
        
#         customeraddress = CustomerAdress.objects.create(customer= user , address= adress_id , main_adress=True)
#     return render(request, 'registrations/customeradress.html')

def manager(req):
    if req.method == 'POST':
        form = ManagerRegisterForm(req.POST)
        if form.is_valid() and req.POST["password"]  == req.POST["password2"]:
            form = form.save()
            return redirect("restaurant:home")
        return render(req , "registrations/manager_signup.html" , {"form":form})
    else:
        form = ManagerRegisterForm()
        context ={'form':form}
    return render(req, 'registrations/manager_signup.html',context)

def customer(req):
    if req.method == 'POST':
        form = CustomerRegisterForm(req.POST)
        if form.is_valid() and req.POST["password"]  == req.POST["password2"]:
            form = form.save()
            return redirect("restaurant:home")
        return render(req , "registrations/customer_signup.html" , {"form":form})
    else:
        form = CustomerRegisterForm()
        context ={'form':form}
    return render(req, 'registrations/customer_signup.html',context)