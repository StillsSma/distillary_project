from django import forms
from inventory.models import Product, InventoryItem
from django.forms import ModelChoiceField

class ProductChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.product_name



class InventoryForm(forms.Form):

    BOTTLES = [
    ("12 ", "12"),
    ("6 ", "6")
    ]


    starting_case_number = forms.IntegerField()
    name = ProductChoiceField(queryset=Product.objects.all(), empty_label=None)
    bottles_per_case= forms.ChoiceField(choices=BOTTLES)
    proof = forms.DecimalField()
    number_of_cases = forms.IntegerField()
    stray_bottles = forms.IntegerField(required=False, initial=0)

class RemovalForm(forms.Form):
    starting_case_number = forms.IntegerField()
    number_of_cases = forms.IntegerField()
    information = forms.CharField(widget=forms.Textarea)
