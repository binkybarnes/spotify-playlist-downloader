
from get_playlist_names import *
from get_YT_ID import *
from download_YT_MP3 import *


def main():
    token = get_token()
    song_names = get_playlist_songnames(token, "37i9dQZEVXcIZo27rvlFW9")

    load_dotenv()
    yt_ApiKey = os.getenv("YT_API_KEY")

    print("Spotify:" + ' '*(50-8) + "Youtube:")
    for name in (song_names):
        yt_id = get_video_id(yt_ApiKey, name)

        url = f"https://www.youtube.com/watch?v={yt_id}"
        destination = "/Users/johnpork/Desktop/python-stuff/webscraping/spotify-playlist-downloader/mp3-downloads"

        yt_name = download_yt_mp3(url, destination, 0)

        print(f"{name:50s}{yt_name}")


if __name__ == "__main__":
    main()
