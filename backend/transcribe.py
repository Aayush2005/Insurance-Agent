from faster_whisper import WhisperModel
from deep_translator import GoogleTranslator

model = WhisperModel("medium")

def transcribe_audio(filepath="test.wav", translate=True):
    segments, info = model.transcribe(filepath, beam_size=5)
    
    full_text = " ".join([segment.text for segment in segments])
    
    if translate:
        try:
            full_text = GoogleTranslator(source='auto', target='en').translate(full_text)
        except Exception as e:
            print(f"[!] Translation failed: {e}")

    return full_text
