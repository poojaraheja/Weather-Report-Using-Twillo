import requests
from twilio.rest import Client


account_sid = "ACad8e7f8a4512c940797bf54ce75ee9ee"
auth_token = "717d2ded9c28661be5e1c7be0afb01bd"
parameters = {
    "lat": 27.167641,
    "lon": 78.035873,
    "appid": "3a40541489ad0159bec63d9c05438868",
    "exclude": "current,minutely,daliy"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
will_rain = True
for i in weather_slice:
    file = i["weather"][0]["id"]
    if int(file) >= 700:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Take Your Umbrella",
        from_="+19126003169",
        to="+919997214857"
    )
