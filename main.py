import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Support Ticket AI API")

# ---------------------------
# Load Models (Joblib Correct)
# ---------------------------

vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
tag_model = joblib.load("models/tag_classifier.pkl")
priority_model = joblib.load("models/priority_classifier.pkl")


# ---------------------------
# Request Schema
# ---------------------------

class TicketInput(BaseModel):
    text: str


# ---------------------------
# Business Rule Layer
# ---------------------------

def adjust_priority(tag, ml_priority, text):
    text = text.lower()

    # Force high priority for critical categories
    if tag in ["Security", "Outage", "Crash"]:
        return "high"

    urgent_keywords = ["urgent", "immediately", "critical", "severe", "asap"]
    if any(word in text for word in urgent_keywords):
        return "high"

    return ml_priority


# ---------------------------
# Root Route (No 404)
# ---------------------------

@app.get("/")
def home():
    return {"message": "Support Ticket AI API is running successfully."}


# ---------------------------
# Prediction Endpoint
# ---------------------------

@app.post("/predict")
def predict_ticket(ticket: TicketInput):
    try:
        vector = vectorizer.transform([ticket.text])

        # -------- Tag Prediction --------
        tag_probs = tag_model.predict_proba(vector)[0]
        tag_index = np.argmax(tag_probs)
        predicted_tag = tag_model.classes_[tag_index]
        tag_confidence = float(tag_probs[tag_index])

        # -------- Priority Prediction --------
        priority_probs = priority_model.predict_proba(vector)[0]
        priority_index = np.argmax(priority_probs)
        ml_priority = priority_model.classes_[priority_index]
        priority_confidence = float(priority_probs[priority_index])

        # -------- Hybrid Rule Adjustment --------
        final_priority = adjust_priority(predicted_tag, ml_priority, ticket.text)

        return {
            "predicted_tag": predicted_tag,
            "tag_confidence": round(tag_confidence, 3),
            "ml_priority": ml_priority,
            "priority_model_confidence": round(priority_confidence, 3),
            "final_priority": final_priority
        }

    except Exception as e:
        return {"error": str(e)}
