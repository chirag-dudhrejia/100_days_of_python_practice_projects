import requests
import smtplib

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "a727730b3858fdf65401161368d5d318"
MY_EMAIL = "dchirag5050@gmail.com"
APP_PASSWORD = "uldahsssgfnsptkw"

weather_params = {
    "lat": "21.588081",
    "lon": "71.223859",
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_response = response.json()

will_rain = False
for hour_data in weather_response["list"]:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="dchirag159@gmail.com",
                            msg=f"Subject:Rainy today!\n\nIt will rain today take umbrella.")