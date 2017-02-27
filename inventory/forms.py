from django import forms
from inventory.models import Product, InventoryItem
from django.forms import ModelChoiceField

class ProductChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.product_name



class InventoryForm(forms.Form):

    starting_case_number = forms.IntegerField(min_value=1)
    date_assigned = forms.DateField()
    name = ProductChoiceField(queryset=Product.objects.all(), empty_label=None)
    proof = forms.DecimalField(min_value=0)
    number_of_cases = forms.IntegerField(min_value=1)

class StrayForm(forms.Form):
    date_assigned = forms.DateField()
    name = ProductChoiceField(queryset=Product.objects.all(), empty_label=None)
    proof = forms.DecimalField(min_value=0)
    number_of_bottles = forms.IntegerField(min_value=1)


class CaseRemovalForm(forms.Form):
    case_id = forms.IntegerField(label='Case Number')
    information = forms.CharField(widget=forms.Textarea, required=False, label='Info')

class StrayRemovalForm(forms.Form):
    name = ProductChoiceField(queryset=Product.objects.all(), empty_label=None)
    number_of_bottles = forms.IntegerField(min_value=1)
    information = forms.CharField(widget=forms.Textarea, required=False, label='Info')
