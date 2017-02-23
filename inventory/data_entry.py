from inventory.models import InventoryItem, Product, Stray
from datetime import datetime
def case_entry(request):

    count = 0
    for item in range(int(request['number_of_cases'])):
        inventory_item = InventoryItem.objects.create(case_number=(int(request['starting_case_number']) + count),
        date_assigned=request['date_assigned'],
        name=Product.objects.get(pk=request['name']),
        proof=float(request['proof']))

        inventory_item.save()
        count += 1
    for num in range(int(request['stray_bottles'])):
        stray_bottle = Stray.objects.create(name=Product.objects.get(pk=request['name']),date_assigned=request['date_assigned'],
        proof=float(request['proof']))
        stray_bottle.save()



def case_remove(request):
    InventoryItem.objects.filter(case_number=int(request['case_id'])).update(date_removed=datetime.now())

def cases_remove(request):
    pass
