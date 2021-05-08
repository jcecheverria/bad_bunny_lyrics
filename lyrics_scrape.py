import os
import requests
from bs4 import  BeautifulSoup
from lyricsgenius import Genius
import unidecode
import re
import unicodedata
import pandas as pd

CLIENT_ACCESS_TOKEN = os.getenv('GENIUS_CLIENT_ACCESS_TOKEN')

##### ALBUMS

album_list = ['X_100pre', 'OASIS', 'YHLQMDLG',
              'LAS QUE NO IBAN A SALIR', 'EL ÚLTIMO TOUR DEL MUNDO']

lyrics_dict = {'artists': [],
               'album' : [],
               'title': [],
               'title_with_featured': [],
               'lyrics': [],
               'url': []
              }

genius = Genius(CLIENT_ACCESS_TOKEN,
				remove_section_headers = False)

# Retrieving songs for artist's albums
for album_name in album_list:
    album_data = genius.search_album(album_name, "Bad Bunny")
    track_list = album_data.tracks
    for track in track_list:
        lyrics_dict['artists'].append(track.song.artist)
        lyrics_dict['album'].append(album_name)
        lyrics_dict['title'].append(track.song.title)
        lyrics_dict['title_with_featured'].append(track.song.title_with_featured)
        lyrics_dict['lyrics'].append(track.song.lyrics)
        lyrics_dict['url'].append(track.song.url)


##### SINGLES OR OTHERS
r = requests.get("https://en.wikipedia.org/wiki/Bad_Bunny_discography")
soup = BeautifulSoup(r.text, 'html.parser')
singles_table = soup.find_all('table', {'class':'wikitable plainrowheaders'})[3]
songs_table = singles_table.find_all('th', {'scope':'row'})
pattern_singles = re.compile(r'\"([\w\s\?\¿\(\)]*)\"')

for song_row in songs_table:
	normalized_str = unicodedata.normalize('NFC', song_row.text.strip())
	single_name = pattern_singles.match(normalized_str).groups()[0]

	single_song = genius.search_song(single_name, 'Bad Bunny')
	
	single_title = single_song.title
	if single_title not in lyrics_dict['title']:
		lyrics_dict['artists'].append(single_song.artist)
		lyrics_dict['album'].append('Single')
		lyrics_dict['title'].append(single_title)
		lyrics_dict['title_with_featured'].append(single_song.title_with_featured)
		lyrics_dict['lyrics'].append(single_song.lyrics)
		lyrics_dict['url'].append(single_song.url)

