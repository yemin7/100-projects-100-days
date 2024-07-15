import requests
from twilio.rest import Client

LATITUDE = 13.756331
LONGITUDE = 100.501762

account_sid = ''
auth_token = ''
from_ph = ''
to_ph = ''
body_message = "It's going to rain today. Remember to bring an ☔️"
api_key = ""
will_rain = False

weather_parameters = {
    "q": "Bangkok,TH",
    "appid": api_key,
}

forecast_5_parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "cnt": 4,
}


def get_url(url, params):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    if response.status_code == 200:
        return response.json()
    else:
        return None


def send_sms():
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=from_ph, to=to_ph, body=body_message)
    print(message.sid)
    print(message.status)

    # weather_data = get_url(url="https://api.openweathermap.org/data/2.5/weather", params=weather_parameters)


# print(weather_data['weather'][0]['id'])
# print(weather_data['weather'][0]['description'])

forecast_data = get_url(url="https://api.openweathermap.org/data/2.5/forecast", params=forecast_5_parameters)

if forecast_data is not None:
    data = forecast_data['list']

    for weather in data:
        # print(weather['weather'][0]['id'])
        # print(weather['weather'][0]['description'])
        if weather['weather'][0]['id'] < 700:
            will_rain = True

    if will_rain:
        send_sms()
