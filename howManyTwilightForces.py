# Script for finding how ofter certain words are used in song lyrics of an artist
# Originally for how ofter the band Twilight Force sings "Twilight Force"
# Source of lyrics: AZlyrics.com

import requests
from bs4 import BeautifulSoup

print("Enter the artist: ")
input = "twilightforce"
artist = input.strip().lower().replace(" ", "")

URL = "https://www.azlyrics.com/{}/{}.html".format(artist[0], artist)
page = requests.get(URL)
# If the artist is not found, AZlyrics redirects to homepage automatically

soup = BeautifulSoup(page.content, "html5lib")
songLinks = soup.findAll("div", {"class": "listalbum-item"})

allLyrics = []
for song in songLinks:
    links = song.findAll("a")
    for link in links:
        fullLink = "https://www.azlyrics.com/{}".format(link.get("href"))
        songPage = requests.get(fullLink)
        songSoup = BeautifulSoup(page.content, "html5lib")
        lyrics = songSoup.getText()
        allLyrics.append(lyrics)

print(allLyrics[0])

print("Enter the words to be found: ")
wordsToFind = "Twilight Force"
count = 0
for lyrics in allLyrics:
    # placeholder
    count += 1

print("The words '{}' are used {} times in songs from '{}'"
      .format(wordsToFind, count, artist))









