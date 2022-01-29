from bottle import Bottle, run, static_file, request, template
import json
import requests

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

        return listArtistUser(userId)
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
    my_params = {'limit': 50, 'offset': 0, 'time-range': 'medium_term'}
    my_headers = {'Authorization': appTOKEN}
    response = requests.get('https://api.spotify.com/v1/me/top/artists', headers=my_headers, params=my_params)
    output = response.json()['items']
    for artist in output:
        print(artist['name'])
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

run(app, host='localhost', port=8080)
