import argparse

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

    return IntervalSession(args.dist_m, args.m_pace, args.s_pace, args.rest_s, args.rep)


def auth_spotify(auth_tokens):
    """Connect to Spotify API with user authentification."""
    pass


def select_matching_songs(interval, auth_tokens):
    """Find user's songs matching the interval and rest duration with ±5sec margin."""
    pass


def create_playlist(matching_songs, auth_tokens):
    """Create a playlist with the songs alternating interval and rest matching songs."""
    pass


def main():
    auth_tokens = {}

    interval = parse_user_args()
    print(interval)
    auth_spotify(auth_tokens)
    matching_songs = select_matching_songs(interval, auth_tokens)
    create_playlist(matching_songs, auth_tokens)


if __name__ == "__main__":
    main()
