from bottle import Bottle, run, static_file, request
import json
import requests

app = Bottle()
appTOKEN = "Bearer BQDHOpu3aJsb9XrUjVIkd58e6SYYx5ip5mSMSFrGVagG-AalLsu5bd7PF8h0oXlfWwhTgRY6ZFHodPsuQsbxUNLTLtcf2C-Z_W14RWcJfgR7ifmJBlvQqLGhDaO6Y7hKlz2YXpiCKD746IyqcNJZ8zNwwU9ZMlbcvX0"
#Method to display webpages
@app.route('/<filename>')
def main(filename):
    return static_file(filename, root='view/main')

@app.route('/search',method='POST')
def searchUser():
    userId = request.forms.get('userID')
    my_headers = {'Authorization': appTOKEN}
    response = requests.get("https://api.spotify.com/v1/users/%s"%userId,headers=my_headers)
    output = response.json()
    print(output)
    if 'error' not in output:
        return output
    elif output['error']['status'] == 400 :
        return "Error User Not found"

@app.route('/artists-user')
def listArtistUser (userId):
    query={'type':"artist", 'after':"246dkjvS1zLTtiykXe5h60", 'limit':50 }
    response = requests.get("http://api.open-notify.org/astros.json/me/following", params=query)
    print(response)

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

run(app, host='localhost', port=8080, reloader=True)