import requests
from bs4 import BeautifulSoup

EMPIRES_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

empires = requests.get(url=EMPIRES_URL)
soup = BeautifulSoup(markup=empires.text, features="html.parser")

titles_list = soup.find_all(name="h3", class_="title")

movies = [titles.string for titles in titles_list]
movies.reverse()

with open(file="movies.txt", mode="a", encoding="utf-8") as writefile:
    for movie in movies:
        writefile.write(f"{movie}\n")