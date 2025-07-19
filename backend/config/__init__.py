# config.py
DATA_PATH = "data/company_docs/scraped.txt"
INDEX_DIR = "vector_db"  # Save index here
META_PATH = f"{INDEX_DIR}/metadata.pkl"
EMBED_MODEL = "all-MiniLM-L6-v2"
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50
USE_HNSW = False


INDEX_PATH = "vector_db/index.faiss"
META_PATH = "vector_db/metadata.pkl"

KNOWN_INTENTS = {
    "cancel_policy", "change_payment_method", "financial_difficulty",
    "file_claim", "claim_status", "renew_policy", "premium_due", "policy_status",
    "update_contact", "update_address", "agent_contact", "payment_status",
    "download_policy", "forgot_policy_number", "policy_term_details",
    "reinstatement_query", "grace_period_query", "policy_transfer",
    "loan_against_policy", "update_nominee", "policy_benefits",
    "register_complaint", "tax_certificate", "auto_debit_setup", "branch_locator",
    "policy_upgrade", "change_mobile_number", "change_language", "change_email"
}
