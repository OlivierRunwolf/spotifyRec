import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# results = spotify.user('Olivier')
# print(results)
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
#
# for album in albums:
#     print(album['name'])
results = spotify.artist_related_artists(birdy_uri)
rel_artists = results['artists']
# while results['next']:
#     results = spotify.next(results)
#     rel_artists.extend(results['artists'])

for rel_art in rel_artists:
    #top track file for each artists
    rel_art_URI = 'spotify:artist:' + rel_art['id']
    topTracksFile = spotify.artist_top_tracks(rel_art_URI)
    topTracks = topTracksFile['tracks']

    print(rel_art['name'])
    sizeTopTracks = len(topTracks)
    # track1Number = random.randint(0,sizeTopTracks-2)
    # track2Number = random.randint(0,sizeTopTracks-2)
    # track3Number = random.randint(0,sizeTopTracks-2)
    # print(topTracks[track1Number]['name'], ",", topTracks[track2Number]['name'], ",", topTracks[track3Number]['name'], "\n")
    randomTracks = random.sample(range(0,sizeTopTracks),3)
    print(topTracks[randomTracks[0]]['name'], ";", topTracks[randomTracks[1]]['name'], ";", topTracks[randomTracks[2]]['name'],"\n")

