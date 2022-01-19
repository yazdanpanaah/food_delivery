from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from django.views.decorators.http import require_POST
from django.contrib.auth.hashers import make_password
from django.views import View
from django.http.response import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate ,logout
from django.contrib import messages


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




def ajax_address(request):
    if request.is_ajax() and request.method == "POST":
        form = AddAddressForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = Customer.objects.get(pk=request.user.id)
            obj.save()
            
            customer = request.user
            address_list=Adress.objects.filter(owner=customer)
            t= render_to_string('cart/choose_adress.html',{'address_list': address_list})
            return JsonResponse({'data': t})
        else:          
            return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": ""}, status=400)

 #------------------------------login------------------------------------------   

def custome_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password )
            if user is not None:
                login(request, user)
                
                return redirect("restaurant:home")
        #     else:
        #         messages.error(request,"Invalid username or password.")
        # else:
        #     messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registrations/login.html", context={"login_form":form}) 

def custome_logout(request):
    logout(request)
    return redirect("restaurant:home")


    # class Login(View):
#     return_url = None
#     def get(self, request):
#         Login.return_url = request.GET.get ('return_url')
#         return render (request, 'registrations/login.html')

#     def post(self, request):
#         email = request.POST.get ('email')
#         password = request.POST.get ('password')
#         customer = Customer.get_customer_by_email(email)
#         error_message = None
#         if customer:
#             print('-----cus-----')
#             flag = check_password (password, customer.password)
#             if flag:
#                 request.session['customer'] = customer.id
#                 print('-----cus2-----')

#                 if Login.return_url:
#                     print('-----cus3-----')
#                     return HttpResponseRedirect (Login.return_url)
                    
#                 else:
#                     Login.return_url = None
#                     return redirect ('restaurant:home')
#             else:
#                 error_message = 'Invalid !!'
#         else:
#             error_message = 'Invalid !!'

#         print (email, password)
#         return render (request, 'registrations/login.html', {'error': error_message})


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