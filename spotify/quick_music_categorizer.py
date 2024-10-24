import yaml
import keyboard
import time
import requests
import logging
logging.basicConfig(level=logging.DEBUG)

import spotipy
from spotipy.oauth2 import SpotifyOAuth


sleep_seconds = 0.3


# Step 1: Load credentials from the YAML file
def load_credentials():
    with open("credentials.yaml", "r") as file:
        credentials = yaml.safe_load(file)
    return credentials


def waiting():
    print(f"Waiting for {sleep_seconds} seconds to prevent to many requests!")
    time.sleep(sleep_seconds)


def validate_connection(sp, auth_manager):
    # Check if token is valid before making API calls
    try:
        sp.current_user()
        waiting()
        print("Token is valid")
    except:
        print("Token is invalid or has expired")
        return False

    try:
        sp.me()  # Retrieves current user's profile
        waiting()
        print("Connection and authentication are OK!")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Authentication or connection error: {e}")
        return False

    token_info = auth_manager.get_cached_token()
    if token_info:
        access_token = token_info['access_token']
        print(f"Access Token: {access_token[:6]}...")
    else:
        print("Failed to retrieve access token")
        return False

    if token_info:
        expires_at = token_info.get('expires_at', 0)
        if expires_at < time.time():
            print("Token expired, refreshing...")
            new_token = sp.auth_manager.refresh_access_token(token_info['refresh_token'])
            print("New token received:", new_token)
        else:
            print("Token is still valid.")
    else:
        print("No cached token found.")

    if sp.auth_manager.is_token_expired(sp.auth_manager.get_cached_token()):
        sp.auth_manager.refresh_access_token(sp.auth_manager.get_cached_token()['refresh_token'])
    return True


def check_if_token_expired(sp):
    token_info = sp.auth_manager.get_cached_token()

    if token_info and token_info['expires_at'] < time.time():
        print("Token has expired, refreshing...")
        sp.auth_manager.refresh_access_token(token_info['refresh_token'])
    else:
        print("Token is valid")


def setup_spotify():
    credentials = load_credentials()
    auth_manager = SpotifyOAuth(
        client_id=credentials['client_id'],
        client_secret=credentials['client_secret'],
        redirect_uri="http://localhost:8888/callback",
        scope="playlist-modify-private playlist-modify-public user-read-playback-state user-modify-playback-state"
    )
    sp = spotipy.Spotify(auth_manager=auth_manager, requests_timeout=10, retries=1, status_retries=3, backoff_factor=1)

    validate_connection(sp, auth_manager)
    check_if_token_expired(sp)
    waiting()
    # Refresh token manually
    # sp.auth_manager.refresh_access_token(sp.auth_manager.get_cached_token()['refresh_token'])
    return sp


# Step 3: Helper functions to handle playlist actions
def get_current_track(sp):
    playback = sp.current_playback()
    if playback and playback['is_playing']:
        track_id = playback['item']['id']
        return track_id
    return None


def get_last_10_songs_in_playlist(sp, playlist_id) -> list:
    """
    Get the last 10 songs from a playlist.
    Returns a list of track IDs.
    """
    # Get the total number of tracks in the playlist
    playlist_info = sp.playlist(playlist_id, fields='tracks.total')
    total_tracks = playlist_info['tracks']['total']

    # Calculate the offset to retrieve the last 10 tracks
    if total_tracks < 10:
        limit = total_tracks  # If less than 10 tracks, get all
        offset = 0  # Start from the first track
    else:
        limit = 10
        offset = total_tracks - 10  # Start 10 tracks before the end

    # Get the last 10 tracks
    results = sp.playlist_tracks(playlist_id, fields='items.track.id', limit=limit, offset=offset)

    # Extract track IDs
    last_10_tracks = [item['track']['id'] for item in results['items']]

    return last_10_tracks


def add_to_playlist(sp, playlist_name, track_id):
    playlists = sp.current_user_playlists(limit=50)
    playlists = {playlist['name']: playlist['id'] for playlist in playlists['items']}

    if playlist_name in playlists:
        counter = 0
        while True:
            # verify if we could add track to playlist (search at the end)
            if track_id in get_last_10_songs_in_playlist(sp, playlists[playlist_name]):
                print(".")
                break
            else:
                if not counter:
                    print(f"Try to add track to playlist: {playlist_name}: {playlists[playlist_name]}")
                else:
                    print(counter * f".")
                sp.playlist_add_items(playlist_id=playlists[playlist_name], items=[track_id], position=None)
                time.sleep(0.2)
    else:
        print(f'Could not find {playlist_name}')


def handle_keypress(sp):
    while True:
        # Be careful putting here any request!
        # You can reach your request limit very quickly for 24 hours in an infinite loop...
        if keyboard.is_pressed('n'):
            track_id = get_current_track(sp)
            if track_id:
                add_to_playlist(sp, "_nope", track_id)
            else:
                print('No available track!')
            waiting()

        elif keyboard.is_pressed('m'):
            track_id = get_current_track(sp)
            if track_id:
                add_to_playlist(sp, "_maybe", track_id)
            else:
                print('No available track!')
            waiting()

        elif keyboard.is_pressed('l'):
            track_id = get_current_track(sp)
            if track_id:
                add_to_playlist(sp, "_buffer", track_id)
                # add_to_playlist(sp, "Gaming", track_id)
                # sp.current_user_saved_tracks_add([track_id])
                waiting()
            else:
                print('No available track!')
            waiting()

        elif keyboard.is_pressed('right'):
            playback_info = sp.current_playback()
            if playback_info and playback_info['is_playing']:
                current_position = playback_info['progress_ms']
                new_position = current_position + 30000  # Go forward 30 sec
                sp.seek_track(new_position)

        elif keyboard.is_pressed('left'):
            playback_info = sp.current_playback()
            if playback_info and playback_info['is_playing']:
                current_position = playback_info['progress_ms']
                new_position = max(0, current_position - 30000)  # Go back 30 sec
                sp.seek_track(new_position)

        elif keyboard.is_pressed('alt') and keyboard.is_pressed('p'):
            playback_info = sp.current_playback()
            if playback_info['is_playing']:
                sp.pause_playback()
            else:
                sp.start_playback()

        elif keyboard.is_pressed('down'):
            sp.next_track()

        elif keyboard.is_pressed('up'):
            sp.previous_track()

        elif keyboard.is_pressed('x'):
            exit()


# Step 5: Run the event loop
if __name__ == "__main__":
    sp = setup_spotify()

    devices = sp.devices()
    waiting()

    if not devices['devices']:
        print("No active devices found. Please start playback on a device.")
    else:
        print(f"Active device: {devices['devices'][0]['name']}")
        if sp:
            print("Press 'N', 'M', 'L', or 'X' on the keyboard to interact with Spotify.")
            handle_keypress(sp)
