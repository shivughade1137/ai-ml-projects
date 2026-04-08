from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(text: str):

    result = sentiment_model(text)

    return {
        "sentiment": result[0]["label"],
        "confidence": result[0]["score"]
    }