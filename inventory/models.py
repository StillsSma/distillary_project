from django.db import models

# Create your models here.
class InventoryItem(models.Model):
    case_number = models.IntegerField()
    date_assigned = models.DateField()
    name = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    bottle_size = models.DecimalField(max_digits=5,decimal_places=3)
    proof = models.DecimalField(max_digits=5,decimal_places=2)
    number_of_cases = models.IntegerField()
    stray_bottles = models.IntegerField(null=True,blank=True)
    date_removed = models.DateField(null=True,blank=True)
    invoice_number = models.IntegerField(null=True,blank=True)
