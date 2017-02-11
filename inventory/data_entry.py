from inventory.models import InventoryItem
from datetime import datetime
def datafunction(request):
    count = 0
    for item in range(int(request['number_of_cases'])):
        inventory_item = InventoryItem.objects.create(case_number=(int(request['starting_case_number']) + count),
        date_assigned=datetime.strptime(request['date_assigned'], '%m/%d/%Y'), name=request['name'],
        bottle_size=float(request['bottle_size']), proof=float(request['proof']),
        number_of_cases=int(request['number_of_cases']),
        stray_bottles=int(request['stray_bottles']))


        inventory_item.save()
        count += 1
