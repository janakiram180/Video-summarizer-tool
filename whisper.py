from transformers import pipeline
import subprocess


def audio_to_text(input_file):
    # mp4 to wav
    output_file = "video\wav\download.wav"
    subprocess.run(["ffmpeg", "-i", input_file, output_file])

    # transribing
    whisper = pipeline('automatic-speech-recognition',
                       model='openai/whisper-medium', chunk_length_s=30, device=-1)
    return whisper(output_file)
