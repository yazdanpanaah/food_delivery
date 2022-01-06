from django import forms
from django.utils.translation import override
from django.utils.translation import gettext_lazy as _

# FOODMENU_NUMBER_CHOICES = [(i,str(i)) for i in range (1,21)]

class CartAddProductForm(forms.Form):
    # number = forms.TypedChoiceField(choices=FOODMENU_NUMBER_CHOICES,coerce=int,label=_("Number"))
    number = forms.IntegerField()
    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)#do not show this field to user
    