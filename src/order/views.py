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
def order_create(request ,id):
    cart = Cart(request)
    foodmenu = FoodMenu.objects.get(id=id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            customer_id = request.user.customer
            customer = Customer.objects.get(id=customer_id.id)
            if Order.objects.filter(customer = customer).filter(status="Order"):
                if (FoodMenu.objects.filter(id = id).values_list("department__name").last())[0] == FoodMenu.objects.filter(food__foodmenu2__order__status="Order").filter(food__foodmenu2__order__customer=customer).values_list("department__name").first()[0]:
                    orderid = Order.objects.filter(customer = customer_id).values_list()[0][0]
                    order = Order.objects.get(id=orderid)
                    city = request.POST['city']
                    street = request.POST['street']
                    plaque = request.POST['plaque']
                    adress = Adress.objects.create(city= city, street=street, plaque= plaque)
                    adress.save()
                    adress = Adress.objects.get(id = adress.id)
                    customeraddress = CustomerAdress.objects.create(customer = customer , address_id = adress )
                    update_order = Order.objects.filter(customer = customer).update(adress = adress)
                    update_status = Order.objects.filter(customer = customer).update(status = "order_registration")
                
                    for item in cart:
                        price = item['total_price']

                    update_order_price = Order.objects.filter(customer = customer).update(total_price= price)
                    cart.clear()
                else:
                  cart.clear()
            else:
                #id customer cart didnt save in database
                order = Order.objects.create(status="order_registration", customer = customer)
                order.save()
                orderid = Order.objects.filter(customer = customer).values_list()[0][0]
                order = Order.objects.get(id=orderid)
                for item in cart:
                    order_item = OrderItem.objects.create(order= order,foodmenu=item['foodmenu'],price=item['price'],number=item['number'])
                    order_item.save()
                    print('------------query------------')
                    print((FoodMenu.objects.filter(id = id).values_list("department__name").last())[0])
                    print(FoodMenu.objects.filter(foodmenu2__order__status="order_registration").filter(foodmenu2__order__customer=customer).values_list("department__name").first()[0])
                    
                if (FoodMenu.objects.filter(id = id).values_list("department__name").last())[0] == FoodMenu.objects.filter(foodmenu2__order__status="order_registration").filter(foodmenu2__order__customer=customer).values_list("department__name").first()[0]:
                    city = request.POST['city']
                    street = request.POST['street']
                    plaque = request.POST['plaque']
                    adress = Adress.objects.create(city= city, street=street, plaque= plaque)
                    adress.save()
                    adress = Adress.objects.get(id = adress.id)
                    customeraddress = CustomerAdress.objects.create(customer = customer , address = adress )
                    update_order = Order.objects.filter(customer = customer).update(adress = adress)
                    total_price = 0
                    for item in cart:
                        price = item['total_price']
                    update_order_price = Order.objects.filter(customer = customer).update(total_price= price)
                    cart.clear()
                    
                else:
                   cart.clear()
                   for item in cart:
                     Order.objects.filter(customer=customer).delete()
                    

    return render(request , "order/finish_order.html" ,{'foodmenu':foodmenu})
                
              

def item_create(request):
    cart = Cart(request)
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = request.user.customer.id
            user = Customer.objects.get(id=user)
            if Order.objects.filter(customer = user).exists():
                order = Order.objects.filter(customer = user).values_list()[0][0]
                order= Order.objects.get(id=order)
                for item in cart:
                        order_item = OrderItem.objects.create(order= order,foodmenu=item['foodmenu'],price=item['price'],number=item['number'])
                        order_item.save()
                        
            else:
                order = Order.objects.create(status="order", customer = user)
                order.save()
                for item in cart:
                    order_item = OrderItem.objects.create(order= order,foodmenu=item['foodmenu'],price=item['price'],number=item['number'])
                    order_item.save()
    # foodmenuid = FoodMenu.objects.filter(Food_id__foodmenuid__order = order).values_list()
    # print(foodmenuid)


    return render(request, 'order/order.html')





# def product(request, pk):
#   product = FoodMenu.objects.get(id=pk)
#   food = Food.objects.get(food__id = pk)
  
#   if request.method == 'POST':
#     #Get user account information
#     try:
#       device = request.COOKIES['device']
#       customer = request.user.email
#       our_customer = Customer.objects.get(device = device)
#       our_customer.email = customer
#       our_customer.device = device
#       our_customer.save
#       customer = our_customer
#     except:
#       device = request.COOKIES['device']
#       customer, created = Customer.objects.get_or_create(username = device,email=device+"@gmail.com",device=device )
  
#     if (Order.objects.filter(customer=customer).filter(status="Order")):
#       # print(FoodMenu.objects.filter(foodmenu__order__status="Order").filter(foodmenu__order__customer=customer).values_list("branch_id__name").last()[0],"___",FoodMenu.objects.filter(id = pk).values_list("branch_id__name").last()[0])  
#       if (FoodMenu.objects.filter(id = pk).values_list("branch_id__name").last())[0] == FoodMenu.objects.filter(foodmenu__order__status="Order").filter(foodmenu__order__customer=customer).values_list("branch_id__name").first()[0]:
#         if ((FoodMenu.objects.all().filter(id = pk).values_list('number').last())[0]>= int(request.POST['number'])):
#           flag = True
#           order, created = Order.objects.get_or_create(customer=customer, status="Order")
#           orderItem, created = OrderItem.objects.get_or_create(order=order, foodmenu=product)
#           orderItem.number =request.POST['number']
#           orderItem.save()
          
#           return redirect('cart')
#         else:
#             context = {'product':product, "food":food ,'msg':"we dont have enough"}
#             return render(request, 'product.html', context)
#       else:
#         context = {'product':product, "food":food ,'msg':"First remove all the foods from other branches"}
#         return render(request, 'product.html', context)
#     else:
#       print("hi")
#       if ((FoodMenu.objects.all().filter(id = pk).values_list('number').last())[0]>= int(request.POST['number'])):
#         order, created = Order.objects.get_or_create(customer=customer, status="Order")
#         orderItem, created = OrderItem.objects.get_or_create(order=order, foodmenu=product)
#         orderItem.number =request.POST['number']
#         orderItem.save()  
#         return redirect('cart')
#       else:
#         context = {'product':product, "food":food ,'msg':"we dont have enough"}
#         return render(request, 'product.html', context)
          

#   context = {'product':product, "food":food }
#   return render(request, 'product.html', context)