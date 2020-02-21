import spotipy
from spotipy import util
from me import Me
from spotipy.oauth2 import SpotifyClientCredentials

def run():
    scope="user-read-currently-playing"
    user_id, user_secret, user_uri = Me.get_user_credentials()
    token = util.prompt_for_user_token(scope, user_id, user_secret, user_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        current_track = sp.current_user_playing_track()
        print(current_track)

    

if __name__=="__main__":
    run()
