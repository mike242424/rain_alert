import requests

API_KEY = '4932f24f1c731cf205df232f38d2a95b'
OPEN_WEATHER_MAP_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
MY_LAT = 32.80129911828599
MY_LNG = -80.00241254232888

weather_parameters = {
    'lat': MY_LAT,
    'lon': MY_LNG,
    'appid': API_KEY,
    'cnt': 4
}

response = requests.get(f'{OPEN_WEATHER_MAP_ENDPOINT}', params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

umbrella = 'No umbrella needed'
for forecast in weather_data['list']:

    if int(forecast['weather'][0]['id']) < 700:
        umbrella = 'Need umbrella'
    else:
        continue

print(umbrella)
