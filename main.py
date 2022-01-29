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
    try:
        print(output)
        return listArtistUser(output)
    except requests.exceptions.HTTPError:
        return "HTTP ERROR"

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
def listrelatedArtists():
    my_headers = {'Authorization': 'BQDHOpu3aJsb9XrUjVIkd58e6SYYx5ip5mSMSFrGVagG-AalLsu5bd7PF8h0oXlfWwhTgRY6ZFHodPsuQsbxUNLTLtcf2C-Z_W14RWcJfgR7ifmJBlvQqLGhDaO6Y7hKlz2YXpiCKD746IyqcNJZ8zNwwU9ZMlbcvX0'}
    response = requests.get("https://api.spotify.com/v1/artists/id/related-artists",headers=my_headers)
    output = response.json()
    print(response)
    print(output)
    if 'error' not in output:
        return output
    elif output['error']['status'] == 400 :
        return "Error No related artists found found"

run(app, host='localhost', port=8080,reloader=True)
