import requests
from bs4 import BeautifulSoup
from collections import Counter

url = "https://books.toscrape.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text(" ", strip=True).lower()

tokens = text.split()
count = Counter(tokens)
total_words = len(tokens)

for word, freq in count.items():
    if freq/total_words > 0.05:  # 5% threshold for real text
        print(f"Potential spam keyword: {word} ({freq/total_words*100:.2f}%)")
