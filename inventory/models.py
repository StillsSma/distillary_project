from django.db import models
from django.db.models import Sum


class Destination(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(null=True, max_length=100)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    UPC = models.CharField(max_length=20)
    bottle_size = models.IntegerField()

    def __str__(self):
        return str(self.product_name)

    @property
    def number_of_strays(self):
        return Stray.objects.filter(name=self).count()

    @property
    def number_of_cases(self):
        return InventoryItem.objects.filter(name=self).count()

    @property
    def total_liters(self):
        cases = InventoryItem.objects.filter(name=self)
        liters = []
        for case in cases:
            liters.append(case.liters)
        return sum(liters)

    @property
    def total_wine_gallons(self):
        return round((float(self.total_liters) * .264172),2)

    @property
    def total_proof_gallons(self):
        cases = InventoryItem.objects.filter(name=self)
        proof_gallons = []
        for case in cases:
            proof_gallons.append(case.proof_gallons)
        return round(sum(proof_gallons),2)


class InventoryItem(models.Model):
    case_number = models.IntegerField(unique=True)
    date_assigned = models.DateField()
    name = models.ForeignKey(Product, on_delete=models.PROTECT)
    proof = models.DecimalField(max_digits=5,decimal_places=2)
    date_removed = models.DateTimeField(null=True,blank=True)
    destination = models.CharField(null=True,max_length=100)
    case_fraction = models.DecimalField(max_digits=5,decimal_places=4,default=1.0)

    def __str__(self):
        return str(self.name)

    @property
    def bottles_per_case(self):
        if self.name.bottle_size == 750:
            return int(round(6 * self.case_fraction,0))
        elif self.name.bottle_size == 375:
            return int(round(12 * self.case_fraction,0))

    @property
    def product(self):
        return self.name.product_type

    @property
    def liters(self):
        return round(self.name.bottle_size/1000 * self.bottles_per_case,2)

    @property
    def wine_gallons(self):
        return round((float(self.liters) * .264172),2)

    @property
    def proof_gallons(self):
        return round((int(self.proof)/100 * self.wine_gallons), 2)

class Stray(models.Model):
    date_assigned = models.DateField()
    name = models.ForeignKey(Product, on_delete=models.PROTECT)
    proof = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return str(self.name)

    @property
    def product(self):
        return self.name.product_type
