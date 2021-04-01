#!/usr/bin/env python3
import requests
from ignored import slack_url

headers = {"content-type": "application/json"}


def send_message():
    payload = {"text": f""}
    requests.post(url=slack_url, headers=headers, json=payload)
