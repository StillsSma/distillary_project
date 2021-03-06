from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import django_excel as excel
import requests

from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from inventory.models import InventoryItem, Product, Stray, Destination
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from inventory.forms import InventoryForm, CaseRemovalForm, StrayForm, StrayRemovalForm, InventoryUpdateForm, InventoryReportForm
from inventory.data_entry import case_entry, case_remove, case_delete, stray_entry, stray_remove, stray_delete, case_update


class UserCreateView(UserPassesTestMixin, CreateView):
    model = User
    success_url = reverse_lazy("inventory_summary_view")
    form_class = UserCreationForm
    def form_valid(self, form): #logs the user in upon account creation
        valid = super(UserCreateView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
    def test_func(self):
        return self.request.user.is_superuser

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
def inventory_report_view(request):
    if request.method == "POST":
        r = request.POST
        form = InventoryUpdateForm()
        start = datetime.strptime(r['from'], "%m/%d/%Y")
        end = datetime.strptime(r['to'], "%m/%d/%Y") + timedelta(hours=24)
        if r['destination'] == '':
            cases = InventoryItem.objects.filter(date_removed__range=[start, end])
        else:
            dest = Destination.objects.get(pk=int(r['destination']))
            cases = InventoryItem.objects.filter(date_removed__range=[start, end]).filter(destination=dest)
        context = {
        "object_list" : cases,
        "form" : InventoryReportForm()
        }
    else:
        context = {
        "form" : InventoryReportForm()

        }
    return render(request, 'inventory_item_report.html', context)

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
        if len(InventoryItem.objects.all()) > 0:
            i = InventoryItem.objects.last().case_number
            form = InventoryForm(initial = {'starting_case_number': i + 1 })
        else:
            form = InventoryForm(initial = {'starting_case_number': 1 })

    return render(request, 'create.html', {'form': form})

@login_required
def inventory_update_view(request):
    if request.method == "POST":
        case_update(request)
        return HttpResponseRedirect(reverse_lazy('inventory_list_view'))
    else:
        cases = request.GET.getlist('checks')
        if len(cases) > 0:
            case = InventoryItem.objects.get(id=cases[0])
            if case.destination != None:
                destination = Destination.objects.get(name=case.destination).id
            else:
                destination = ''
            form = InventoryUpdateForm(initial = {
            'date_assigned':case.date_assigned ,
            'name':case.name ,
            'proof':case.proof ,
            'date_removed': case.date_removed,
            'destination': destination,
            })


        else:
            return HttpResponseRedirect(reverse_lazy('inventory_list_view'))
    return render(request, 'inventory_item_update.html', {'form': form})

@login_required
def inventory_removal_view(request):
    if request.method == "POST":
        r = request
        form = CaseRemovalForm(request.POST)
        if form.is_valid():
            case_remove(r)
            return HttpResponseRedirect(reverse_lazy('inventory_removal_view'))
    else:
        form = CaseRemovalForm()

    return render(request, 'removal.html', {'form': form})

@login_required
def inventory_delete_view(request):
    print(request)
    if request.method == "POST":
        print(request.GET.getlist('checks'))
        case_delete(request)
        return HttpResponseRedirect(reverse_lazy('inventory_list_view'))
    else:
        pass
    return render(request, 'inventory_item_confirm_delete.html')




@login_required
def stray_create_view(request):
    if request.method == "POST":
        r = request.POST
        form = StrayForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Successfully Added Stray.')
            stray_entry(r)
            return HttpResponseRedirect(reverse_lazy('inventory_summary_view'))
    else:
        form = StrayForm()
    return render(request, 'create_stray.html', {'form': form})

@login_required
def stray_removal_view(request):
    if request.method == "POST":
        r = request
        form = StrayRemovalForm(r.POST)
        if form.is_valid():
            stray_remove(r)
            return HttpResponseRedirect(reverse_lazy('stray_removal_view'))
    else:
        form = StrayRemovalForm()

    return render(request, 'stray_removal.html', {'form': form})

@login_required
def stray_delete_view(request):
    if request.method == "POST":
        print(request.GET.getlist('checks'))
        stray_delete(request)
        return HttpResponseRedirect(reverse_lazy('inventory_list_view'))
    else:
        pass
    return render(request, 'stray_confirm_delete.html')


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


class DestinationListView(LoginRequiredMixin, ListView):
    model = Destination

    def get_queryset(self):
        return Destination.objects.all().order_by('name')


class DestinationCreateView(LoginRequiredMixin, CreateView):
    model = Destination
    fields = ['name', 'address']
    success_url = reverse_lazy("destination_list_view")

class DestinationUpdateView(LoginRequiredMixin, UpdateView):
    model = Destination
    fields = ['name', 'address']
    success_url = reverse_lazy("destination_list_view")

class DestinationDeleteView(LoginRequiredMixin, DeleteView):
    model = Destination
    success_url = reverse_lazy("destination_list_view")
