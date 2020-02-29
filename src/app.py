import spotipy, sys
from spotipy import util

username = "hedeeen"
playlist = "4x98GQp3hWLtX4MEAtXWhB" # playlist id

def main():
    scope = "user-read-currently-playing playlist-modify-private playlist-modify-public playlist-read-private playlist-read-collaborative user-library-read"
    token = util.prompt_for_user_token(username=username, scope=scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        if len(sys.argv)<=1:
            return 0
        if sys.argv[1]=="-add":
            add_current_track(sp)
        elif sys.argv[1]=="-clean":
            limbo_liked = find_liked_in_limbo(sp)
            remove_from_limbo(sp, limbo_liked)

        else:
	        print("\""+sys.argv[1] + "\" is not a valid option.\n" + "Try one of these instead: -add -clean")
        
# Adds currently playing track to Limbo (my choosen playlist)
def add_current_track(sp):
    current_track_data = sp.current_user_playing_track()
    if current_track_data==None:
        print("No currently playing track.")
        return
    current_track = current_track_data.get("item")
    track_id = current_track.get("id")
    sp.user_playlist_add_tracks(username, playlist_id=playlist, tracks=[track_id])
    print("Added \"" + current_track.get("name") + "\" to Limbo.")

def remove_from_limbo(sp, tracks):
    sp.user_playlist_remove_all_occurrences_of_tracks(user=username, playlist_id=playlist, tracks=tracks)
    print("Liked tracks removed from Limbo.")

def find_liked_in_limbo(sp):
    limbo_liked_tracks = []
    limbo = sp.playlist_tracks(playlist_id=playlist).get("items")
    recent_likes = add_all_liked_tracks(sp)
    for track in limbo:
        limbo_track_id = track.get("track").get("id")
        for liked_track in recent_likes:
            if (liked_track.get("track").get("id")==limbo_track_id):
                limbo_liked_tracks.append(limbo_track_id)
    return limbo_liked_tracks

def add_all_liked_tracks(sp):
    recent_likes = []
    liked_tracks = sp.current_user_saved_tracks(limit=20).get("items")
    for i in range(5):
        for track in liked_tracks:
            recent_likes.append(track)
        liked_tracks = sp.current_user_saved_tracks(limit=20, offset=20*i).get("items")
    return recent_likes
        
def add_to_next_month_playlist(sp):
    current_track = sp.current_user_playing_track().get("item")



if __name__=="__main__":
    main()
