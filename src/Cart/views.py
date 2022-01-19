# from django.core.checks import messages
from django.shortcuts import render , get_object_or_404 , redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from restaurant.models import *
from .forms import CartAddProductForm
from django.contrib import messages
from accounts.forms import *
from accounts.models import *


@require_POST
def cart_add(request,foodmenu_id):
    cart = Cart(request)
    foodmenu = get_object_or_404(FoodMenu,id=foodmenu_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
    if not (request.session.get(settings.CART_SESSION_ID)):
        request.session['branch'] = foodmenu.department.id
    
    if request.session['branch'] == foodmenu.department.id: 
        cart.add(foodmenu = foodmenu ,number= int(request.POST['number']),override_number=cd['override'])
        
    else:
        cart.clear() 
        messages.error(request, "you can not order from diffrent branches!choose your items again")
    return redirect('cart:carts_detail')
        

        

@require_POST
def cart_remove(request,foodmenu_id):
    cart = Cart(request)
    foodmenu = get_object_or_404(FoodMenu,id=foodmenu_id)
    if request.user.is_authenticated:
            user = request.user.customer.id
            user = Customer.objects.get(id=user)
            if Order.objects.filter(customer= user).exists():
                orderitem = OrderItem.objects.filter(foodmenu = foodmenu_id).delete()



            foodmenu = get_object_or_404(FoodMenu,id=foodmenu_id)
            cart.remove(foodmenu)


    foodmenu = get_object_or_404(FoodMenu,id=foodmenu_id)
    cart.remove(foodmenu)
    return redirect('cart:carts_detail')


def cart_detail(request):
    cart = Cart(request)
    cart_items = [item['foodmenu'] for item in cart]
    for item in cart:
        item['update_number_form'] = CartAddProductForm(initial={
            'number':item["number"],
            "override":True,
        })
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=request.user.id)
        form=AddAddressForm()
        addresses = Adress.objects.filter(owner=customer)
        return render(request,'cart/detail.html',{'cart':cart ,'address_list':addresses,'form':form })
    
    
    return render(request,'cart/detail.html',{'cart':cart})
    

    
    

    

