from pytube import YouTube

# Paste the YouTube URL of the video you want to download
url = "https://www.youtube.com/watch?v=eOPeYoXrIHs"

# Create a YouTube object
yt = YouTube(url)

# Get the first stream that has a MIME type of "audio/wav"
audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/wav").first()

# Download the audio stream
audio_stream.download('/sound')