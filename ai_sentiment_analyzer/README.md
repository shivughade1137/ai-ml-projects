
AI Sentiment Analyzer using FastAPI
# AI Sentiment Analyzer using FastAPI & Transformers

A machine learning powered web application that analyzes the sentiment of user text using HuggingFace Transformers.

The system classifies text into positive or negative sentiment with a confidence score.

---

## 🚀 Features

- AI powered sentiment analysis
- FastAPI backend
- HuggingFace Transformers integration
- Real time text analysis
- Simple web interface
- REST API support

---

## 🧠 Technologies Used

- Python
- FastAPI
- HuggingFace Transformers
- PyTorch
- HTML
- CSS
- Jinja2 Templates

---

## 📂 Project Structure


sentiment_analyzer_fastapi
│
├── app
│ ├── main.py
│ ├── model.py
│ └── schemas.py
│
├── templates
│ └── index.html
│
├── static
│ └── style.css
│
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone Repository


git clone https://github.com/YOUR\_USERNAME/sentiment-analyzer-fastapi.git

cd sentiment-analyzer-fastapi


---

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

Start FastAPI server:


uvicorn app.main:app --reload


Open in browser:


http://127.0.0.1:8000


---

## 🔎 API Endpoint

### POST /analyze

Request:


{
"text": "This product is amazing"
}


Response:


{
"sentiment": "POSITIVE",
"confidence": 0.998
}


---

## 📊 Example

Input:


The movie was fantastic


Output:


Sentiment: POSITIVE
Confidence: 0.99


---

## 🔮 Future Improvements

- Support neutral sentiment
- Add charts for sentiment visualization
- Integrate social media data
- Deploy using Docker
- Deploy on AWS or GCP

---

## 👨‍💻 Author

Your Name

---

## 📜 License

This project is open-source and available under the MIT License.