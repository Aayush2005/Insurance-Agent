from intent_classifier import classify_intent
from rag_pipeline import retrieve_context
from response_generator import generate_script_response
from user_data_handler import fetch_user_data
from call_flow import determine_branch
from stt import record_audio, transcribe_audio

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

        intent = classify_intent(user_text)
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
        print("—" * 60)

if __name__ == "__main__":
    main()
