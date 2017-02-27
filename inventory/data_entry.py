from inventory.models import InventoryItem, Product, Stray
from datetime import datetime
from django.contrib import messages

def case_entry(request):

    count = 0
    for item in range(int(request['number_of_cases'])):
        inventory_item = InventoryItem.objects.create(case_number=(int(request['starting_case_number']) + count),
        date_assigned=datetime.strptime(request['date_assigned'], "%m/%d/%Y"),
        name=Product.objects.get(pk=request['name']),
        proof=float(request['proof']))

        inventory_item.save()
        count += 1



def case_remove(request):
        case = InventoryItem.objects.filter(case_number=int(request.POST['case_id']))
        if len(case) != 0:
            InventoryItem.objects.filter(case_number=int(request.POST['case_id'])).update(date_removed=datetime.now())
            messages.success(request, 'Case Removed.')
        else:
            messages.info(request, 'Case Does Not Exist.')


def case_delete(request):
    for num in request.GET.getlist('to_delete'):
        InventoryItem.objects.get(id=num).delete()


def stray_entry(request):
    for bottle in range(int(request['number_of_bottles'])):
        stray = Stray.objects.create(date_assigned=datetime.strptime(request['date_assigned'], "%m/%d/%Y"),
                                        name=Product.objects.get(pk=request['name']),
                                        proof=float(request['proof']))

        stray.save()

def stray_remove(request):
    bottles = Stray.objects.filter(name=request.POST['name'])
    if int(request.POST['number_of_bottles']) < int(len(bottles)):
        for num in range(int(request.POST['number_of_bottles'])):
            bottle = bottles.first()
            bottle.delete()
            messages.success(request, 'Successfully Removed Stray.')
    else:
        messages.info(request, 'Not Enough Bottles in Inventory')


def stray_delete(request):
    for num in request.GET.getlist('to_delete'):
        Stray.objects.get(id=num).delete()
