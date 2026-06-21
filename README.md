# Jarvis - Voice Assistant 🤖

A Python based voice assistant built with speech recognition.

## Features
- Wake word detection ("Jarvis")
- Play music from custom library via YouTube
- Read latest news headlines
- Open Google and YouTube
- Voice responses using pyttsx3

## Libraries Used
- SpeechRecognition
- pyttsx3
- requests
- python-dotenv
- os (built-in)
- time (built-in)
- webbrowser (built-in)

## Setup
1. Clone the repo
2. Create virtual environment:
   python -m venv env
3. Activate it:
   env\Scripts\activate
4. Install dependencies:
   pip install -r requirements.txt
5. Create .env file:
   NEWS_API_KEY=yourkey
6. Run:
   python jarvis.py

## How It Works
- Say "Jarvis" to wake it up
- Say "news" to hear latest headlines
- Say a song name to play music from YouTube
- Say "open google" to launch Google
- Say "open youtube" to launch YouTube
- Jarvis responds with voice for every command
