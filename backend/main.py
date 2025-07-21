from intent_classifier import classify_intent
from rag_pipeline import retrieve_context
from response_generator import generate_script_response
from user_data_handler import fetch_user_data
from call_flow import determine_branch
from stt import record_audio, transcribe_audio

from elevenlabs import generate, play, set_api_key
from deep_translator import GoogleTranslator
from stt import transcribe_audio

user_text = transcribe_audio("test.wav")  

def translate_to_english(text):
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except:
        return text  

set_api_key("sk_4411a3acffe20e7caa77731ceb1fd8507a53be8b1cf9be46")  

VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  

def speak_text(text):
    try:
        audio = generate(
            text=text,
            voice=VOICE_ID,
            model="eleven_multilingual_v2"
        )
        play(audio)
    except Exception as e:
        print(f"[ERROR] Could not generate or play audio: {e}")

def main():
    print("🎙 Insurance Voice Agent Terminal Interface\n")
    user_id = input("Enter user ID (or leave blank): ").strip()

    while True:
        print("🎤 Speak now (5 seconds)... or type 'exit' to quit.")
        audio_path = record_audio()
        user_text = transcribe_audio(audio_path)
        print(f"🧑 You said: {user_text}\n")

        if user_text.lower() == "exit":
            print("Goodbye!")
            break

        if not user_text.strip():
            print("[ERROR] Could not hear clearly, please try again.")
            continue

        try:
            intent = classify_intent(user_text)
        except Exception as e:
            print(f"[✗] Error during intent classification: {e}")
            speak_text("I'm sorry, I couldn't understand that. Can you repeat?")
            continue

        user_context = fetch_user_data(user_id) if user_id else ""
        static_context = retrieve_context(intent)

        policy_data = {
            "user_text": user_text,
            "user_context": user_context,
            "static_context": static_context,
            "policy_holder_name": "Mr. Jadhav",
            "policy_number": "XYZ123456",
            "premium_due_date": "2025-08-10",
            "outstanding_amount": "₹15,000",
            "total_premium_paid": "₹50,000",
            "product_name": "ULIP",
            "policy_start_date": "2018-06-01",
            "sum_assured": "₹5,00,000",
            "fund_value": "₹1,20,000"
        }

        branch = determine_branch(user_text, intent)
        final_response = generate_script_response(branch, user_text, policy_data)

        print("🤖 Agent:", final_response)
        speak_text(final_response)
        print("—" * 60)

if __name__ == "__main__":
    main()
