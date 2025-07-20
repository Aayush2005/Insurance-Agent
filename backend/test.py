import sounddevice as sd
import scipy.io.wavfile as wav

print("Recording 5 seconds...")
fs = 16000
duration = 5
recording = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype='int16')
sd.wait()

filename = "test.wav"
wav.write(filename, fs, recording)
print("Saved as test.wav")
