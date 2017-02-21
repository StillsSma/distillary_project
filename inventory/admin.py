from django.contrib import admin
from inventory.models import InventoryItem, Product, Stray
# Register your models here.
admin.site.register(InventoryItem)
admin.site.register(Product)
admin.site.register(Stray)
