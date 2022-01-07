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
            user = Customer.objects.filter(username = request.user).values_list()[0][0]
            customer = Customer.objects.get(id=user)
            if Order.objects.filter(customer_id = customer).exists():
               
                orderid = Order.objects.filter(customer_id = customer).values_list()[0][0]
                order_id = Order.objects.get(id=orderid)
                city = request.POST['city']
                street = request.POST['street']
                plaque = request.POST['plaque']
                adress = Adress.objects.create(city= city, street=street, plaque= plaque)
                adress.save()
                adress_id = Adress.objects.get(id = adress.id)
                customeraddress = CustomerAdress.objects.create(customer_id = customer , address_id = adress_id )
                update_order = Order.objects.filter(customer_id = customer).update(adress_id = adress_id)
               
                for item in cart:
                    price = item['total_price']

                update_order_price = Order.objects.filter(customer_id = customer).update(total_price= price)
                cart.clear()
                
            else:
                #id customer cart didnt save in database
                order = Order.objects.create(status="order_registration", customer_id = customer)
                order.save()
                orderid = Order.objects.filter(customer_id = customer).values_list()[0][0]
                order_id = Order.objects.get(id=orderid)
                for item in cart:
                    order_item = OrderItem.objects.create(order_id= order,food_menu_id=item['foodmenu'],price=item['price'],number=item['number'])
                    order_item.save()
                # orderitem_id = Adress.objects.get(id = order_item.id) 
                
                city = request.POST['city']
                street = request.POST['street']
                plaque = request.POST['plaque']
                adress = Adress.objects.create(city= city, street=street, plaque= plaque)
                adress.save()
                adress_id = Adress.objects.get(id = adress.id)
                customeraddress = CustomerAdress.objects.create(customer_id = customer , address_id = adress_id )
                update_order = Order.objects.filter(customer_id = customer).update(adress_id = adress_id)
                total_price = 0
                for item in cart:
                    price = item['total_price']
                update_order_price = Order.objects.filter(customer_id = customer).update(total_price= price)
                cart.clear()

    return render(request , "order/finish_order.html")
                
              

def item_create(request):
    cart = Cart(request)
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = Customer.objects.filter(username = request.user).values_list()[0][0]
            customer = Customer.objects.get(id=user)
            
            if Order.objects.filter(customer_id = customer).exists():
                orderid = Order.objects.filter(customer_id = customer).values_list()[0][0]
                order_id = Order.objects.get(id=orderid)
                for item in cart:
                        order_item = OrderItem.objects.create(order_id= order_id,food_menu_id=item['foodmenu'],price=item['price'],number=item['number'])
                        order_item.save()
                        
            else:
                order = Order.objects.create(status="order", customer_id = customer)
                order.save()
                for item in cart:
                    order_item = OrderItem.objects.create(order_id= order,food_menu_id=item['foodmenu'],price=item['price'],number=item['number'])
                    order_item.save()
    # foodmenuid = FoodMenu.objects.filter(Food_id__foodmenuid__order_id = order_id).values_list()
    # print(foodmenuid)


    return render(request, 'order/order.html')





