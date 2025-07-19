import ollama
import os

def load_prompt(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Prompt file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def generate_script_response(branch: str, user_input: str, data: dict) -> str:
    prompt_path = f"prompts/{branch}.txt"

    try:
        template = load_prompt(prompt_path)
    except FileNotFoundError as e:
        return f"[ERROR] {e}"

    try:
        branch_script = template.format(user_input=user_input.strip(), **data)
    except KeyError as e:
        return f"[ERROR] Missing placeholder key in data: {e}"

    # ✅ Wrap your script with guiding instructions
    wrapped_prompt = f"""
You are Veena, a polite and professional insurance advisor speaking to a customer.

Use the following branch-specific call script to respond:
\"\"\"
{branch_script.strip()}
\"\"\"

The customer said: "{user_input.strip()}"

Respond based only on the relevant part of the script.
Do not repeat the whole script. Do not say “If customer says...” — just respond naturally.
""".strip()

    # === Log prompt ===
    os.makedirs("log", exist_ok=True)
    try:
        with open("log/prompt.log", "a", encoding="utf-8") as log_file:
            log_file.write(f"--- Prompt Sent to LLM ---\n{wrapped_prompt}\n\n")
    except Exception:
        pass

    response = None
    try:
        response = ollama.chat(model="mistral", messages=[
            {"role": "user", "content": wrapped_prompt}
        ])
    except Exception as e:
        try:
            with open("log/ollama_exception.log", "a", encoding="utf-8") as exc_file:
                exc_file.write(str(e) + "\n")
        except Exception:
            pass
        if response is not None:
            try:
                with open("log/ollama_partial_response.log", "a", encoding="utf-8") as log_file:
                    log_file.write(str(response) + "\n")
            except Exception:
                pass
        return f"[ERROR] Ollama call failed: {e}"

    # === Log raw response ===
    try:
        with open("log/ollama_raw_response.log", "a", encoding="utf-8") as log_file:
            log_file.write(str(response) + "\n")
    except Exception:
        pass

    # === Parse content ===
    content = ""
    if hasattr(response, "message") and hasattr(response.message, "content"):
        content = response.message.content.strip()
    elif isinstance(response, dict) and "message" in response and "content" in response["message"]:
        content = response["message"]["content"].strip()
    else:
        print("[ERROR] Could not find 'content' in response object.")
        return "[ERROR] Unknown response format from Ollama."

    return content or "[ERROR] Empty response from LLM."
