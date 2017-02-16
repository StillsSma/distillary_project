from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    invoice_number = models.IntegerField()

    def __str__(self):
        return str(self.product_name)


class InventoryItem(models.Model):
    case_number = models.IntegerField()
    date_assigned = models.DateField(auto_now_add=True)
    name = models.ForeignKey(Product, on_delete=models.PROTECT)
    bottles_per_case = models.IntegerField()
    proof = models.DecimalField(max_digits=5,decimal_places=2)
    number_of_cases = models.IntegerField()
    stray_bottles = models.IntegerField(null=True,blank=True)
    date_removed = models.DateField(null=True,blank=True)
    invoice_number = models.IntegerField()


    @property
    def bottle_size(self):
        if self.bottles_per_case == 6:
            return .750
        elif self.bottles_per_case == 12:
            return .375
        else:
            pass

    @property
    def product(self):
        return self.name.product_type

    @property
    def liters(self):
        return self.bottle_size * self.bottles_per_case

    @property
    def wine_gallons(self):
        return round((self.liters * .264172),2)

    @property
    def proof_gallons(self):
        return round((int(self.proof)/100 * self.wine_gallons), 2)
