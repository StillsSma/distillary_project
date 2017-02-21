from django import forms
from inventory.models import Product, InventoryItem
from django.forms import ModelChoiceField

class ProductChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.product_name



class InventoryForm(forms.Form):

    starting_case_number = forms.IntegerField()
    name = ProductChoiceField(queryset=Product.objects.all(), empty_label=None)
    proof = forms.DecimalField()
    number_of_cases = forms.IntegerField()
    stray_bottles = forms.IntegerField(required=False, initial=0)

class RemovalForm(forms.Form):
    case_id = forms.IntegerField(label='Case')
    information = forms.CharField(widget=forms.Textarea, required=False, label='Info')

class FileForm(forms.Form):
    data = forms.FileField()
