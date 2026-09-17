import argparse

import playlist_planner
import spotify_client
from models import IntervalSession


def parse_user_args():
    """Retrieve info about interval session entered by the user in the command line."""

    parser = argparse.ArgumentParser()

    parser.add_argument("dist_m", help="distance in meter", type=int)
    parser.add_argument("m_pace", help="minutes from pace in mm:ss/km", type=int)
    parser.add_argument("s_pace", help="seconds from pace in mm:ss/km", type=int)
    parser.add_argument("rest_s", help="rest in seconds", type=int)
    parser.add_argument("rep", help="number of repetitions", type=int)

    args = parser.parse_args()
    interval = IntervalSession(
        args.dist_m, args.m_pace, args.s_pace, args.rest_s, args.rep
    )
    return interval


def auth_spotify():
    """Connect to Spotify API with user authentification."""
    code = spotify_client.request_user_authorization()
    auth_dic = spotify_client.request_access_token(code)
    return auth_dic


def create_playlist(interval, auth_tokens):
    """Create a playlist with the songs alternating interval and rest matching songs."""

    r_new_playlist = spotify_client.create_new_playlist(auth_tokens)
    if r_new_playlist.status_code == 201:
        print("New playlist created")

    matching_songs = []
    i = 0
    while len(matching_songs) < interval.rep:
        items = spotify_client.get_liked_songs(auth_tokens, i)
        matching_songs = playlist_planner.select_matching_songs(
            interval, items, matching_songs
        )
        i += 1

    playlist_id = r_new_playlist.json()["id"]
    r_final_playlist = spotify_client.add_matching_songs_to_new_playlist(
        auth_tokens, matching_songs, playlist_id
    )

    if r_final_playlist.status_code == 201:
        print(f"Playlist ready: {r_new_playlist.json()["external_urls"]} ")


def main():

    try:
        interval = parse_user_args()
        print(interval)
        auth_tokens = auth_spotify()
        create_playlist(interval, auth_tokens)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
