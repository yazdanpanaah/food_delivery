from email import message
from django.contrib.auth import login
from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from django.contrib.auth.decorators import login_required

from accounts.models import Customer
from .forms import *
from restaurant.models import FoodMenu, OrderItem , Order
from Cart.cart import Cart
# from .tasks import order_created
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
# from zarinpal.tasks import payment_completed
from accounts.models import *
# Create your views here.
@login_required
def order_create(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            customer_id = request.user.customer
            customer = Customer.objects.get(id=customer_id.id)
            address = Adress.objects.get(id=request.POST.get('address_id'))
            order = Order.objects.create(status="order_registration", customer = customer ,adress =address)
            order.save()
            price = 0
            for item in cart:
                order_item = OrderItem.objects.create(order= order,foodmenu=item['foodmenu'],price=item['price'],number=item['number'])
                order_item.save()
                price += item['price'] * item['number']
                
            
            
            
            print(price)
            Order.objects.filter(customer = customer).update(total_price= price)
            cart.clear()

    messages.success(request ,"your order saved successfuly!")           
    return redirect("restaurant:home")
    # return render(request , "order/finish_order.html" ,{'foodmenu':foodmenu})
                
              

# def item_create(request):
#     cart = Cart(request)
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             user = request.user.customer.id
#             user = Customer.objects.get(id=user)
#             if Order.objects.filter(customer = user).exists():
#                 order = Order.objects.filter(customer = user).values_list()[0][0]
#                 order= Order.objects.get(id=order)
#                 for item in cart:
#                         order_item = OrderItem.objects.create(order= order,foodmenu=item['foodmenu'],price=item['price'],number=item['number'])
#                         order_item.save()
                        
#             else:
#                 order = Order.objects.create(status="order", customer = user)
#                 order.save()
#                 for item in cart:
#                     order_item = OrderItem.objects.create(order= order,foodmenu=item['foodmenu'],price=item['price'],number=item['number'])
#                     order_item.save()
   

#     return render(request, 'order/order.html')





# else:
    #     #id customer cart didnt save in database
    #     order = Order.objects.create(status="order_registration", customer = customer)
    #     order.save()
    #     orderid = Order.objects.filter(customer = customer).values_list()[0][0]
    #     order = Order.objects.get(id=orderid)
    #     for item in cart:
    #         order_item = OrderItem.objects.create(order= order,foodmenu=item['foodmenu'],price=item['price'],number=item['number'])
    #         order_item.save()
    #         print('------------query------------')
    #         print((FoodMenu.objects.filter(id = id).values_list("department__name").last())[0])
    #         print(FoodMenu.objects.filter(foodmenu2__order__status="order_registration").filter(foodmenu2__order__customer=customer).values_list("department__name").first()[0])
            
    #     if (FoodMenu.objects.filter(id = id).values_list("department__name").last())[0] == FoodMenu.objects.filter(foodmenu2__order__status="order_registration").filter(foodmenu2__order__customer=customer).values_list("department__name").first()[0]:
    #         city = request.POST['city']
    #         street = request.POST['street']
    #         plaque = request.POST['plaque']
    #         adress = Adress.objects.create(city= city, street=street, plaque= plaque)
    #         adress.save()
    #         adress = Adress.objects.get(id = adress.id)
    #         customeraddress = CustomerAdress.objects.create(customer = customer , address = adress )
    #         update_order = Order.objects.filter(customer = customer).update(adress = adress)
    #         total_price = 0
    #         for item in cart:
    #             price = item['total_price']
    #         update_order_price = Order.objects.filter(customer = customer).update(total_price= price)
    #         cart.clear()
            
    #     else:
    #        cart.clear()
    #        for item in cart:
    #          Order.objects.filter(customer=customer).delete()