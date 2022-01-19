from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from .decorators import *
from restaurant.models import *
from django.views.generic import TemplateView,ListView,UpdateView,CreateView
from django.urls import reverse_lazy
from .forms import *
# Create your views here.

@is_staff_required() 
class MangerProfile(TemplateView): 
    template_name = 'restaurantpanel/profile.html'  
 
@is_staff_required() 
class DepartmentView(ListView): 
    model = Department
    template_name = 'restaurantpanel/branch.html' 
    def get_queryset(self, *args, **kwargs): 
        return Department.objects.filter(manager = self.request.user.id)   
 
@is_staff_required()
class UpdateDepartment(UpdateView): 
    model = Department 
    template_name = "restaurantpanel/update_branch.html"  
    fields = "__all__" 
    success_url = reverse_lazy('managerprofile') 
 
@is_staff_required() 
class FoodMenuView(ListView): 
    model = FoodMenu 
    template_name = "restaurantpanel/foodmenu.html" 
    def get_queryset(self, *args, **kwargs): 
        return FoodMenu.objects.filter(department__manager= self.request.user.id)  

class UpdateFoodMenu(UpdateView): 
    model = FoodMenu 
    template_name = "restaurantpanel/update_foodmenu.html" 
    fields = ['price','number']
    success_url = reverse_lazy('mangerprofile')
    


def create_foodmenu(request,pk):
    if request.method == 'POST':
        form = CreateFoodMenuForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            department = Department.objects.get(manager= request.user.id)
            foodmenu = FoodMenu.objects.create(food=cd['food'], department = department, number=cd['number'],price=cd['price'])
            foodmenu.save()
            return redirect('mangerprofile')
    else:
        form = CreateFoodMenuForm()
        context = {'form':form}
        return render(request, 'restaurantpanel/create_food.html', context)


def deletefoodmenu(request,pk): 
    delete_food=FoodMenu.objects.filter(id=pk) 
    delete_food.delete() 
    return redirect('foodmenu_view')
    # return render(request, "restaurantpanel/foodmenu.html")


def order_status(request):
    department = Department.objects.get(manager= request.user.id)
    
    order = Order.objects.all().filter(order__foodmenu__department__id= department.id).exclude(status="order")
    print('--------query---------')
    print(order)
    return render(request, 'restaurantpanel/order_status.html',{'order':order})


class UpdateStatus(UpdateView):
    model = Order 
    template_name = "restaurantpanel/update_status.html" 
    fields = ['status']
    success_url = reverse_lazy('order_status')

# def update_status(request ,id):
#     if request.POST:
#         status = request.POST.get('status')
#         update_status = Order.objects.filter(id =id).update(status= status)

