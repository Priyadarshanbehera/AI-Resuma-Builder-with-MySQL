# FastAPI Resume Analysis Dashboard

A web application built with **FastAPI**, **Jinja2**, and **MySQL** that allows users to upload their resumes (PDF/DOCX) or paste text, specify a target role, and receive an AI‑powered analysis of their skills, missing skills, roadmap, and interview questions.  

The project uses **spaCy** for NLP and integrates with a database to store user reports.

---

## 🚀 Features
- User authentication with session management
- Resume upload (PDF/DOCX) or text input
- Automatic text extraction (pdfplumber / python-docx)
- AI analysis of resume skills vs. target role
- Dashboard with results (skills, missing skills, roadmap, interview questions)
- Reports saved to MySQL database
- Static assets (CSS) served via FastAPI

---

## 🛠️ Tech Stack
- **Backend**: FastAPI, SQLAlchemy
- **Frontend**: Jinja2 templates, HTML, CSS
- **Database**: MySQL
- **AI/NLP**: spaCy (`en_core_web_sm`)
- **File Parsing**: pdfplumber, python-docx, pytesseract (OCR fallback)

---

## 📂 Project Structure
├── main.py               # FastAPI entry point
├── ai.py                 # Resume analysis logic (spaCy)
├── db.py                 # Database connection
├── models.py             # SQLAlchemy models
├── templates/            # Jinja2 HTML templates
│   └── dashboard.html ... # show on 
├── static/               # Static files (CSS, JS)
│   └── style.css
└── requirements.txt      # Python dependencies


---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/fastapi-resume-dashboard.git
cd fastapi-resume-dashboard

### Create a virtual environment ###
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### 3. Install dependencies ###
pip install -r requirements.txt

### 4. Download spaCy model ###
python -m spacy download en_core_web_sm

### 5. Configure database ###
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@localhost/resume_db"

### 6. Start the server / run the main.py ###
uvicorn main:app --reload

