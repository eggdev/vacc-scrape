from datetime import datetime, timedelta
from ignored import cookies, headers
import json
import requests

url = (
    "https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability"
)

data = {
    "serviceId": "99",
    "position": {"latitude": 40.9505752, "longitude": -73.7301331},
    "appointmentAvailability": {"startDateTime": "2021-04-08"},
    "radius": 25,
}


def run():
    today = datetime.today()
    tomorrow = today + timedelta(days=1)
    data["appointmentAvailability"]["startDateTime"] = tomorrow.strftime("%Y-%m-%d")
    response = requests.post(url=url, headers=headers, cookies=cookies, json=data)
    return response.json()


if __name__ == "__main__":
    run()