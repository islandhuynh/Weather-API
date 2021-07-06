import requests
from api_keys import api_key

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
  "lat": 75.1638,
  "lon": 39.9523,
  "appid": api_key,
  "exclude": "currently,minutely,daily"
}

response = requests.api.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
hourly_forecast = response.json()["hourly"][0:11]
weather_conditions = [forecast["weather"][0]["id"] for forecast in hourly_forecast]
rain = False
for weather_id in weather_conditions:
  if weather_id < 700:
    rain = True
if rain:
  print("bring an umbrella")
print(weather_conditions)