# from django.core.checks import messages
from django.shortcuts import render , get_object_or_404 , redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from restaurant.models import *
from .forms import CartAddProductForm
from django.contrib import messages


# Create your views here.


# @require_POST
# def cart_add(request,foodmenu_id):
#     cart = Cart(request)
#     foodmenu = get_object_or_404(FoodMenu,id=foodmenu_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(foodmenu = foodmenu ,number=cd['number'],override_number=cd['override'])
#         return redirect('cart:carts_detail') 

@require_POST
def cart_add(request,foodmenu_id):
    cart = Cart(request)
    foodmenu = get_object_or_404(FoodMenu,id=foodmenu_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if int(request.POST['number']) <= ((FoodMenu.objects.all().filter(id = foodmenu_id).values_list('number').last())[0]):
            
            cart.add(foodmenu = foodmenu ,number=cd['number'],override_number=cd['override'])
        
            
            return redirect('cart:carts_detail') 
        else:
            
            messages.error(request, 'this food is not availbale in this amount!')
            return redirect('cart:carts_detail')
        
            
        
     

    # if request.method == 'POST':
    #     if request.user.is_authenticated:
    #             user = Customer.objects.filter(username = request.user).values_list()[0][0]
    #             customer = Customer.objects.get(id=user)
    #             # print(customer)
    #             order = Order.objects.create(status="order", customer_id = customer)
    #             order.save()
    #             for item in cart:
    #                     order_item = OrderItem.objects.create(order_id= order,food_menu_id=item['foodmenu'],price=item['price'],number=item['number'])
    #                     order_item.save()
        

@require_POST
def cart_remove(request,foodmenu_id):
    cart = Cart(request)
    foodmenu = get_object_or_404(FoodMenu,id=foodmenu_id)
    cart.remove(foodmenu)
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = Customer.objects.filter(username = request.user).values_list()[0][0]
            customer = Customer.objects.get(id=user)
            # print(user)
            order = Order.objects.filter(customer_id = customer).delete()
            # order.save()
            for item in cart:
                    order_item = OrderItem.objects.create(order_id= order,food_menu_id=item['foodmenu'],price=item['price'],number=item['number'])
                    order_item.save()
    return redirect('cart:carts_detail')


def cart_detail(request):
    cart = Cart(request)
    cart_items = [item['foodmenu'] for item in cart]
    for item in cart:
        item['update_number_form'] = CartAddProductForm(initial={
            'number':item["number"],
            "override":True,
        })
    return render(request,'cart/detail.html',{'cart':cart })
    

    
    
        
    

