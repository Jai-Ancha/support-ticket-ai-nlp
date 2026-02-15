# 📌 Support Ticket AI – Cloud-Deployed NLP Ticket Classification System

An end-to-end Machine Learning system that automatically classifies IT support tickets using Natural Language Processing and deploys predictions via a REST API and interactive web interface.

---

## 🚀 Project Overview

Manual classification of IT support tickets is time-consuming, inconsistent, and not scalable.  

Support Ticket AI automates ticket categorization using an NLP pipeline built with TF-IDF and Logistic Regression, deployed using FastAPI and Streamlit on AWS EC2.

This project demonstrates real-world ML deployment architecture — from preprocessing to cloud hosting.

---

## 🧠 Tech Stack

- Python  
- Scikit-learn  
- TF-IDF Vectorization  
- Logistic Regression  
- FastAPI (Backend REST API)  
- Streamlit (Frontend UI)  
- Uvicorn (ASGI Server)  
- AWS EC2 (Cloud Deployment)

---

## 🏗 System Architecture

User (Browser)  
        ↓  
Streamlit Frontend  
        ↓  
FastAPI Backend (/predict endpoint)  
        ↓  
TF-IDF Vectorizer  
        ↓  
Logistic Regression Model  
        ↓  
Predicted Ticket Category  

---

## 📂 Project Structure

support-ticket-ai/
│
├── app.py                  # FastAPI backend
├── streamlit_app.py        # Streamlit frontend
├── requirements.txt
├── README.md
│
├── model/
│   ├── model.pkl
│   ├── vectorizer.pkl

---

## ⚙️ How It Works

1. User enters a support ticket description.
2. Text is preprocessed and transformed using TF-IDF.
3. Logistic Regression model predicts ticket category.
4. FastAPI returns prediction through a REST API.
5. Streamlit displays real-time classification result.

---

## 🖥 How to Run Locally

### 1️⃣ Clone Repository

git clone https://github.com/your-username/support-ticket-ai.git  
cd support-ticket-ai  

### 2️⃣ Install Dependencies

pip install -r requirements.txt  

---

Frontend:
http://13.234.56.78:8501

Backend Docs:
http://13.234.56.78:8000/docs

---

## 🌐 Deployment

The application is deployed on AWS EC2 using:

- Ubuntu Server
- Python environment
- Uvicorn ASGI server
- Public IP-based access

---

## 📊 Model Details

- Feature Extraction: TF-IDF Vectorization  
- Algorithm: Logistic Regression  
- Multi-class classification  
- Pre-trained model included for direct testing  

---

## 🎯 Key Highlights

- End-to-end NLP pipeline
- REST API design
- Cloud deployment experience
- Production-style architecture
- Modular project structure

---

## 📌 Future Improvements

- Add evaluation metrics (Accuracy, Precision, Recall, F1-score)
- Add authentication layer
- Containerize using Docker
- Implement CI/CD pipeline
- Integrate database logging for predictions

---

## 👨‍💻 Author

Ancha Jai Ranganath  
Final-Year B.Tech CSE | AIML & Cloud Enthusiast  
Focused on real-world AI system design and deployment.
