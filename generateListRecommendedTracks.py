import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
def generateListRecommendedTracks(user_id):
    listUserTopArtist = getTopArtists()
    #Gets a set of all the artists related to the top artists
    setRelatedArtists = getRelatedArtists(listUserTopArtist)

    #Filters the list of related artists by removing elements that are in the user's top artists
    listRelatedArtists = []
    for rel_art in setRelatedArtists:
        if rel_art not in listUserTopArtist:
            listRelatedArtists.append(rel_art)

    #Get tracks from the related artists
    list_tracks_rel_artists = getTracksFromArtists(listRelatedArtists)

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

#Gets the top 50 artists from a user
def getTopArtists():
    #Get access to the user's top artists
    results = spotify.current_user_top_artists(limit=50, offset=0, time_range='medium_term')
    topArtists = results['items']
    #Generate list of top artists
    top_artists_id = []
    for x in top_artists_id:
        top_artists_id.append(x)
        #print(x['id'])
    return topArtists

#Getting a set of related artists
def getRelatedArtists(list_artists):
    #initialize set
    set_related_artists = {}
    #For each artist, find the top 3 related artists
    for artist in list_artists:
        #Get access to an artist's related artists
        artist_URI = 'spotify:artist:' + artist['id']
        results = spotify.artist_related_artists(artist_URI)
        artistRelatedArtists = results['artists']

        #Chooses the top 3 related artists and insert them in this list
        set_related_artists.add(artistRelatedArtists[0])
        set_related_artists.add(artistRelatedArtists[1])
        set_related_artists.add(artistRelatedArtists[2])
    return set_related_artists

#Chooses 3 random tracks from each of the artist in the passed list
def getTracksFromArtists(list_artists):
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

#For testing purposes
if __name__ == "__main__":
    getTopArtists()