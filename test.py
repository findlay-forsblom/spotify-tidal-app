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

tidalPlaylist = 'Findlays Playlist'


def getArtists(artists):
    names = ''
    for artist in artists:
        names += artist['name'] +';'

    return names

def getPlaylist(playlists):
    for item in playlists:
        if item.name == tidalPlaylist:
            return item
    return None

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

import tidalapi

session = tidalapi.Session()


session.user.id
favourites = tidalapi.Favorites(session, session.user.id)
lol3 = session.search('track', 'Mad Love')


lol2 = favourites.playlists()

user = tidalapi.User(session, session.user.id)
playlists = user.playlists()
playlist = getPlaylist(lol2)

playlist.add_track()
if playlist:
    pass
else:
    print('Playlist not found pls check spelling')







favourites.add_track(126462760)
lol = tidalapi.models.Playlist()
lol.id = 'kkjn'
lol.add_track(126462760)
hej = tidalapi

tidalTracks = session.get_playlist_items('1e79e17b-e54c-498e-97e0-a4a27846207e')
for track in tidalTracks:
    print(track)
