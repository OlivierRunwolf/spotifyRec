import random

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
        auth="BQCFX4zO0OLGaty80iz8ubnEi__7rw9CDia8ihKMtKClDvvoLHIPIQJQjFv-jZT-_JVU9agxRskhJ8IEtBXHoS0Bbaim7wolX-Nv8St5xnElrd-6UvlTyp4GIrUpQTdhnSxC1YL-cskS3xTTHUPGtQFeGj-4UA3Rs-f39wjOBNdnJfTPTfTKhL7q78ZpiScgEGLRoKyb")
    print(sp.current_user())
    list_rec_tracks = generateListRecommendedTracks(sp)

    for track in list_rec_tracks:
        print(track['artists'])

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

@app.route('/result')
@app.route('/result/search/<name>')
def listArtistUser(user):
    top_artists = spotify.current_user_top_artists(limit=5, offset=0, time_range='medium_term')
    output = top_artists['items']
    top_artists_id = []
    for x in top_artists_id:
        top_artists_id.append(x['id'])
    return template('search', username=user['display_name'])

def generateListRecommendedTracks(spotify):
    listUserTopArtist = getTopArtists(spotify)
    #Gets a set of all the artists related to the top artists
    setRelatedArtists = getRelatedArtists(listUserTopArtist, spotify)

    #Filters the list of related artists by removing elements that are in the user's top artists
    listRelatedArtists = []
    for rel_art in setRelatedArtists:
        if rel_art not in listUserTopArtist:
            listRelatedArtists.append(rel_art)

    #Get tracks from the related artists
    list_tracks_rel_artists = getTracksFromArtists(listRelatedArtists, spotify)

    list_chosen_tracks = []
    size_tracks_rel_artists = len(list_tracks_rel_artists)
    #If the amount of tracks is less or equal to 50, then it returns the list as is
    if size_tracks_rel_artists <= 50:
        list_chosen_tracks = list_tracks_rel_artists
    #Otherwise, it chooses 50 different tracks from the big list of artists
    else:
        randomTracksIndices = random.sample(range(0, size_tracks_rel_artists), 50)
        for index in randomTracksIndices:
            list_chosen_tracks.append(list_tracks_rel_artists[index])
    return list_chosen_tracks

#Gets the top 50 artists from a user
def getTopArtists(spotify):
    #Get access to the user's top artists
    results = spotify.current_user_top_artists(limit=50, offset=0, time_range='medium_term')
    topArtists = results['items']
    #Generate list of top artists
    top_artists_id = []
    for x in top_artists_id:
        top_artists_id.append(x)
    return topArtists

#Getting a set of related artists
def getRelatedArtists(list_artists, spotify):
    #initialize set
    set_related_artists = []
    #For each artist, find the top 3 related artists
    for artist in list_artists:
        #Get access to an artist's related artists
        artist_URI = 'spotify:artist:' + artist['id']
        results = spotify.artist_related_artists(artist_URI)
        artistRelatedArtists = results['artists']

        #Chooses the top 3 related artists and insert them in this list
        set_related_artists.append(artistRelatedArtists[0])
        set_related_artists.append(artistRelatedArtists[1])
        set_related_artists.append(artistRelatedArtists[2])
    return set_related_artists

#Chooses 3 random tracks from each of the artist in the passed list
def getTracksFromArtists(list_artists, spotify):
    #initializing the list
    listTracks = []
    for artist in list_artists:
        #Get request to the artist's top tracks
        artist_URI = 'spotify:artist:' + artist['id']
        results = spotify.artist_top_tracks(artist_URI)
        artist_tracks = results['tracks']

        #Chooses three different tracks randomnly and put it in listTracks
        sizeTracks = len(artist_tracks)
        randomTracksIndices = random.sample(range(0, sizeTracks), 3)
        listTracks.append(artist_tracks[randomTracksIndices[0]])
        listTracks.append(artist_tracks[randomTracksIndices[1]])
        listTracks.append(artist_tracks[randomTracksIndices[2]])
    return listTracks


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
