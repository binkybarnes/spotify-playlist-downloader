from pytube import YouTube
import os


def download_yt_mp3(url, destination):

    yt = YouTube(url)

    # extract only audio
    try:
        video = yt.streams.filter(only_audio=True).first()
    except pytube.exceptions.AgeRestrictedError as e:
        print("url: ", e)

    # download file

    out_file = video.download(output_path=destination)

    # save file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(f"{yt.title} has been downloaded in {destination}")


def main():
    url = "https://www.youtube.com/watch?v=_neDP3Dpo_I"
    destination = '/Users/johnpork/Desktop/python-stuff/webscraping/spotify-playlist-downloader/youtube-part/mp3-downloads'
    download_yt_mp3(url, destination)


if __name__ == "__main__":
    main()
