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

def listArtistUser (STring userId):
    response = requests.get("http://api.open-notify.org/astros.json")


run(app, host='localhost', port=8080)