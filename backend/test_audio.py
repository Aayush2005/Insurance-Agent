import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

duration = 5  
fs = 16000  
device_index = 1  

print("🎙 Speak for 5 seconds...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16', device=device_index)
sd.wait()

wav.write("test3.wav", fs, recording)
print(" Audio saved as test3.wav")
