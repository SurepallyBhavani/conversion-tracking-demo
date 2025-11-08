import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon (only need to do this once)
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    print("Downloading VADER lexicon...")
    nltk.download('vader_lexicon')

# 1. Initialize the Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# 2. The same list of reviews
reviews = [
    "The food was delicious.",
    "It took 3 weeks to arrive and was broken.",
    "It's just okay, nothing special."
]

print("--- Applying VADER to the reviews ---")
print("")

# 3. Loop through and analyze each review
for review in reviews:
    scores = sia.polarity_scores(review)
    print(f"Review: '{review}'")
    print(f"Scores: {scores}")
    print("---")