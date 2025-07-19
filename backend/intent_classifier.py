import ollama
import os

from config import KNOWN_INTENTS  # Load from config or external file

def load_prompt(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Prompt file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def classify_intent(user_input: str) -> str:
    try:
        template = load_prompt("prompts/intent_classifier_prompt.txt")
        prompt = template.format(user_input=user_input.strip())

        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )

        prediction = response["message"]["content"].strip().lower().replace(" ", "_")

        if prediction in KNOWN_INTENTS:
            return prediction
        else:
            print(f"[!] Unrecognized prediction: '{prediction}'")
            return "unknown_intent"

    except Exception as e:
        print(f"[✗] Error during intent classification: {e}")
        return "unknown_intent"
