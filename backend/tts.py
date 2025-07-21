# tts.py
from gtts import gTTS
import os
from playsound import playsound
import uuid

def speak(text):
    filename = f"{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
