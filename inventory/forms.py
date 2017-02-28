from django import forms
from inventory.models import Product, InventoryItem, Destination
from django.forms import ModelChoiceField

class ModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj


class InventoryForm(forms.Form):

    starting_case_number = forms.IntegerField(min_value=1)
    date_assigned = forms.DateField()
    name = ModelChoiceField(queryset=Product.objects.all())
    proof = forms.DecimalField(min_value=0)
    number_of_cases = forms.IntegerField(min_value=1)

class InventoryUpdateForm(forms.Form):

    date_assigned = forms.DateField()
    name = ModelChoiceField(queryset=Product.objects.all())
    proof = forms.DecimalField(min_value=0)
    date_removed = forms.DateTimeField(required=False)
    destination = ModelChoiceField(queryset=Destination.objects.all())

class StrayForm(forms.Form):
    date_assigned = forms.DateField()
    name = ModelChoiceField(queryset=Product.objects.all())
    proof = forms.DecimalField(min_value=0)
    number_of_bottles = forms.IntegerField(min_value=1)


class CaseRemovalForm(forms.Form):
    case_id = forms.IntegerField(label='Case Number')
    destination = ModelChoiceField(queryset=Destination.objects.all())

class StrayRemovalForm(forms.Form):
    name = ModelChoiceField(queryset=Product.objects.all())
    number_of_bottles = forms.IntegerField(min_value=1)
