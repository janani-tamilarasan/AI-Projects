# 🤖 AI Chatbot - FastAPI + Gemini + PostgreSQL

An AI-powered conversational chatbot built using **FastAPI**, **Google Gemini LLM**, and **PostgreSQL**.

The application provides AI-generated responses, stores conversation history, and follows a clean backend architecture.

![Demo](C:\Users\ADMIN\Downloads\ai-chatbot.mp4)

![AI Chatbot Demo](/ai-chatbot (1).mp4)
---

## 🚀 Features

- ✅ AI chatbot using Google Gemini API
- ✅ FastAPI REST API
- ✅ Conversation management
- ✅ Message history storage
- ✅ PostgreSQL database integration
- ✅ SQLAlchemy ORM
- ✅ Environment-based configuration
- ✅ Swagger API documentation
- ✅ Clean service-layer architecture

---

# 🏗️ Architecture

```
                User
                  |
                  |
             FastAPI API
                  |
        -------------------
        |                 |
 Chat Service       Database Layer
        |                 |
        |             PostgreSQL
        |
    Gemini API
        |
  AI Generated Response
```

---

# 🛠️ Tech Stack

## Backend

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | REST API Framework |
| SQLAlchemy | ORM |
| PostgreSQL | Database |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |

## AI

| Technology | Purpose |
|------------|---------|
| Google Gemini | Large Language Model |
| Prompt Engineering | AI Response Generation |

---

# 📂 Project Structure

```
ai-chatbot/

│
├── app/
│   │
│   ├── api/
│   │   └── chat.py
│   │
│   ├── database/
│   │   └── db.py
│   │
│   ├── models/
│   │   ├── users.py
│   │   ├── conversations.py
│   │   └── messages.py
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │   └── chat_service.py
│   │
│   └── main.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/janani-tamilarasan/AI-Projects.git

cd AI-Projects/ai-chatbot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Configuration

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key

DATABASE_URL=postgresql://username:password@localhost/chatbot_db
```

### Important

Do not commit `.env` into GitHub.

Use:

```
.env.example
```

for sharing configuration.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key

DATABASE_URL=your_database_url
```

---

# 🗄️ Database Design

## Users Table

```
users

id
email
created_at
```

---

## Conversations Table

```
conversations

id
user_id
title
created_at
```

---

## Messages Table

```
messages

id
conversation_id
role
content
created_at
```

Relationship:

```
User
 |
 |
Conversations
 |
 |
Messages
```

---

# ▶️ Run Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Application URL:

```
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI provides automatic Swagger documentation.

Open:

```
http://127.0.0.1:8000/docs
```

---

## Chat API Example

### Request

```
POST /chat
```

Body:

```json
{
  "message": "Explain Python decorators"
}
```

---

### Response

```json
{
  "response": "Python decorators are..."
}
```

---


