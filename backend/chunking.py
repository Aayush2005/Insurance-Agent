import os
import re
from PyPDF2 import PdfReader

INPUT_PDF = "data/company_docs/Calling_Script.pdf"
OUTPUT_DIR = "prompts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Read PDF content
reader = PdfReader(INPUT_PDF)
raw_text = "\n".join(page.extract_text() for page in reader.pages)

# Split by Branch headings
pattern = r"(Branch\s+\d+\.\d+.*?)\n(?=Branch\s+\d+\.\d+|\Z)"  
matches = re.findall(pattern, raw_text, flags=re.DOTALL)


for match in matches:

    branch_match = re.search(r"Branch\s+(\d+)\.(\d+)", match)
    if not branch_match:
        continue
    branch_id = f"branch_{branch_match.group(1)}_{branch_match.group(2)}"
    file_path = os.path.join(OUTPUT_DIR, f"{branch_id}.txt")

    # Clean and write
    cleaned = match.strip().replace("\n\n", "\n")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(cleaned)

print(f"[✓] Saved {len(matches)} branch prompt files to '{OUTPUT_DIR}'")
