import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_id = '1c9f1311b702482d8f7e1e792a29e7c3'
client_secret = 'f918f7b7e0104b0dbb4c1b3a71c7226f'


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
