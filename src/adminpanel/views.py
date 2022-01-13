from django.shortcuts import render
from django.views.generic.edit import DeleteView,CreateView,UpdateView
# Create your views here.
from restaurant.models import *
from django.urls import reverse_lazy
from .decoratores import *
from django.contrib.auth.decorators import login_required

@login_required
def adminpanel(req):
    foods = Food.objects.all()
    context = {'food': foods}
    return render(req,'adminpanel/admin.html',context)
    
@superuser_required()
class AddFood(CreateView):
    model = Food
    success_url = reverse_lazy('admin')
    template_name = 'adminpanel/addfood.html'
    fields = "__all__"

@superuser_required()
class DeleteFood(DeleteView):
    model = Food
    success_url = reverse_lazy('admin')
    template_name = 'adminpanel/deletefood.html'
    fields = "__all__"
@superuser_required()
class UpdateFood(UpdateView):
    model = Food
    success_url = reverse_lazy('admin')
    template_name = 'adminpanel/updatefood.html'
    fields = "__all__"

@superuser_required()
class AddCategory(CreateView):
    model = Category
    success_url = reverse_lazy('admin')
    template_name = 'adminpanel/updatefood.html'
    fields = "__all__"
