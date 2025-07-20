# stt.py
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import os
from faster_whisper import WhisperModel

MODEL_SIZE = "medium"  
model = WhisperModel(MODEL_SIZE, compute_type="int8")

def record_audio(duration=5, fs=16000, filename="user_input.wav"):
    print("🎙 Speak now (5 seconds)...")
    try:
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        write(filename, fs, recording)
        return filename
    except Exception as e:
        print("[ERROR] Recording failed:", str(e))
        return None

def transcribe_audio(audio_path):
    if not audio_path or not os.path.exists(audio_path):
        return "[UNRECOGNIZED]"

    segments, _ = model.transcribe(audio_path)
    transcript = ""
    for segment in segments:
        transcript += segment.text.strip() + " "
    return transcript.strip() if transcript else "[UNRECOGNIZED]"
