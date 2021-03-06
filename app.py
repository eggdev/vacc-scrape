import logging
from calls import availability, send_slack_message


def main():
    response = availability.run()
    is_available = response["appointmentsAvailable"]

    if is_available:
        send_slack_message.send_message(response)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()