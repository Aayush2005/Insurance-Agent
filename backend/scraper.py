import requests
from bs4 import BeautifulSoup
import re

def clean_text(raw_text):
    text = re.sub(r'\s+', ' ', raw_text) 
    text = re.sub(r'http\S+|www\S+', '', text)  
    text = re.sub(r'[^A-Za-z0-9\s.,!?\'"-]', '', text)  
    return text.strip()

def scrape_multiple_and_append(urls, output_file='combined_output.txt'):
    with open(output_file, 'w', encoding='utf-8') as f:
        for url in urls:
            try:
                print(f"[+] Scraping: {url}")
                response = requests.get(url, timeout=10)
                response.raise_for_status()

                soup = BeautifulSoup(response.content, 'html.parser')
                raw_text = soup.get_text(separator=' ', strip=True)
                cleaned = clean_text(raw_text)

                f.write(f"\n\n=== Content from {url} ===\n\n")
                f.write(cleaned + "\n")
            except Exception as e:
                print(f"[-] Failed to scrape {url}: {e}")

    print(f"[✓] All content saved to {output_file}")

# Example usage
urls = [
    "https://licindia.in/faqs",
    "https://licindia.in/policy-conditions",
    "https://licindia.in/policy-guidelines-helpline"
]

scrape_multiple_and_append(urls, "data/company_docs/scraped.txt")
