from email import message
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic.edit import DeleteView,CreateView,UpdateView
# Create your views here.
from restaurant.models import *
from django.urls import reverse_lazy
from .decoratores import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from  django.db.models import ProtectedError
from django.http import  HttpResponseRedirect

# @user_passes_test(lambda u: u.is_superuser)
def adminpanel(req):
    if req.user.is_superuser:
        foods = Food.objects.all()
        context = {'food': foods}
        return render(req,'adminpanel/admin.html',context)
    else:
        messages.error(req, "you are not site admin!please log as site admin ")
        return redirect('login')
    

@superuser_required()
class AddFood(CreateView):
    model = Food
    success_url = reverse_lazy('admin')
    template_name = 'adminpanel/addfood.html'
    fields = "__all__"


class DeleteFood(DeleteView):
    model = Food
    success_url = reverse_lazy('admin')
    template_name = 'adminpanel/deletefood.html'
    fields = "__all__"
    # def delete(self, request, *args, **kwargs):
    #     """
    #     Call the delete() method on the fetched object and then redirect to the
    #     success URL. If the object is protected, send an error message.
    #     """
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()

    #     try:
    #         self.object.delete()
    #     except ProtectedError:
    #         messages.add_message(request, messages.ERROR, 'Can not delete: this parent has a child!')
    #         return # The url of the delete view (or whatever you want)

    #     return HttpResponseRedirect(success_url)


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
