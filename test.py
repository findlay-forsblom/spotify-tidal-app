import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import env_file
import os
import requests
import sys
import json
env_file.load('.env')


CLIENT_ID = os.getenv("client_id")
CLIENT_SECRET = os.getenv("client_secret")
USERNAME_TIDAL = os.getenv("username")
auth=''




sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

birdy_uri = 'spotify:playlist:5gvBKYg6mlKs5dWnlOwr2i'
#sp.playlist_items()
results = sp.playlist_items(birdy_uri)
tracks = results['items']
trackList = []

tidalPlaylistName = 'Findlays Playlist'


def getArtists(artists):
    names = ''
    for artist in artists:
        names += artist['name'].lower() +';'

    return names

def getPlaylist(playlists, desiredPlaylst):
    for item in playlists:
        if item.name == desiredPlaylst:
            return item
    return None

def addSongToPlaylist(url, data, headers):
    while(True):
        p = requests.post(url=url, headers=headers, data=data)
        responseHeaders = p.headers
        if p.status_code == 200:
            ETAG = responseHeaders['ETag']
            headers = {'Authorization': auth, 'If-None-Match': ETAG}



def getTidalSongs(trackList, session):
    notFound = []
    notAvailable = []
    foundTracks = []

    for spotifyTrack in trackList:
        found = False
        songs = []
        value = spotifyTrack['name']
        spotifyArt = spotifyTrack['artists'].split(';')[:-1]
        searchResults = session.search('track', value, 10).tracks
        if len(searchResults) == 0:
            notFound.append({'name': spotifyTrack['name'], 'artist': spotifyTrack['artists'], 'errorCode': 1,
                             'errorMsg': 'Not found because trackname gave 0 results'})
            continue
        for tidalTrack in searchResults:
            tidalArt = tidalTrack.artist.name.lower()
            if tidalArt in spotifyArt:
                found = True
                if tidalTrack.available:
                    songs.append(tidalTrack)
                else:
                    notAvailable.append(tidalTrack)
        if found:
            foundTracks.append({'name': spotifyTrack['name'], 'artist': spotifyTrack['artists'], 'tracks': songs})
        else:
            notFound.append({'name': spotifyTrack['name'], 'artist': spotifyTrack['artists'], 'errorCode': 0,
                             'errorMsg': 'Not found because of non matching artist names', 'tracks': searchResults})
            # if tidalArt ==
            #     print(tidalArt)
     return foundTracks, notFound, notAvailable

while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])


for track in tracks:
    # print(track['track']['name'])
    # print(track['track']['id'])
    artists = getArtists(track['track']['artists'])
    #print(artists)
    # print(track['track'])
    trackList.append({'id': track['track']['id'], 'name': track['track']['name'], 'artists': artists })

print(trackList)
print(len(trackList))

import tidalapi

url = ''
session = tidalapi.Session()
session.login(USERNAME_TIDAL, os.getenv("password"))

foundTracks, notFound, notAvailable = getTidalSongs(trackList, session)
favourites = tidalapi.Favorites(session, session.user.id)
allPlaylists = favourites.playlists()
playlist = getPlaylist(allPlaylists, tidalPlaylistName)

if playlist:
    url = 'https://listen.tidal.com/v1/playlists/{playlistID}?countryCode=SE'.format(playlistID=playlist.id)
else:
    sys.exit("Playlist not found pls check spelling, stopping execution")

headers = {'Authorization': auth}
r = requests.get(url = url, headers=headers)

if r.status_code == 200:
    responseHeaders = r.headers
    ETAG = responseHeaders['ETag']
    url = 'https://listen.tidal.com/v1/playlists/{playlistID}/items?countryCode=SE'.format(playlistID=playlist.id)
    data = {'onArtifactNotFound': 'FAIL', 'onDupes': 'FAIL', 'trackIds': 97874144}
    headers = {'Authorization': auth,  'If-None-Match': ETAG}

    addSongToPlaylist()


    p = requests.post(url=url, headers= headers,  data = data)
    responseHeaders = p.headers
    ETAG = responseHeaders['ETag']

else :
    sys.exit(json.loads(r.content)['userMessage'])



# for spotifyTrack in trackList:
#     found = False
#     songs = []
#     value = spotifyTrack['name']
#     spotifyArt = spotifyTrack['artists'].split(';')[:-1]
#     searchResults = session.search('track', value, 10).tracks
#     if len(searchResults) == 0:
#         notFound.append({'name': spotifyTrack['name'], 'artist': spotifyTrack['artists'], 'errorCode': 1, 'errorMsg':'Not found because trackname gave 0 results'})
#         continue
#     for tidalTrack in searchResults:
#         tidalArt = tidalTrack.artist.name.lower()
#         if tidalArt in spotifyArt:
#             found = True
#             if tidalTrack.available:
#                 songs.append(tidalTrack)
#             else:
#                 notAvailable.append(tidalTrack)
#     if found:
#         foundTracks.append({'name': spotifyTrack['name'], 'artist': spotifyTrack['artists'], 'tracks': songs})
#     else:
#         notFound.append({'name': spotifyTrack['name'], 'artist': spotifyTrack['artists'], 'errorCode':0, 'errorMsg':'Not found because of non matching artist names', 'tracks': searchResults })
        # if tidalArt ==
        #     print(tidalArt)



len(foundTracks)
len(notFound)
len(notAvailable)







searchResults = session.search('track', 'Mad Love').tracks


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
