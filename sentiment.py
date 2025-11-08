from transformers import pipeline

# 1. Initialize the sentiment analysis pipeline
# This downloads a default model and tokenizer
# Model: "distilbert-base-uncased-finetuned-sst-2-english"
print("Loading model...")
sentiment_pipeline = pipeline("sentiment-analysis")
print("Model loaded.")

print("---")

# --- Example 1: Simple Positive ---
text1 = "I absolutely love this product! It's incredible."
result1 = sentiment_pipeline(text1)
print(f"Text: '{text1}'")
print(f"Result: {result1}")

print("---")

# --- Example 2: Simple Negative ---
text2 = "This is the worst customer service I have ever received."
result2 = sentiment_pipeline(text2)
print(f"Text: '{text2}'")
print(f"Result: {result2}")

print("---")

# --- Example 3: The "Context" Test (Slang) ---
# VADER or TextBlob might get this wrong, thinking "sick" is negative.
text3 = "This new user interface is sick! So responsive."
result3 = sentiment_pipeline(text3)
print(f"Text: '{text3}'")
print(f"Result: {result3}")

print("---")

# --- Example 4: Multiple Texts at Once ---
reviews = [
    "The food was delicious.",
    "It took 3 weeks to arrive and was broken.",
    "It's just okay, nothing special."
]
results = sentiment_pipeline(reviews)
print(f"Batch processing results:")
for text, result in zip(reviews, results):
    print(f"  - '{text}': {result}")