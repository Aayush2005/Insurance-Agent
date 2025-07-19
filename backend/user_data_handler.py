from tinydb import TinyDB, Query

db = TinyDB("data/user_docs/user_data.json")
User = Query()

def fetch_user_data(user_id: str) -> str:
    result = db.search(User.id == user_id)
    if not result:
        return "No user-specific information available."

    user = result[0]
    
    # Turn dict into readable string
    context = "\n".join([f"{key.replace('_', ' ').title()}: {value}" for key, value in user.items() if key != "id"])
    return context
