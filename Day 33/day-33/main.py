import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# # if response.status_code != 200:
# #     raise Exception("Bad response from ISS API")
# # else:
# #     print(response.json())
# # Now instead of this to raise/include all exceptions
# response.raise_for_status()
#
# data = response.json()["iss_position"]
#
# latitude = data["latitude"]
# longitude = data["longitude"]
#
# iss_position = (latitude, longitude)
#
# print(iss_position)

parameters = {
        "lat": 1.3733,
        "lng": 32.2903,
        "formatted": 0
              }

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


time_now = datetime.now().hour

print(sunrise)
print(time_now)
