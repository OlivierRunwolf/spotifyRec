from gevent import monkey;
import random

monkey.patch_all()
from bottle import Bottle, run, static_file, request, template, response
import json
import requests, spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import Spotify, SpotifyOAuth, oauth2

app = Bottle()

SPOTIPY_CLIENT_ID = '3441111ba643438aa09f7aa0d8680561'
SPOTIPY_CLIENT_SECRET = '80967271ad8b4fc19f8e6274bd93eb2e'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


# Method to display webpages
@app.route('/<filename>')
def main(filename):
    return static_file(filename, root='view/main')


@app.route('/spot')
def login():
    #   print(request.query['code'])
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id="3441111ba643438aa09f7aa0d8680561",
            client_secret="80967271ad8b4fc19f8e6274bd93eb2e",
            redirect_uri="http://localhost:8888/callback",
            scope="user-library-read"
        )
    )
    # sp = spotipy.Spotify(auth=str(request.query['code']))
    results = sp.current_user()
    print(results)


@app.route('/callback')
def callback():
    # print(request.query['code'])
    sp = spotipy.Spotify(
        auth="BQB8RKRLGERXt5JGLqP8obvIeB-aFYUHBDvMLz9FbjodwSXcz8DO7rRrM_rnS8mjByfHI4nlksGuTzm3-msEGnXyzXo5zrwtMeXShAbxBXG54QHVxueW44kr0ITNtSD4rQfQ1QYkRxrwQeDPy_rpDkZj7evuAL6ea6hYc-1K1pG0")
    print(sp.current_user())
    return "phey"


@app.route('/search', method='POST')
def searchUser():
    userId = request.forms.get('userID')

    try:
        output = spotify.user(userId)
        print(output)
        return listArtistUser(output)
    except:
        output = {'display_name': ''}
        return listArtistUser(output)


# @app.route('/callback')
def callback():
    print('response')
    return False


@app.route('/result')
@app.route('/result/search/<name>')
def listArtistUser(user):
    top_artists = spotify.current_user_top_artists(limit=5, offset=0, time_range='medium_term')
    output = top_artists['items']
    top_artists_id = []
    for x in top_artists_id:
        top_artists_id.append(x['id'])
    return template('search', username=user['display_name'])


def generateListRecommendedTracks():
    recommendedTracks = [1]

    return recommendedTracks


#
def listUnlistenedTracksFromUserTopArtists(user_id):
    return False

# def listTracksFromRelatedArtists(artist_id):
#     return False


@app.route('/related-artists')
def listrelatedArtists(artist_id):
    # my_headers = {'Authorization': 'BQDHOpu3aJsb9XrUjVIkd58e6SYYx5ip5mSMSFrGVagG-AalLsu5bd7PF8h0oXlfWwhTgRY6ZFHodPsuQsbxUNLTLtcf2C-Z_W14RWcJfgR7ifmJBlvQqLGhDaO6Y7hKlz2YXpiCKD746IyqcNJZ8zNwwU9ZMlbcvX0'}
    # response = requests.get("https://api.spotify.com/v1/artists/id/related-artists",headers=my_headers)
    # output = response.json()
    # print(response)
    # print(output)
    # if 'error' not in output:
    #     return output
    # elif output['error']['status'] == 400 :
    #     return "Error No related artists found found"

    # Access to
    artist_uri = 'spotify:artist:' + artist_id
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    # Gets the list of related artists
    results = spotify.artist_related_artists(artist_uri)
    rel_artists = results['artists']

    for rel_art in rel_artists:
        # top track file for each artists
        rel_art_URI = 'spotify:artist:' + rel_art['id']
        topTracksFile = spotify.artist_top_tracks(rel_art_URI)
        topTracks = topTracksFile['tracks']

        print(rel_art['name'])
        sizeTopTracks = len(topTracks)
        # track1Number = random.randint(0,sizeTopTracks-2)
        # track2Number = random.randint(0,sizeTopTracks-2)
        # track3Number = random.randint(0,sizeTopTracks-2)
        # print(topTracks[track1Number]['name'], ",", topTracks[track2Number]['name'], ",", topTracks[track3Number]['name'], "\n")
        randomTracks = random.sample(range(0, sizeTopTracks), 3)
        print(topTracks[randomTracks[0]]['name'], ";", topTracks[randomTracks[1]]['name'], ";",
              topTracks[randomTracks[2]]['name'], "\n")


run(app, host='localhost', port=8080, reloader=True)
