import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# Initialize recognizer and TTS
recognizer = sr.Recognizer()
engine = pyttsx3.init()
pygame.mixer.init()
newsapi = "1234567890abcdef1234567890abcdef"

# List available microphones
print("Available microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")

# Choose a working mic manually
MIC_INDEX = 19
print("Using mic index:", MIC_INDEX)



# Speak function using gTTS + pygame
def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

# OpenAI function
def aiProcess(command):
    client = OpenAI(api_key="YOUR_OPENAI_API_KEY")  # fill in your key
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant. Give short responses."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

# Command processing
def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            articles = r.json().get("articles", [])
            for article in articles:
                speak(article["title"])
    else:
        output = aiProcess(c)
        speak(output)

# Main loop
if __name__ == "__main__":
    speak("Initializing your assistant...")
    try:
        with sr.Microphone(device_index=MIC_INDEX) as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            while True:
                print("Listening for wake word...")
                try:
                    audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
                    word = recognizer.recognize_google(audio)
                    print("Heard:", word)

                    if word.lower() == "zia":
                        speak("How can I help you?")
                        print("Listening for command...")
                        audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)
                        processCommand(command)

                except sr.WaitTimeoutError:
                    print("⏳ Timeout, no speech detected")
                except sr.UnknownValueError:
                    print("❌ Could not understand audio")
                except Exception as e:
                    print("⚠️ Error:", e)

    except Exception as e:
        print("Fatal error initializing microphone:", e)
