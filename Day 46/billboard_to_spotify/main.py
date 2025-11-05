from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

ID = os.environ["ID"]
SECRET = os.environ["SECRET"]
USERNAME = os.environ["USERNAME"]

#Scraping Billboard 100
date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD:")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
all_titles = soup.select("li ul li h3")
titles = [title.getText().strip() for title in all_titles]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://www.example.com",
        client_id=ID,
        client_secret=SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    )
)

user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
