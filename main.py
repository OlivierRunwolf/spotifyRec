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


def listArtistUser (userId):
    response = requests.get("http://api.open-notify.org/astros.json")
    return True

run(app, host='localhost', port=8080, reloader=True)