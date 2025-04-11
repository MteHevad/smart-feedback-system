from fastapi import FastAPI
from app.feedback.feedback_handler import collect_feedback
from app.sentiment.analyzer import analyze_sentiment
from app.escalation.escalation import escalate_issue

app = FastAPI(title="Smart Feedback API")

@app.get("/")
def home():
    return {"message": "Smart Feedback System is running!"}

@app.post("/feedback/")
def handle_feedback(feedback: dict):
    sentiment = analyze_sentiment(feedback["message"])
    if sentiment == "negative":
        escalate_issue(feedback)
    return collect_feedback(feedback, sentiment)
