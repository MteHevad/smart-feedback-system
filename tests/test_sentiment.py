from app.sentiment.analyzer import analyze_sentiment

def test_sentiment():
    assert analyze_sentiment("I hate this service") == "negative"
    assert analyze_sentiment("I love this place") == "positive"
