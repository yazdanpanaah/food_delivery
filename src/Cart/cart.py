from django.conf import settings
from restaurant.models import *


class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            
        self.cart = cart
        
    # add to cart
    def add(self,foodmenu,number=1,override_number=False):
        foodmenu_id = str(foodmenu.id)
        if foodmenu_id not in self.cart:
            self.cart[foodmenu_id] = {'number':0,'price':foodmenu.price }
        if override_number:
            self.cart[foodmenu_id]['number'] = number
        else:
            self.cart[foodmenu_id]['number'] += number
        self.save()
    
    def save(self):
        self.session.modified = True
    
    #remove from cart
    def remove(self,foodmenu):
        foodmenu_id = str(foodmenu.id)
        if foodmenu_id in self.cart:
            del self.cart[foodmenu_id]
            self.save()
    
    def __iter__(self):
        foodmenu_ids = self.cart.keys()
        foodmenus = FoodMenu.objects.filter(id__in=foodmenu_ids)
        
        cart = self.cart.copy()
        for food in foodmenus:
            cart[str(food.id)]['foodmenu'] = food
        
        for item in cart.values():
            item['total_price'] = item['price'] * item['number']
            yield item
    
    def __len__(self):#return number of items in cart
        return sum(item['number'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(item['price'] * item['number'] for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
    
    