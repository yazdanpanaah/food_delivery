from django.shortcuts import get_object_or_404, render ,redirect 
from django.template.loader import render_to_string
from Cart.forms import *
from restaurant.models import Department, Food, FoodMenu, Order
from django.db.models.aggregates import Count, Sum
from Cart.cart import Cart
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.
def home(req):
    foodmenu = FoodMenu.objects.all()
    food = Food.objects.all()
    # if Order.objects.all().filter(status="Send").exists():
    #     best_food = FoodMenu.objects.all().filter(foodmenu2__order__status = "Send").annotate(our_sum=Sum("foodmenu2__number")).order_by("-our_sum")[:3]


    # elif Order.objects.all().filter(status="Delivery").exists():

    #     best_food = FoodMenu.objects.all().filter(foodmenu2__order__status = "Delivery").annotate(our_sum=Sum("foodmenu2__number")).order_by("-our_sum")[:3]

    # else:
    best_food = FoodMenu.objects.all().filter(foodmenu2__order__status = "order_registration").annotate(our_sum=Sum("foodmenu2__number")).order_by("-our_sum")[:3]

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
    # all_menu= FoodMenu.objects.all().filter(department = foodmenu.department.id)
    cart_foodmenu_form = CartAddProductForm()
    cart = Cart(request)
    
            
    context = {
        'foodmenu':foodmenu,
        'form': cart_foodmenu_form,
        # 'allmenu':all_menu
    }

    return render(request, "cart/food/food_detail.html",context)

def all_item(request, id):
    foodmenu = get_object_or_404(FoodMenu,id=id)
    all_menu= FoodMenu.objects.all().filter(department = foodmenu.department.id)
    print(all_menu)
    return render(request , 'restaurants/menu.html',{'menus':all_menu ,'branch':foodmenu.department})


def search_result(req):
    if req.is_ajax():
        
        if req.POST.get('data')!= None:
            result = req.POST.get('data')
            q = FoodMenu.objects.filter(Q(food__name__icontains= result)| Q(department__name__icontains=result))
            if len(q) > 0 and len(result) > 0:
                print('-----hi------')
                data =[]
                for i in q:
                    item ={
                        'pk' : i.pk,
                        'food':{'name':i.food.name, 'photo':i.food.photo.url},
                        'branch': {'department':i.department.name},
                        'price': i.price,
                        'number': i.number
                    }
                    data.append(item)
                res = data
            else:
                print('-----buyyy------')
                res = "No Food Or Restaurant Found..."

            return JsonResponse({'dataview':res})
    return JsonResponse({})

def branch_menu(request):
    branch = Department.objects.all()
    return render(request, "restaurants/branch_menu.html",{'branch':branch})

def show_menu(request,id):
    branch = Department.objects.get(id = id)
    foodmenu = FoodMenu.objects.all().filter(department = branch.id)
    return render(request, "restaurants/show_menu.html",{'foodmenu':foodmenu})












# def add_cart_to_db(req,id):
#     food= req.session['price']
#     return food


# def search_result(req):
# 	results=[]
# 	if req.method == "GET":
# 		query = req.GET.get('search')
# 		if query == '':
# 			query = 'None'
# 		results = FoodMenu.objects.filter(Q(food__name__icontains= query)| Q(department__name__icontains=query ))

# 	context ={'query': query, 'results': results}
	
# 	return render(req, 'search.html', context)




# def get_info_search(req, pk):
#     obj = get_object_or_404(FoodMenu, pk=pk)
#     return render(req, 'search.html', {'obj':obj})
# def search(request):
#     q = request.GET.get('q')

#     if q:
#         items = FoodMenu.objects.filter(Q(food__name__icontains = q)
#          | Q(department__name__icontains = q))
#         category = '  Results'
#         print('------search')
#     else : 
#         # items = MenuItem.objects.all()
#         items = {}
#         category = ''
  
#     t = render_to_string('search.html' , 
#     {'products':items , 'request':request , 'category': category })
#     return JsonResponse({'data': t})