import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import env_file
import os
env_file.load('.env')


CLIENT_ID = os.getenv("client_id")
CLIENT_SECRET = os.getenv("client_secret")



sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

birdy_uri = 'spotify:playlist:5gvBKYg6mlKs5dWnlOwr2i'
#sp.playlist_items()
results = sp.playlist_items(birdy_uri)
tracks = results['items']
trackList = []


def getArtists(artists):
    names = ''
    for artist in artists:
        names += artist['name'] +';'

    return names

while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])


for track in tracks:
    # print(track['track']['name'])
    # print(track['track']['id'])
    artists = getArtists(track['track']['artists'])
    # print(artists)
    # print(track['track'])
    trackList.append({'id': track['track']['id'], 'name': track['track']['name'], 'artists': artists })

print(trackList)
print(len(trackList))