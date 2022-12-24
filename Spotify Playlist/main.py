import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

PAGE_URL = "https://www.billboard.com/charts/hot-100/"
SCOPE = "playlist-modify-private"
REDIRECT_URL = "http://localhost:8888/callback"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(PAGE_URL + date)
# print(response.encoding) #UTF-8
soup = BeautifulSoup(response.text, "html.parser")
music_title = soup.find_all(name="h3",
                            id="title-of-a-story",
                            class_="a-no-trucate")
song_names = [music.getText().strip("\n\t") for music in music_title]

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE,
                                               redirect_uri=REDIRECT_URL,
                                               client_id=config.SPOTIFY_ID,
                                               client_secret=config.SPOTIFY_SECRET,
                                               cache_path="token.txt"))
user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100",
                                   public=False)
print(playlist)

