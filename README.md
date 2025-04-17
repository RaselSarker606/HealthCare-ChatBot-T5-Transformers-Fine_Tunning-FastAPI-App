# ✨ HealthCare ChatBot || T5 Transformers || Fine_Tunning || FastAPI-App

## 📖 Overview

This project is an AI-powered Healthcare Chatbot designed to assist users with common medical and service-related queries using a fine-tuned T5 Transformer. Hosted on a Flask web app, the chatbot is capable of answering practical questions like:

🧑‍💻 "How do I log in to the healthcare portal?"

🩺 "How can I book an appointment with a doctor?"

💰 "How do I check my balance or billing info?"

---

## 📂 Features

- 🧠 **T5 Transformer Model**: Fine-tuned for medical and healthcare-related Q&A.
- 🩺 **Healthcare-Focused Responses**: Handles queries related to symptoms, conditions, and treatments.
- 🧹 **Text Cleaning**: Cleans and preprocesses user inputs for improved model accuracy.
- 🌐 **Flask Web App**: Includes both a browser-based UI and a REST API.
- 🚀 **Real-Time Chat Interface**: Get fast and accurate replies via a `/chat` endpoint.

---

## 🛠️ Technologies Used

- **Python 3.x**  
- **Flask** – lightweight web server  
- **Hugging Face Transformers** – for T5 model  
- **Torch (PyTorch)** – for inference backend  
- **SentencePiece** – tokenizer support  
- **HTML & Jinja2** – simple web UI

---

## 🚀 Installation & Setup

### 📦 Prerequisites

- Python 3.7+
- A fine-tuned T5 model for healthcare domain (stored in a local folder, e.g., `model +token`)

### 🔧 Setup

```bash
git clone https://github.com/your-username/healthcare-t5-chatbot.git
cd healthcare-t5-chatbot
pip install flask transformers torch sentencepiece
```

Place your fine-tuned model in the folder `model +token`, or update the path in the code if different.

---

## ▶️ Running the Chatbot

```bash
python app.py
```

- Open the browser at: `http://127.0.0.1:5000/` to chat via the web UI  
- Send POST requests to: `http://127.0.0.1:5000/chat` to use the API

---

## 💬 Sample API Request

**POST** `/chat`

```json
{ "message": "What are the symptoms of diabetes?" }
```

**Response**:
```json
{ "response": "Common symptoms of diabetes include frequent urination, increased thirst, and fatigue." }
```

---

## 📌 Future Enhancements

- 🧾 **Medical Record Integration**: Support for personalized responses based on user health data
- 🔊 **Voice Input**: Speech-to-text and audio replies for better accessibility
- 🌐 **Multilingual Support**: Bengali, Hindi, and other regional languages
- 🔐 **Authentication**: Secure sensitive healthcare interactions

---

🚀 **Empowering healthcare with intelligent AI-driven conversations.**
