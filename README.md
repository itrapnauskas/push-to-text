<<<<<<< HEAD
# Audio Transcription System

This project provides a simple real-time audio transcription system using OpenAI's Whisper API. The application captures audio from the microphone, transcribes it into text, and simulates typing the transcribed text where the cursor is focused.

## Features

- **Real-time audio capture**: Records audio using the `sounddevice` library.
- **Transcription**: Converts audio to text using OpenAI's Whisper API.
- **Keyboard automation**: Automatically types the transcribed text where the cursor is focused.
- **Customizable shortcut**: Start and stop recording with `CTRL + 1`.

## Requirements

- Python 3.7+
- OpenAI API key

### Libraries

Install the required libraries using pip:

```bash
pip install sounddevice numpy keyboard wave openai pyautogui
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/audio-transcription.git
   cd audio-transcription
   ```

2. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```

3. Run the script:
   ```bash
   python audio_transcription.py
   ```

4. Press `CTRL + 1` to start recording and release it to transcribe the audio.

## File Structure

```
.
├── audio_transcription.py  # Main script
├── README.md               # Project documentation
├── .gitignore              # Git ignore file
```

## Notes

- The system uses a sample rate of 22,050 Hz for optimal balance between performance and accuracy.
- Temporary `.wav` files are created during the transcription process but are automatically deleted after use.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
=======
# push-to-text
>>>>>>> origin/main
