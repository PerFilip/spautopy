import spotipy
from spotipy import util

username = "hedeeen"

def run():
    scope = "user-read-currently-playing"
    token = util.prompt_for_user_token(username=username, scope=scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        current_track = sp.current_user_playing_track().get("item")
        print(current_track.get("name"))

if __name__=="__main__":
    run()
