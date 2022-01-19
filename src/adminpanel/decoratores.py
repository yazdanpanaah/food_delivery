from django.contrib.auth.mixins import UserPassesTestMixin 
from django.views.generic import View 
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.admin.views.decorators import user_passes_test
 
 
def superuser_required(): 
    def wrapper(wrapped): 
        class WrappedClass(UserPassesTestMixin, wrapped): 
            def test_func(self): 
                return self.request.user.is_superuser 
 
        return WrappedClass 
    return wrapper 



# def is_superuser(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
#                    login_url='/login'):
#     """
#     Decorator for views that checks that the user is logged in and is a
#     superuser, redirecting to the login page if necessary.
#     """
#     actual_decorator = user_passes_test(
#         lambda u: u.is_active and u.is_superuser,
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#     if view_func:
#         return actual_decorator(view_func)
#     return actual_decorator