from textblob import TextBlob

def analyze_sentiment(text):
    """Analyze sentiment of a given text."""
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return {
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity
    }

if __name__ == "__main__":
    text = input("Enter text to analyze: ")
    result = analyze_sentiment(text)
    print(f"Polarity: {result['polarity']:.2f} (Positive if > 0)")
    print(f"Subjectivity: {result['subjectivity']:.2f} (0 = Factual, 1 = Opinionated)")
