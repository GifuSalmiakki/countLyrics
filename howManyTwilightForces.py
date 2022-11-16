# Script for finding how ofter certain words are used in song lyrics of an artist
# Originally for how ofter the band Twilight Force sings "Twilight Force"
# Source of lyrics: AZlyrics.com

import requests
from bs4 import BeautifulSoup

# TODO: download the content locally to minimize the amount of requests

def get_artist():

    art_input = input("Enter the artist: ")
    artist = art_input.strip().lower().replace(" ", "")

    words_to_find = input("Enter the words to be found: ")

    return artist, words_to_find


def run_scraper(artist):

    URL = "https://www.azlyrics.com/{}/{}.html".format(artist[0], artist)
    page = requests.get(URL)
    # If the artist is not found, AZlyrics redirects to homepage automatically

    soup = BeautifulSoup(page.content, "html5lib")
    song_links = soup.findAll("div", {"class": "listalbum-item"})

    all_lyrics = []
    for song in song_links:
        links = song.findAll("a")
        for link in links:
            full_link = "https://www.azlyrics.com/{}".format(link.get("href"))
            song_page = requests.get(full_link)
            song_soup = BeautifulSoup(song_page.content, "html5lib")
            lyrics = song_soup.getText()
            all_lyrics.append(lyrics)

    print(all_lyrics[0])
    return all_lyrics


def count_lyric_frequency(all_lyrics, words_to_find, artist):

    count = 0
    for lyrics in all_lyrics:
        # placeholder
        count += 1

    print("The words '{}' are used {} times in songs from '{}'"
          .format(words_to_find, count, artist))



def main():

    artist, words_to_find = get_artist()

    all_lyrics = run_scraper(artist)

    count_lyric_frequency(all_lyrics, words_to_find, artist)


main()