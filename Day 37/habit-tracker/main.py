import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.getenv("USER_NAME")
TOKEN = os.getenv("TOKEN")

user_params = {
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?"),
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

print(response.text)


# update pixel below:

# today = datetime(year=2023, month=12, day=22)
#
# date = today.strftime("%Y%m%d")


# update_pixel_params = {
# "quantity": "3",
# }

# update_pixel_endpoint = f"{pixel_endpoint}/{date}"

# response = requests.put(url = update_pixel_endpoint, json=update_pixel_params, headers=headers)
#
# print(response.text)


# delete pixel below:

# response = requests.delete(url = update_pixel_endpoint, headers=headers)
#
# print(response.text)


# for creating a new user down below:

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# print(response.json())


# for configuring a new graph down below:

# graph_config = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "Hours",
#     "type": "float",
#     "color": "ajisai"
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
