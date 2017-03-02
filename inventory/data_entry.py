from inventory.models import InventoryItem, Product, Stray, Destination
from datetime import datetime
from django.contrib import messages

def case_entry(request):

    count = 0
    for item in range(int(request['number_of_cases'])):
        inventory_item = InventoryItem.objects.create(case_number=(int(request['starting_case_number']) + count),
        date_assigned=datetime.strptime(request['date_assigned'], "%m/%d/%Y"),
        name=Product.objects.get(pk=request['name']),
        proof=float(request['proof']), case_fraction=float(request['case_fraction']))

        inventory_item.save()
        count += 1



def case_remove(request):
    # You can't filter single objects, so the single case is represented by as a queryset with one object
        case = InventoryItem.objects.filter(case_number=int(request.POST['case_id']))
        for item in case:
            print(item.destination)
        if len(case) != 0:
            for item in case:
                if item.destination == None:
                    case.update(date_removed=datetime.now(),destination=Destination.objects.get(pk=request.POST['destination']).name)
                    messages.success(request, 'Case Removed.')
                else:
                    messages.info(request, 'Case Already Removed')
        else:
            messages.info(request, 'Case Does Not Exist.')

def case_update(request):
    g = request.GET
    p = request.POST
    for num in g.getlist('checks'):
        InventoryItem.objects.filter(pk=num).update(name=p['name'],
        date_assigned=p['date_assigned'],
        proof=p['proof'],
        destination=Destination.objects.get(pk=request.POST['destination']).name,
        date_removed=p['date_removed'])

def case_delete(request):
    for num in request.GET.getlist('checks'):
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
    for num in request.GET.getlist('checks'):
        Stray.objects.get(id=num).delete()
