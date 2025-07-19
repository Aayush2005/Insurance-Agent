def determine_branch(user_text: str, intent: str) -> str:
    user_text = user_text.lower()

    if "already paid" in user_text or "paid last" in user_text:
        return "branch_6_0"
    elif "can't pay" in user_text or "no money" in user_text or "financial" in user_text:
        return "branch_7_0"
    elif "call me later" in user_text or "busy" in user_text:
        return "branch_3_0"
    elif "don’t have bond" in user_text or "no policy bond" in user_text:
        return "branch_4_0"
    elif "not interested" in user_text or "don’t want to" in user_text:
        return "branch_8_0"
    elif intent == "premium_due" or intent == "renew_policy":
        return "branch_5_0"
    elif intent == "unknown_intent":
        return "branch_1_0"
    else:
        return "branch_2_0"
