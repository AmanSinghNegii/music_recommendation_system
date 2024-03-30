import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_id = 'id'
client_secret = 'secretkey'


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
def fetch_spotify_recommendations(song_name):
    results = sp.search(q='track:' + song_name, limit=1)
    if len(results['tracks']['items']) == 0:
        return "Song not found in Spotify. Please try another song."
    
    track_id = results['tracks']['items'][0]['id']
    recommendations = sp.recommendations(seed_tracks=[track_id], limit=5)
    return [track['name'] for track in recommendations['tracks']]
user_input = input("Enter a song name: ")
spotify_recommendations = fetch_spotify_recommendations(user_input)

if isinstance(spotify_recommendations, str):
    print(spotify_recommendations)
else:
    print("Songs similar to", user_input, ":", spotify_recommendations)
