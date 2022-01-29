import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# results = spotify.user('Olivier')
# print(results)
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
results = spotify.artist_related_artists(birdy_uri)
rel_artists = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
