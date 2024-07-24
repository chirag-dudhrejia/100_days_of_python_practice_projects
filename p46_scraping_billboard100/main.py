import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_APP_CLIENT_ID = "8c22d733ca1b41df813fb9ca04c9669a"
SPOTIFY_APP_CLIENT_SECRET = "b14e14c5998d44f39e3af7ed292146c0"
REDIRECT_URI = "http://example.com"

input_date = input("Which year do you want to travel? Type the date in format YYYY-MM-D : ")

billboard_response = requests.get(url=f"{BILLBOARD_URL}{input_date}/")
soup = BeautifulSoup(markup=billboard_response.text, features="html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_="lrv-u-font-size-16")

songs_list = [song.string.strip() for song in songs]

print(songs_list)