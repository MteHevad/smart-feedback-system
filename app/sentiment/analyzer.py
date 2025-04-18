from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text: str) -> str:
    result = sentiment_pipeline(text)[0]
    return result['label'].lower()
