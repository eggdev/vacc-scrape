import logging
from calls import availability, send_slack_message


def main():
    response = availability.run()
    print(response)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()