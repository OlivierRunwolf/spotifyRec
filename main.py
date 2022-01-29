from bottle import Bottle, run, static_file, request, template
import json
import requests, spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Bottle()
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
#Method to display webpages
@app.route('/<filename>')
def main(filename):
    return static_file(filename, root='view/main')

@app.route('/search',method='POST')
def searchUser():
    userId = request.forms.get('userID')
    output = spotify.user(userId)
    print(output)
    if 'error' not in output:
        print(output)
        return listArtistUser(output)
    elif output['error']['status'] == 400 :
        return "Error User Not found"

#@app.route('/callback')
def callback():
    print('response')
    return False

@app.route('/result')
@app.route('/result/search/<name>')
def listArtistUser(user):
    #
    #
    #
    #....
    return template('search', username=user['display_name'])

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

    #Access to
    artist_uri = 'spotify:artist:' + artist_id
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    #Gets the list of related artists
    results = spotify.artist_related_artists(artist_uri)
    rel_artists = results['artists']

    for rel_art in rel_artists:
        rel_art_URI = 'spotify:artist:' + rel_art['id']
        topTracksFile = spotify.artist_top_tracks(rel_art_URI)
        topTracks = topTracksFile['tracks']
        print(rel_art['name'])

run(app, host='localhost', port=8080,reloader=True)
