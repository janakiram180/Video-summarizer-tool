import yt_dlp
from whisper import audio_to_text

def download_video(video_url, output_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        ydl.download([video_url])
    return audio_to_text(output_path)
