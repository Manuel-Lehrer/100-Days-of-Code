import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Create a .env file and add your personal info there
account_sid = os.getenv('ACCOUNT_SID')       # from twilio account
auth_token = os.getenv('AUTH_TOKEN')         # for twilio
api_key = os.getenv('API_KEY')               # for openweathermap
phone_number = os.getenv('PHONE_NUMBER')
twilio_number = os.getenv('TWILIO_NUMBER')
MY_LAT = float(os.getenv('MY_LAT'))          # Latitude of your location
MY_LON = float(os.getenv('MY_LON'))          # Longitude of your location


parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(" https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()

next_12_hours = []

for sections in weather_data["list"]:
    weather_id = int(sections["weather"][0]["id"])
    next_12_hours.append(weather_id)


def check_for_rain():
    for ids in next_12_hours:
        if ids < 700:
            return True


if check_for_rain():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=twilio_number,
        body="It's going to rain today, Remember to bring an Umbrella ☂️",
        to=phone_number,
    )

    print(message.status)
