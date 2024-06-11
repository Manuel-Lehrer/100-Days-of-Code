import requests
from datetime import datetime
import os


calories_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# add a .env file and configure these values
APP_ID = os.environ["ENV_NIX_API_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]

SHEETY_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]
MY_TOKEN = os.environ["ENV_SHEETY_TOKEN"]


exercise = input("What exercise did you do?")

parameters = {
    "query": exercise,
    "gender": "",  # add your gender as a string (male/female)
    "weight_kg": 0,  # add your weight as an int in kg
    "height_cm": 0,  # add your height as an int in cm
    "age": 0,  # add your age as an int in years
    }

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
  }


response = requests.post(url=calories_endpoint, json=parameters, headers=headers)

outcome = response.json()

print(outcome)

today = datetime.now()

exercise = outcome["exercises"][0]["user_input"]
duration = outcome["exercises"][0]["duration_min"]
calories = outcome["exercises"][0]["nf_calories"]

for exercises in outcome["exercises"]:
    parameters_row = {
      "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%X"),
        "exercise": exercise.capitalize(),
        "duration": duration,
        "calories": calories,
        }
    }

    headers = {
        "Authorization": f"Bearer {MY_TOKEN}"
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=parameters_row, headers=headers)

    print(response.text)
