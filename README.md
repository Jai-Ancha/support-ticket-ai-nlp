# 📌 Support Ticket AI – Cloud-Deployed NLP Ticket Classification System

An end-to-end Machine Learning system that automatically classifies IT support tickets using Natural Language Processing and deploys predictions via a REST API and interactive web interface on AWS.

---

## 🚀 Project Overview

Manual classification of IT support tickets is time-consuming, inconsistent, and not scalable.

Support Ticket AI automates ticket categorization using a production-style NLP pipeline built with TF-IDF and Logistic Regression. The system is exposed through a FastAPI REST API and an interactive Streamlit frontend, deployed on AWS cloud infrastructure.

This project demonstrates real-world ML system design — from preprocessing and model training to secure cloud deployment.

---

## 🧠 Tech Stack

**Programming & ML**
- Python  
- Scikit-learn  
- TF-IDF Vectorization  
- Logistic Regression  
- Pandas  
- NumPy  
- Joblib  

**Backend & API**
- FastAPI (REST API)
- Uvicorn (ASGI Server)

**Frontend**
- Streamlit (Interactive Web UI)

**Cloud Infrastructure**
- AWS EC2 (Compute & Hosting)
- AWS S3 (Model / Asset Storage)
- AWS IAM (Secure Role & Permission Management)

---

## 🏗 System Architecture

User (Browser)  
        ↓  
Streamlit Frontend (Port 8501)  
        ↓  
FastAPI Backend (/predict endpoint – Port 8000)  
        ↓  
TF-IDF Vectorizer  
        ↓  
Logistic Regression Model  
        ↓  
Predicted Ticket Category  

---

## 🌍 Live Deployment

### 🔹 Frontend (Streamlit UI)
http://13.234.56.78:8501

### 🔹 Backend API Documentation (Swagger UI)
http://13.234.56.78:8000/docs

The FastAPI interactive documentation allows direct testing of the `/predict` endpoint.

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

1. User enters a support ticket description in the web interface.
2. Text is preprocessed and transformed using TF-IDF vectorization.
3. Logistic Regression model predicts the appropriate ticket category.
4. FastAPI serves the prediction via a REST endpoint.
5. Streamlit displays the classification result in real time.

---

## 🖥 How to Run Locally

### 1️⃣ Clone Repository

git clone https://github.com/your-username/support-ticket-ai.git  
cd support-ticket-ai  

### 2️⃣ Install Dependencies

pip install -r requirements.txt  

### 3️⃣ Run FastAPI Backend

uvicorn app:app --reload  

Backend runs at:  
http://127.0.0.1:8000  

### 4️⃣ Run Streamlit Frontend

streamlit run streamlit_app.py  

---

## ☁️ Cloud Deployment Architecture

The application is deployed on AWS using a structured cloud setup:

- **Amazon EC2** – Hosts FastAPI backend and Streamlit frontend
- **Amazon S3** – Stores model artifacts and project-related assets
- **AWS IAM** – Manages secure access control and permissions
- **Uvicorn** – Production ASGI server for FastAPI
- **Public IP Configuration** – Enables external system access

Security groups are configured to allow traffic on ports 8000 and 8501.

This demonstrates practical cloud infrastructure management beyond local ML experimentation.

---

## 📊 Model Details

- Feature Extraction: TF-IDF Vectorization  
- Algorithm: Logistic Regression  
- Multi-class classification  
- Model persistence using Joblib  
- Pre-trained model included for immediate testing  

---

## 🎯 Key Highlights

- End-to-end NLP pipeline
- REST API development using FastAPI
- Interactive frontend using Streamlit
- Cloud deployment on AWS
- IAM-based access control understanding
- Production-style modular architecture
- Real-world ML system simulation

---

## 📌 Future Enhancements

- Add evaluation metrics dashboard (Accuracy, Precision, Recall, F1-score)
- Add authentication & role-based access
- Containerization using Docker
- CI/CD pipeline integration
- Logging predictions to a database
- Load balancing & scalable deployment

---

## 👨‍💻 Author

Ancha Jai Ranganath  
Final-Year B.Tech CSE  
AIML & Cloud Computing Enthusiast  

Focused on building real-world AI systems with production-ready architecture.
