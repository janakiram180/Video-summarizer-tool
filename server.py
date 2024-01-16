
import os
from summary import summarize_text
from youtube_video import download_video
from whisper import audio_to_text
from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)
app.config['upload_dir'] = os.path.join('uploads/')
os.makedirs(app.config['upload_dir'], exist_ok=True)
# the home route


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def upload_file():
    """
    The function upload_file() takes in a video file or a video link, transcribes the video, and
    summarizes the transcript

    Returns:
      the transcript and summary text.
    """
    if request.method == 'POST':
        video_file = request.files["video_file"]
        if video_file:
            filename = video_file.filename
            video_path = os.path.join(os.path.join(
                app.config['upload_dir'], filename))
            print(video_path)
            video_file.save(video_path)
            transcript_text = audio_to_text(video_path)
        else:
            video_link = request.form["link-input"]
            output_path = 'uploads/downloaded_video.mp4'
            transcript_text = download_video(video_link, output_path)
        
        summary_text = summarize_text(transcript_text['text'])
            # print(video_link)
    return render_template('index.html', transcript = transcript_text['text'],summary=summary_text)


if __name__ == '__main__':
    app.run()
