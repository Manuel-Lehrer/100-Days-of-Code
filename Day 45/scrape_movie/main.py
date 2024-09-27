from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https:"
                        "//www.empireonline.com/movies/features/best-movies-2/")

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

all_movies = soup.find_all(class_="article-title-description__text")


all_titles = [movies.find(name="h3").getText() for movies in all_movies]
movies = all_titles[::-1]
print(movies)
with open("movies.txt", "w", encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")
