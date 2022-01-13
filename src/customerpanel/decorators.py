from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View

from accounts.models import Customer
from django.http import HttpResponse



def customer_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return not (self.request.user.is_staff) and not (self.request.user.is_superuser)

        return WrappedClass
    return wrapper 

# def customer_required2():
#     def wrapper(request, *args, **kwargs):
#         user = request.customer
#         customer = Customer.objects.get(id=user.id) #id
#         if not (user.is_staff) and not (user.is_superuser):
#             return function(request, *args, **kwargs)
            
#         else:
#             return HttpResponse('You cannot view this.')
            
#     return wrapper
