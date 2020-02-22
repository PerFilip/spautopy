import spotipy
from spotipy import util

def run():
    scope="user-read-currently-playing"
    token = util.prompt_for_user_token(scope)
    print("token = " + token)

    if token:
        sp = spotipy.Spotify(auth=token)
        print("Token provided...")
        current_track = sp.current_user_playing_track()
        print(current_track)

if __name__=="__main__":
    run()
