from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    product_number = models.IntegerField()

    def __str__(self):
        return str(self.product_name)
    @property
    def number_of_strays_small(self):
        return Stray.objects.filter(name=self).filter(bottle_size=.375).count()
    @property
    def number_of_strays_large(self):
        return Stray.objects.filter(name=self).filter(bottle_size=.750).count()


class InventoryItem(models.Model):
    case_number = models.IntegerField(unique=True)
    date_assigned = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(Product, on_delete=models.PROTECT)
    bottle_size = models.DecimalField(max_digits=3,decimal_places=3)
    proof = models.DecimalField(max_digits=5,decimal_places=2)
    number_of_cases = models.IntegerField()
    date_removed = models.DateTimeField(null=True,blank=True)


    @property
    def bottles_per_case(self):
        if self.bottle_size == .750:
            return 6
        elif self.bottle_size == .375:
            return 12

    @property
    def product(self):
        return self.name.product_type

    @property
    def liters(self):
        return round(self.bottle_size * self.bottles_per_case,2)

    @property
    def wine_gallons(self):
        return round((int(self.liters) * .264172),2)

    @property
    def proof_gallons(self):
        return round((int(self.proof)/100 * self.wine_gallons), 2)

class Stray(models.Model):
    date_assigned = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(Product, on_delete=models.PROTECT)
    proof = models.DecimalField(max_digits=5,decimal_places=2)
    bottle_size = models.DecimalField(max_digits=3,decimal_places=3)

    @property
    def product(self):
        return self.name.product_type
