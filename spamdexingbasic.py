from collections import Counter

# Example text that imitates spamdexing (keyword stuffing)
text = "cheap flights cheap tickets cheap hotels cheap packages cheap deals cheap cheap cheap"

tokens = text.lower().split()
count = Counter(tokens)
total_words = len(tokens)

print("Total words:", total_words)
print("Word frequencies:")

for word, freq in count.items():
    density = freq / total_words
    print(f"{word}: {freq} times ({density*100:.2f}%)")
    if density > 0.3:   # 30% threshold
        print("⚠️  Potential spam keyword:", word)
