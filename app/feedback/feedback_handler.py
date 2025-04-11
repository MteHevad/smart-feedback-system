def collect_feedback(feedback: dict, sentiment: str):
    # Store in database or log
    print(f"Feedback received: {feedback['message']} | Sentiment: {sentiment}")
    return {"status": "received", "sentiment": sentiment}
