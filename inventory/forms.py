from django import forms
from inventory.models import Product, InventoryItem, Destination
from django.forms import ModelChoiceField

class ModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj


class InventoryForm(forms.Form):

    FRACTION = [
    (1.0, 'Whole'),
    (.083,'1/12'),
    (.167,'2/12, 1/6'),
     (.25,'3/12,'),
     (.333,'4/12, 2/6'),
     (.417,'5/12'),
     (.5,'6/12, 3/6'),
     (.583, '7/12'),
     (.666,'8/12, 4/6'),
     (.75, '9/12'),
     (.833, '10/12, 5/6'),
     (.917, '11/12'),
    ]

    starting_case_number = forms.IntegerField(min_value=1)
    date_assigned = forms.DateField()
    name = ModelChoiceField(queryset=Product.objects.all())
    proof = forms.DecimalField(min_value=0)
    number_of_cases = forms.IntegerField(min_value=1)
    case_fraction = forms.ChoiceField(choices=FRACTION)

class InventoryUpdateForm(forms.Form):

    date_assigned = forms.DateField()
    name = ModelChoiceField(queryset=Product.objects.all())
    proof = forms.DecimalField(min_value=0)
    date_removed = forms.DateTimeField(required=False)
    destination = ModelChoiceField(required=False, queryset=Destination.objects.all())

class InventoryReportForm(forms.Form):
    destination = ModelChoiceField(queryset=Destination.objects.all(), empty_label='all', required=False)


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
