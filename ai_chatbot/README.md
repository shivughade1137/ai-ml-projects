
AI-Powered Chatbot using FastAPI
# AI Powered Chatbot using FastAPI & Transformers

An intelligent chatbot web application built using FastAPI and HuggingFace Transformers.  
The chatbot generates contextual responses and logs user interactions in a SQLite database.

---

## 🚀 Features

- AI based chatbot using NLP
- Contextual text generation using Transformers
- FastAPI backend
- Simple web interface
- Chat history logging
- SQLite database integration
- REST API support

---

## 🧠 Technologies Used

- Python
- FastAPI
- HuggingFace Transformers
- PyTorch
- SQLite
- Jinja2 Templates
- HTML/CSS

---

## 📂 Project Structure


ai_chatbot_fastapi
│
├── app
│ ├── main.py
│ ├── model.py
│ ├── database.py
│ └── schemas.py
│
├── templates
│ └── index.html
│
├── static
│ └── style.css
│
├── chatbot.db
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone Repository


git clone https://github.com/YOUR\_USERNAME/ai-chatbot-fastapi.git

cd ai-chatbot-fastapi


### 2️⃣ Create Virtual Environment


python -m venv venv


Activate environment

Windows:


venv\Scripts\activate


Mac/Linux:


source venv/bin/activate


---

### 3️⃣ Install Dependencies


pip install -r requirements.txt


---

## ▶️ Run the Application

Start the FastAPI server:


uvicorn app.main:app --reload


Open in browser:


http://127.0.0.1:8000


---

## 💬 Chatbot API Endpoint

### POST /chat

Request:


{
"message": "Hello"
}


Response:


{
"response": "Hello, how can I assist you today?"
}


---

## 🗄 Database

Chat interactions are stored in SQLite.

Table: `chat_logs`

Columns:

| Field | Type |
|------|------|
| id | Integer |
| user_message | Text |
| bot_response | Text |

---

## 📸 Example Use Case

User enters a message:


Hello chatbot


Bot generates response using AI model and logs the conversation.

---

## 🔮 Future Improvements

- Use OpenAI or Llama models
- Add conversation memory
- Deploy on cloud
- Add authentication
- Improve UI with React

---

## 👨‍💻 Author

Your Name

---

## 📜 License

This project is open-source and available under the MIT License.