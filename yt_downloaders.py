import yt_dlp

def download_video(url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_mp3(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_playlist_mp3(url):
    ydl_opts = {
        "format": "bestaudio/best",

        "extractor_args": {
            "youtube": {
                "player_client": ["android"]
            }
        },

        "outtmpl": "%(playlist)s/%(playlist_index)04d - %(title)s.%(ext)s",

        "ignoreerrors": True,

        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }],
    }


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


while True:
    print("\n=== YouTube Downloader ===")
    print("1. Download Video")
    print("2. Download MP3")
    print("3. Download Playlist MP3")
    print("4. Exit")

    choice = input("\nChoose option: ")

    if choice == "1":
        url = input("Video URL: ")
        download_video(url)

    elif choice == "2":
        url = input("Video URL: ")
        download_mp3(url)

    elif choice == "3":
        url = input("Playlist URL: ")
        download_playlist_mp3(url)

    elif choice == "4":
        break

    else:
        print("Invalid choice!")