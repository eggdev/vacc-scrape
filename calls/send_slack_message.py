#!/usr/bin/env python3
from ignored import slack_url
import json
import requests

headers = {"content-type": "application/json"}


def send_message(response):
    is_available = response["appointmentsAvailable"]
    payload = {
        "text": f"Availability = {is_available}",
        "blocks": [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": json.dumps(response, indent=4)},
            },
        ],
    }
    res = requests.post(url=slack_url, headers=headers, json=payload)
    print(res)
