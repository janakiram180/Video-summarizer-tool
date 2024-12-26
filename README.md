

# Video Summarizer Tool  

This repository contains a **Video Summarizer Tool** that processes video files to generate concise and meaningful summaries. The tool leverages state-of-the-art AI models like **Hugging Face Whisper** for audio transcription and **Pegasus** for text summarization, combined with a user-friendly web interface for seamless interaction.

## Features  
- **Audio Transcription**: Extracts speech from video files using **Hugging Face Whisper**.  
- **Text Summarization**: Summarizes the transcribed content using the **Pegasus** model.  
- **Web Interface**: Provides a simple and intuitive interface for video uploads and summary generation.  
- **Real-Time Processing**: Quickly processes video files to generate summaries efficiently.  

## How It Works  
1. **Upload a Video**: The user uploads a video file through the web interface.  
2. **Audio Extraction**: The tool extracts audio from the video.  
3. **Transcription**: Speech in the audio is transcribed into text using Whisper.  
4. **Summarization**: The transcribed text is summarized using Pegasus to provide concise insights.  
5. **Summary Display**: The generated summary is displayed to the user on the interface.  

## Requirements  
- Python 3.8+  
- Libraries:  
  - `transformers`  
  - `torch`  
  - `moviepy`  
  - `flask`  
  - `whisper`  

## Setup Instructions  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/janakiram180/Video-summarizer-tool.git  
   cd Video-summarizer-tool  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Run the application:  
   ```bash  
   python app.py  
   ```  
4. Open the web interface in your browser:  
   ```
   http://127.0.0.1:5000  
   ```  

## Usage  
- Upload a video file via the web interface.  
- Wait for the tool to process the video and generate the summary.  
- View or download the summary from the interface.  

## Technologies Used  
- **Hugging Face Whisper**: For accurate speech-to-text transcription.  
- **Pegasus**: For state-of-the-art text summarization.  
- **Flask**: Backend framework for building the web interface.  
- **MoviePy**: For video and audio processing.  

## Future Enhancements  
- Add support for multiple languages.  
- Integrate with cloud storage for larger video files.  
- Optimize processing time for longer videos.  
- Enhance summarization with user-selectable models.  

## License  
This project is licensed under the MIT License. See the `LICENSE` file for more details.  

