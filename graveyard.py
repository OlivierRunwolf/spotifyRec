from bottle import Bottle, run, static_file, request, template, response
import json
import requests, spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import Spotify, SpotifyOAuth, oauth2

app = Bottle()

PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = '3441111ba643438aa09f7aa0d8680561'
SPOTIPY_CLIENT_SECRET = '80967271ad8b4fc19f8e6274bd93eb2e'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080/callback'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE,
                               cache_path=CACHE)

@app.route('/')
def index():
    access_token = ""
    token_info = sp_oauth.get_cached_token()

    if token_info:
        print("Found cached token!")
        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)
        if code != url:
            print("Found Spotify auth code in Request URL! Trying to get valid access token...")
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print("Access token available! Trying to get user information...")
        sp = spotipy.Spotify(access_token)
        results = sp.current_user()
        return results

    else:
        return htmlForLoginButton()


def htmlForLoginButton():
    auth_url = getSPOauthURI()
    htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    return htmlLoginButton


def getSPOauthURI():
    auth_url = sp_oauth.get_authorize_url()
    return auth_url