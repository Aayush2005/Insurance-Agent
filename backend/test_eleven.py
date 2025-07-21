from elevenlabs import generate, play, set_api_key

set_api_key("sk_4411a3acffe20e7caa77731ceb1fd8507a53be8b1cf9be46")

audio = generate(
    text="Hello! This is ElevenLabs speaking live.",
    voice="21m00Tcm4TlvDq8ikWAM",  
    model="eleven_multilingual_v2"
)

play(audio)
