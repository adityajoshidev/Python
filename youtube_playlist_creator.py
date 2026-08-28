from ytmusicapi import YTMusic
import requests
from bs4 import BeautifulSoup

###### Fetching the url #########

date=input("What year you would like to travel to in YYYY-MM-DD format: ")
# date="2026-04-18"
url=f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
r=requests.get(url)
r.raise_for_status()

##### making soup ########

soup=BeautifulSoup(r.text,"html.parser")
songs=soup.find_all(name="h3",class_="chart-entry__title")

##### collecting songs and artists names #######

song_names=[song.text for song in songs]
artist_names=[song.text for song in soup.find_all(name="span", class_="chart-entry__artist")]

###### making the playlist ########

ytmusic = YTMusic("browser.json")
playlists=ytmusic.get_library_playlists()
name=f"{date} BillBoard 100"
flag=1
for playlist in playlists:
    if playlist["title"]==name:
        flag=0
        playlist_id=playlists[playlists.index(playlist)]["playlistId"]
        break
if flag:
    playlist_id=ytmusic.create_playlist(name,"")
else:
    print("Name already exists")


##### adding the songs ########

for i in range(len(songs)):
    search_result=ytmusic.search(str(song_names[i])+" "+artist_names[i],filter="songs")
    try:
        video_id=[search_result[0]["videoId"]]
        ytmusic.add_playlist_items(playlist_id,video_id)
        print(f"Added: {song_names[i]}")
    except Exception:
        print("Something went wrong")
