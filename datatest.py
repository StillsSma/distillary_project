from pyexcel_xlsx import get_data
from datetime import datetime
import json

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

data = get_data("Software_Project/Bottling Records through 29 JAN 17.xlsx")
print(json.dumps(data,cls=DateTimeEncoder))
