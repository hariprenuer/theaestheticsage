import datetime
import random
import json


def sample_gen(d,m,y):
        # Start date
    start_date = datetime.date(y, m, d)
    # Generate data for 1 year (365 days)
    data = []
    for i in range(365):
        day = start_date + datetime.timedelta(days=i)
        value = round(random.uniform(10.0, 100.0), 2)
        data.append({
            "date": day.isoformat(),
            "value": value
        })

    # Convert to JSON string (for example use)
    json_output = json.dumps(data, indent=2)
    # print(json_output)
    return data
