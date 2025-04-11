# 🧠 Smart Feedback Collection & Real-Time Response System

This project is a complete smart hospitality feedback system that:
- Collects guest feedback via chatbots or kiosks
- Analyzes sentiment in real time
- Escalates urgent issues automatically
- Notifies staff and logs insights into a dashboard
- Generates reports for service improvements

## 🚀 Features
- AI-powered chatbot (Rasa/custom) for feedback
- Sentiment classification using Transformers
- Real-time escalation via email/SMS
- Web dashboard (Streamlit) for managers
- PDF reporting for staff training & review

## 🔧 Stack
- FastAPI, Rasa, Transformers
- Redis, PostgreSQL/MongoDB
- Streamlit / Dash for dashboard
- Celery for task queue
- Docker + Docker Compose for deployment

## ▶️ Run Locally
```bash
git clone https://github.com/yourname/smart-feedback-system.git
cd smart-feedback-system
cp .env.example .env
docker-compose up --build
