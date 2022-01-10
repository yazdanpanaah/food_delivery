from django.shortcuts import get_object_or_404, render ,redirect
from Cart.forms import *
from restaurant.models import Department, Food, FoodMenu
from django.db.models.aggregates import Count, Sum
from Cart.cart import Cart
# Create your views here.
def home(req):
    foodmenu = FoodMenu.objects.all()
    food = Food.objects.all()
    best_food = Food.objects.all().filter(food2__foodmenu2__order__status = "order_registration").annotate(our_sum=Sum("food2__foodmenu2__number")).order_by("-our_sum")[:3]
    print('--------------------------------')
    print(best_food)
    print('--------------------------------')
    # print(req.user.customer.id)


    best_department = Department.objects.filter(food__food2__foodmenu2__order__status="order_registration").annotate(sums =Sum("food__food2__foodmenu2__order__total_price") ).order_by("-sums")[:3]
    
    context ={
        'foodmenus':foodmenu,
        'foods': food,
        'best_food': best_food,
        'best_department': best_department
    }
    return render(req, 'home.html',context)

def food_detail(request,id):
    foodmenu = get_object_or_404(FoodMenu,id=id)
    cart_foodmenu_form = CartAddProductForm()
    cart = Cart(request)
    
            
    context = {
        'foodmenu':foodmenu,
        'form': cart_foodmenu_form
    }

    return render(request, "cart/food/food_detail.html",context)



# def add_cart_to_db(req,id):
#     food= req.session['price']
#     return food


