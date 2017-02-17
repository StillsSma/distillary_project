from inventory.models import InventoryItem, Product
from datetime import datetime
def case_entry(request):
    count = 0
    for item in range(int(request['number_of_cases'])):
        inventory_item = InventoryItem.objects.create(case_number=(int(request['starting_case_number']) + count),
         name=Product.objects.get(pk=request['name']),
        bottles_per_case=int(request['bottles_per_case']), proof=float(request['proof']),
        number_of_cases=int(request['number_of_cases']),
        invoice_number=Product.objects.get(pk=request['name']).invoice_number,
        stray_bottles=int(request['stray_bottles']))


        inventory_item.save()
        count += 1

def case_remove(request):
    InventoryItem.objects.filter(case_number=int(request['case_id'])).update(date_removed=datetime.today())
