import requests
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]

MY_TOKEN = os.environ["ENV_SHEETY_TOKEN"]

CUSTOMERS_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]

HEADERS = {
            "Authorization": f"Bearer {MY_TOKEN}"
        }


class DataManager:
    # This class is responsible for talking to the Google sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=SHEETY_ENDPOINT, headers=HEADERS)

        data = response.json()

        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city["id"]}", json=new_data, headers=HEADERS)
            print(response.text)

    # Emails and names have been collected through a replit application and inserted in the Google sheet.
    def get_emails(self):
        response = requests.get(url=CUSTOMERS_ENDPOINT, headers=HEADERS)

        data = response.json()["users"]
        emails = [rows["email"]for rows in data]
        return emails
