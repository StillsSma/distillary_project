from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from inventory.models import InventoryItem, Product
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from inventory.forms import InventoryForm, RemovalForm
from inventory.data_entry import case_entry, case_remove

class InventoryListView(ListView):
    model = InventoryItem

def inventory_form_view(request):
    if request.method == "POST":
        r = request.POST
        print(r)
        form = InventoryForm(request.POST)
        if form.is_valid():
            case_entry(r)
            return HttpResponseRedirect('/inventory/')
    else:
        form = InventoryForm()

    return render(request, 'create.html', {'form': form})

def inventory_removal_view(request):
    if request.method == "POST":
        r = request.POST
        print(r)
        form = RemovalForm(request.POST)
        if form.is_valid():
            case_remove(r)
            return HttpResponseRedirect('/inventory')
    else:
        form = RemovalForm()

    return render(request, 'remove.html', {'form': form})


class ProductListView(ListView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ['product_name', 'product_type', 'invoice_number']
    success_url = reverse_lazy("product_list_view")

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['product_name', 'product_type', 'invoice_number']
    success_url = reverse_lazy("product_list_view")

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product_list_view")
