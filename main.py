from bottle import Bottle, run, static_file
import requests

app = Bottle()

@app.route('/spotify')
def hello():
    print("....")
    return "Hello dsada!!!!"


@app.route('/<filename>')
def main(filename):
    return static_file(filename, root='view/main')


def hello2():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response)
    # update -> commit -> push
    return "false"

def listArtistUser (userId):
    response = requests.get("http://api.open-notify.org/astros.json")
    return True

run(app, host='localhost', port=8080, reloader=True)