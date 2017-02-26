from django import forms
from inventory.models import Product, InventoryItem
from django.forms import ModelChoiceField

class ProductChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.product_name



class InventoryForm(forms.Form):

    starting_case_number = forms.IntegerField()
    date_assigned = forms.DateField()
    name = ProductChoiceField(queryset=Product.objects.all(), empty_label=None)
    proof = forms.DecimalField()
    number_of_cases = forms.IntegerField()

class StrayForm(forms.Form):
    date_assigned = forms.DateField()
    name = ProductChoiceField(queryset=Product.objects.all(), empty_label=None)
    proof = forms.DecimalField()
    number_of_bottles = forms.IntegerField()


class RemovalForm(forms.Form):


    case_id = forms.IntegerField(label='Case Number')
    information = forms.CharField(widget=forms.Textarea, required=False, label='Info')
