from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import django_excel as excel
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from inventory.models import InventoryItem, Product, Stray
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from inventory.forms import InventoryForm, RemovalForm
from inventory.data_entry import case_entry, case_remove
from django.contrib import messages


class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy("inventory_summary_view")
    form_class = UserCreationForm
    def form_valid(self, form): #logs the user in upon account creation
        valid = super(UserCreateView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class InventoryListView(LoginRequiredMixin, ListView):
    # Lists the items currently in inventory
    model = InventoryItem
    def get_queryset(self):
        return InventoryItem.objects.all().order_by('case_number')
    def get_context_data(self, **kwargs):
        # Gather queryset for stray bottles
        context = super(InventoryListView, self).get_context_data(**kwargs)
        strays = Stray.objects.all()
        context['strays'] = strays
        return context

class InventorySummaryView(LoginRequiredMixin, ListView):

    model = Product
    def get_template_names(self):
        return('inventory/inventory_summary.html')


@login_required
def inventory_form_view(request):
    if request.method == "POST":
        r = request.POST

        form = InventoryForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Successfully Added.')
            case_entry(r)
            return HttpResponseRedirect(reverse_lazy('inventory_summary_view'))
    else:
        i = len(InventoryItem.objects.all())
        form = InventoryForm(initial = {'starting_case_number': i + 1 })

    return render(request, 'create.html', {'form': form})


@login_required
def inventory_removal_view(request):
    if request.method == "POST":
        r = request.POST
        print(r)
        form = RemovalForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Case Removed.')
            case_remove(r)
            return HttpResponseRedirect(reverse_lazy('inventory_removal_view'))
    else:
        form = RemovalForm()

    return render(request, 'remove.html', {'form': form})


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['product_name', 'product_type', 'UPC', 'bottle_size']
    success_url = reverse_lazy("product_list_view")

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['product_name', 'product_type', 'UPC', 'bottle_size']
    success_url = reverse_lazy("product_list_view")

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("product_list_view")
