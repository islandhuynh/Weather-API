import requests
from api_keys import api_key

lat = 75.1638
lon = 39.9523

response = requests.api.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exlucde=current,minutely,daily,alerts&appid={api_key}").json()
print(response)