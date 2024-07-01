import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id='869b753e778c48499db962d926a99f6a',
        redirect_uri='https://github.com/TimatoPaste/Tim-and-Henry-Summer-2024',
        client_secret='289c9f563818444097d766d4572c5b4b',
        scope=scope))

timPlaylist = sp.playlist(
    playlist_id='https://open.spotify.com/playlist/18JD8kcZaP48GhEecXzewK?si=9a20c135b3084683',
    additional_types='track')

timTracks = timPlaylist.pop('tracks')

timItems = timTracks.pop('items')
count = 0
timTrackIDList = []
for item in timItems:
    timTrackIDList.append(item['track']['id'])

for id in timTrackIDList:
    print(id)
    count+=1
print(count)