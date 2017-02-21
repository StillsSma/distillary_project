from inventory.models import InventoryItem, Product, Stray
from datetime import datetime
def case_entry(request):

    count = 0
    for item in range(int(request['number_of_cases'])):
        inventory_item = InventoryItem.objects.create(case_number=(int(request['starting_case_number']) + count),
         name=Product.objects.get(pk=request['name']),
        bottle_size=float(request['bottle_size']), proof=float(request['proof']),
        number_of_cases=int(request['number_of_cases']))

        inventory_item.save()
        count += 1
    for num in range(int(request['stray_bottles'])):
        stray_bottle = Stray.objects.create(name=Product.objects.get(pk=request['name']),
                                        proof=float(request['proof']),bottle_size=float(request['bottle_size']))
        stray_bottle.save()



def case_remove(request):
    InventoryItem.objects.filter(case_number=int(request['case_id'])).update(date_removed=datetime.now())

def bottle_entry(request):
    pass
