#!/usr/bin/env python3
import requests
from ignored import slack_url

headers = {"content-type": "application/json"}


def send_message(response):
    availability = response["appointmentsAvailable"]
    payload = {"text": f"Availability = {availability}"}
    response = requests.post(url=slack_url, headers=headers, json=payload)
