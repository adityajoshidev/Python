import requests
from bs4 import BeautifulSoup
from pyautogui import write

URL="https://editorial.rottentomatoes.com/guide/best-movies-21st-century/"
# Write your code below this line 👇
r=requests.get(URL)
r.raise_for_status()
soup=BeautifulSoup(r.text,"html.parser")
movies=[movie.text for movie in soup.find_all(name="a",class_="meta-title")]
with open("movies.txt","w") as file:
    for i in range(len(movies)):
        file.write(f"{i+1}) {movies[i]}\n")
