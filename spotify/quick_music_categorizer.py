import yaml
import keyboard
import time

import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Step 1: Load credentials from the YAML file
def load_credentials():
    with open("credentials.yaml", "r") as file:
        credentials = yaml.safe_load(file)
    return credentials


def setup_spotify():
    credentials = load_credentials()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=credentials['client_id'],
                                                   client_secret=credentials['client_secret'],
                                                   redirect_uri="http://localhost:8888/callback",
                                                   scope="playlist-modify-private playlist-modify-public user-read-playback-state user-modify-playback-state"))
    return sp


# Step 3: Helper functions to handle playlist actions
def get_current_track(sp):
    playback = sp.current_playback()
    if playback and playback['is_playing']:
        track_id = playback['item']['id']
        return track_id
    return None


def add_to_playlist(sp, playlist_name, track_id):
    playlists = sp.current_user_playlists(limit=99)
    playlist_id = None
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            playlist_id = playlist['id']
            break

    if not playlist_id:
        print(f'Could not find {playlist_name}')
    else:
        sp.playlist_add_items(playlist_id=playlist_id, items=[track_id], position=None)
        print(f"Added track to playlist: {playlist_name}")


def handle_keypress(sp):
    while True:
        playback_info = sp.current_playback()

        if keyboard.is_pressed('n'):
            track_id = get_current_track(sp)
            if track_id:
                add_to_playlist(sp, "_nope", track_id)
            else:
                print('No available track!')
            time.sleep(1)

        elif keyboard.is_pressed('m'):
            track_id = get_current_track(sp)
            if track_id:
                add_to_playlist(sp, "_maybe", track_id)
            else:
                print('No available track!')
            time.sleep(1)

        elif keyboard.is_pressed('l'):
            track_id = get_current_track(sp)
            if track_id:
                add_to_playlist(sp, "_buffer", track_id)
                # add_to_playlist(sp, "Gaming", track_id)
                sp.current_user_saved_tracks_add([track_id])
                time.sleep(1)
            else:
                print('No available track!')
            time.sleep(1)

        elif keyboard.is_pressed('1'):
            track_id = get_current_track(sp)
            if track_id:
                add_to_playlist(sp, "First", track_id)
                time.sleep(0.05)
                add_to_playlist(sp, "_buffer", track_id)
                time.sleep(0.05)
                sp.current_user_saved_tracks_add([track_id])
                time.sleep(0.05)
            else:
                print('No available track!')
            time.sleep(1)

        elif keyboard.is_pressed('/'):
            track_id = get_current_track(sp)
            if track_id:
                add_to_playlist(sp, "Rap", track_id)
                add_to_playlist(sp, "_buffer", track_id)
                sp.current_user_saved_tracks_add([track_id])
            else:
                print('No available track!')
            time.sleep(1)

        elif keyboard.is_pressed('right'):
            if playback_info and playback_info['is_playing']:
                current_position = playback_info['progress_ms']
                new_position = current_position + 30000  # Go forward 30 sec
                sp.seek_track(new_position)

        elif keyboard.is_pressed('left'):
            if playback_info and playback_info['is_playing']:
                current_position = playback_info['progress_ms']
                new_position = max(0, current_position - 30000)  # Go back 30 sec
                sp.seek_track(new_position)

        elif keyboard.is_pressed('alt') and keyboard.is_pressed('p'):
            if playback_info['is_playing']:
                sp.pause_playback()
            else:
                sp.start_playback()

        elif keyboard.is_pressed('up'):
            sp.next_track()

        elif keyboard.is_pressed('down'):
            sp.previous_track()

        elif keyboard.is_pressed('x'):
            exit()


# Step 5: Run the event loop
if __name__ == "__main__":
    sp = setup_spotify()
    if sp:
        print("Press 'N', 'M', 'L', or 'X' on the keyboard to interact with Spotify.")
        handle_keypress(sp)
