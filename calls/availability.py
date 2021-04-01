import requests
import json
from ignored import cookies, headers

url = (
    "https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability"
)

data = {
    "serviceId": "99",
    "position": {"latitude": 41.0901834, "longitude": -73.541744},
    "appointmentAvailability": {"startDateTime": "2021-04-02"},
    "radius": 25,
}


def run():
    response = requests.post(url=url, headers=headers, cookies=cookies, json=data)
    return response.json()


if __name__ == "__main__":
    run()