

# **** represents YOUR own personally assigned keys, code ... etc


import matplotlib.pyplot as plt
import requests
from twilio.rest import Client

account_sid = '****'
auth_token = '****'
client = Client(account_sid, auth_token)

params = {
    "lat": 43.65893903788291,
    "lon": -79.71759594593912,
    "appid": "****",
    "units": "metric"
}
res = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
res.raise_for_status()

icon = res.json()["weather"][0]["icon"]
imageURL = f"http://openweathermap.org/img/wn/{icon}.png"

messageBody = (
    f"{res.json()['weather'][0]['main']} : {res.json()['weather'][0]['description']}\n"
    f"Feels Like : {res.json()['main']['feels_like']}°C\n"
    f"{res.json()['main']['temp_min']}°C < {res.json()['main']['temp']}°C < {res.json()['main']['temp_max']}°C\n"
)

message = client.messages.create(
    body=messageBody,
    from_='****',
    to='****'
)

print(message.status)
