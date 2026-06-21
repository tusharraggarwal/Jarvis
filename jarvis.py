import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from dotenv import load_dotenv
import os
import time
recognizer= sr.Recognizer()

load_dotenv()

def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processcommand(c):
    print("Command recieved",c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open chat" in c.lower():
        webbrowser.open("https://chatgpt.com")

    elif c.lower().startswith("play"):
        song=c.lower().replace("play", "").strip()
        musicLibrary.play(song)
        
    elif c.lower().startswith("news"):
        try:
            newsapi=os.getenv("NEWS_API_KEY")
            r = requests.get(f"https://newsapi.org/v2/top-headlines?language=en&apiKey={newsapi}")

            if r.status_code ==200:
            #parse the Json response
                data = r.json()
            # extract the article
                articles= data.get('articles',[])
            # print the headlines
                for article in articles[:3]:
                    title=article.get("title")
                    if title:
                        speak(title)
                        time.sleep(2)
            else:
                speak("could not fetch news")
        except Exception as e:
            print(f"Error:{e}")


if __name__=="__main__":
    speak("Initializing Jarvis...")
    time.sleep(2)
    while True:
        # listen for the wake word jarvis
        # obtain audio from microphone
        r= sr.Recognizer()
        print("Recognizing...")

        try:
             with sr.Microphone(device_index=1) as source:
                 r.adjust_for_ambient_noise(source,duration=1)
                 print("Listening...")
                 audio= r.listen(source, timeout=5,phrase_time_limit=2)
             word=r.recognize_google(audio)
             if(word.lower()=="jarvis"):
                speak("Yes, How can I help you")
                time.sleep(3)

                #  listen for command
                with sr.Microphone(device_index=1) as source:
                     print("Jarvis Active...")
                     audio= r.listen(source, timeout=5,phrase_time_limit=2)
                     command=r.recognize_google(audio)
                     print("you said",command)

                     processcommand(command)


        except Exception as e:
            print(f"Error:{e}")

