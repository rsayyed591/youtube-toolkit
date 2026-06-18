import yt_dlp

url = input("Paste YouTube URL: ")

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

print("Done! MP3 downloaded.")
