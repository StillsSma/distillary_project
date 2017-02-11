from django import forms

class InventoryForm(forms.Form):


    starting_case_number = forms.IntegerField(initial=213)
    date_assigned = forms.DateField(initial="10/23/1993")
    name = forms.CharField(initial='some whiskey')
    bottle_size = forms.DecimalField(initial=6.3)
    proof = forms.DecimalField(initial=88.4)
    number_of_cases = forms.IntegerField(initial=20)
    stray_bottles = forms.IntegerField(required=False, initial=0)
    date_removed = forms.DateField(required=False)
    invoice_number = forms.IntegerField(required=False, initial=0)
