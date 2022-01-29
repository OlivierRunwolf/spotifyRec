from bottle import Bottle, run
import requests

app = Bottle()

@app.route('/spotify')
def hello():

    print("....")


    return "Hello SPOTI!!!!"



def hello2():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response)
    return "false"


def listrelatedArtists():
    my_headers = {'Authorization': 'BQDHOpu3aJsb9XrUjVIkd58e6SYYx5ip5mSMSFrGVagG-AalLsu5bd7PF8h0oXlfWwhTgRY6ZFHodPsuQsbxUNLTLtcf2C-Z_W14RWcJfgR7ifmJBlvQqLGhDaO6Y7hKlz2YXpiCKD746IyqcNJZ8zNwwU9ZMlbcvX0'}
    response = requests.get("https://api.spotify.com/v1/artists/id/related-artists",headers=my_headers)
    output = response.json()
    print(response)
    print(output)
    return "false"

run(app, host='localhost', port=8080)