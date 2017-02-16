from django.contrib import admin
from inventory.models import InventoryItem, Product
# Register your models here.
admin.site.register(InventoryItem)
admin.site.register(Product)
