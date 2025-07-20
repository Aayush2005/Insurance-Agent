from faster_whisper import WhisperModel

model = WhisperModel("medium")

# Transcribe the audio file
segments, info = model.transcribe("test.wav", beam_size=5)

print("📄 Transcription:")
for segment in segments:
    print(segment.text)
