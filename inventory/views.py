from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from inventory.models import InventoryItem
from django.views.generic.list import ListView
from inventory.forms import InventoryForm
from inventory.data_entry import datafunction

class InventoryListView(ListView):
    model = InventoryItem

def inventory_form_view(request):
    if request.method == "POST":
        r = request.POST
        form = InventoryForm(request.POST)
        if form.is_valid():
            datafunction(r)
            return HttpResponseRedirect('/inventory/')
    else:
        form = InventoryForm()

    return render(request, 'create.html', {'form': form})
