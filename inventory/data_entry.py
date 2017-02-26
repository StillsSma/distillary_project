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



def case_remove(request):
        InventoryItem.objects.filter(case_number=int(request['case_id'])).update(date_removed=datetime.now())


def case_delete(request):
    for num in request.GET.getlist('to_delete'):
        InventoryItem.objects.get(id=num).delete()


def stray_entry(request):
    for bottle in range(int(request['number_of_bottles'])):
        stray = Stray.objects.create(date_assigned=request['date_assigned'],
                                        name=Product.objects.get(pk=request['name']),
                                        proof=float(request['proof']))

        stray.save()

def stray_delete(request):
    for num in request.GET.getlist('to_delete'):
        Stray.objects.get(id=num).delete()
