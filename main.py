import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
MY_LAT = float(os.getenv('MY_LAT'))
MY_LNG = float(os.getenv('MY_LNG'))
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
RECIPIENT_PHONE_NUMBER = os.getenv('RECIPIENT_PHONE_NUMBER')

weather_parameters = {
    'lat': MY_LAT,
    'lon': MY_LNG,
    'appid': API_KEY,
    'cnt': 4
}

OPEN_WEATHER_MAP_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'

response = requests.get(f'{OPEN_WEATHER_MAP_ENDPOINT}', params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for forecast in weather_data['list']:
    if int(forecast['weather'][0]['id']) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="Bring an umbrella.",
        from_=TWILIO_PHONE_NUMBER,
        to=RECIPIENT_PHONE_NUMBER,
    )
else:
    print("You won't need an umbrella.")

