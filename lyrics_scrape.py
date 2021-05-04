from lyricsgenius import Genius
import unidecode
import pandas as pd
import os

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

# Retrieving songs for artist's albums
for album_name in album_list:
    album_data = Genius(CLIENT_ACCESS_TOKEN,
                            remove_section_headers = False) \
                    .search_album(album_name,"Bad Bunny")
    track_list = album_data.tracks
    for track in track_list:
        lyrics_dict['artists'].append(track.song.artist)
        lyrics_dict['album'].append(album_name)
        lyrics_dict['title'].append(track.song.title)
        lyrics_dict['title_with_featured'].append(track.song.title_with_featured)
        lyrics_dict['lyrics'].append(track.song.lyrics)
        lyrics_dict['url'].append(track.song.url)

##### SINGLES OR OTHERS

