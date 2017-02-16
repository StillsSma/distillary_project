"""distillary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from inventory.views import InventoryListView, ProductListView, ProductCreateView, \
                            ProductDeleteView, ProductUpdateView, inventory_form_view, \
                            inventory_removal_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inventory/$', InventoryListView.as_view(), name='inventory_list_view'),
    url(r'^inventory/create/$', inventory_form_view, name="inventory_form_view"),
    url(r'^inventory/remove/$', inventory_removal_view, name="inventory_removal_view"),
    url(r'^product/$', ProductListView.as_view(), name="product_list_view"),
    url(r'^product/create/$', ProductCreateView.as_view(), name="product_create_view"),
    url(r'^product/update$', ProductUpdateView.as_view(), name="product_update_view"),
    url(r'^product/delete$', ProductDeleteView.as_view(), name="product_delete_view"),
]
