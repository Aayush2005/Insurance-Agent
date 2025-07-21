import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel


MICROPHONE_INDEX = 1

# Record from mic
def record_audio(filename="user_input.wav", duration=5, fs=44100, device_index=MICROPHONE_INDEX):
    try:
        print("🎙 Speak now (5 seconds)...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16', device=device_index)
        sd.wait()
        write(filename, fs, recording)
        return filename
    except Exception as e:
        print(f"[ERROR] Recording failed: {e}")
        return ""

def transcribe_audio(audio_path):
    try:
        model = WhisperModel("medium", device="cpu", compute_type="int8")  
        segments, _ = model.transcribe(audio_path)

        full_text = ""
        for segment in segments:
            full_text += segment.text + " "

        return full_text.strip() if full_text else "[UNRECOGNIZED]"
    except Exception as e:
        print(f"[ERROR] Transcription failed: {e}")
        return "[UNRECOGNIZED]"
