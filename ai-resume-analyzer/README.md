# 🤖 AI Resume Analyzer 
An AI-powered Resume Analysis and Job Matching application built using **FastAPI, React, PostgreSQL, LangChain, ChromaDB, and Google Gemini LLM**.

This application analyzes candidate resumes against job descriptions using **Retrieval Augmented Generation (RAG)** and provides AI-powered insights including:

- Resume match score
- Matched skills
- Missing skills
- Experience summary
- AI recommendations

---

# 🚀 Project Overview

Traditional resume screening requires recruiters to manually compare candidate resumes with job requirements.

This project automates the resume screening process using **Generative AI and RAG architecture**.

The system processes resumes, retrieves relevant information using semantic search, and uses Google Gemini LLM to generate meaningful resume analysis.

---

# 🔄 Application Workflow


```
User Upload Resume PDF

        |
        ↓

React Frontend

        |
        ↓

FastAPI Backend

        |
        ↓

Resume Validation

        |
        ↓

Extract Text from PDF

        |
        ↓

Save Resume Data

        |
        ↓

Split Resume into Chunks

        |
        ↓

Generate Embeddings

        |
        ↓

Store Embeddings in ChromaDB

        |
        ↓

Retrieve Relevant Resume Context

        |
        ↓

Gemini LLM Analysis

        |
        ↓

Save Analysis Result

        |
        ↓

Return AI Response

```

---

# ✨ Features

## 📄 Resume Processing

✅ Upload Resume PDF

✅ Validate resume file

✅ Extract text from PDF

✅ Store resume information

✅ Process resume documents using LangChain


---

## 🤖 AI Resume Analysis

✅ Compare resume with job description

✅ Generate resume match score

✅ Identify matching skills

✅ Identify missing skills

✅ Generate experience summary

✅ Provide AI recommendations


---

## 🔍 RAG Implementation

Implemented using:

- LangChain
- Google Gemini LLM
- ChromaDB Vector Database


### RAG Pipeline

```
Resume Document

      |
      ↓

Text Extraction

      |
      ↓

Document Chunking

      |
      ↓

Embedding Generation

      |
      ↓

Vector Storage (ChromaDB)

      |
      ↓

Similarity Search

      |
      ↓

Relevant Context Retrieval

      |
      ↓

Gemini LLM

      |
      ↓

Structured Resume Analysis

```

---

# 🛠️ Technologies Used


## Backend

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | REST API Framework |
| SQLAlchemy | ORM |
| PostgreSQL | Database |
| Pydantic | Data Validation |
| Uvicorn | Application Server |


---

## Generative AI

| Technology | Purpose |
|------------|---------|
| Google Gemini | Large Language Model |
| LangChain | RAG Framework |
| Embeddings | Semantic Search |
| Prompt Engineering | AI Response Generation |


---

## Vector Database

| Technology | Purpose |
|------------|---------|
| ChromaDB | Vector Storage |
| Similarity Search | Relevant Context Retrieval |


---

## Frontend

| Technology | Purpose |
|------------|---------|
| React | User Interface |
| TypeScript | Type Safety |
| Axios | API Communication |


---

# 🔌 API Endpoints


Base URL:

```
http://localhost:8000
```


Swagger Documentation:

```
http://localhost:8000/docs
```


---

## Resume Upload API


### Upload Resume

Upload resume PDF and analyze against job description.


### Endpoint

```
POST /resume/upload
```


### Request Type

```
multipart/form-data
```


### Parameters

| Parameter | Type | Required |
|-----------|------|----------|
| file | PDF File | Yes |
| job_description | String | Yes |


---

### Example Request


```
file:

resume.pdf


job_description:

Senior Backend Developer with Ruby Rails AWS experience

```


---

### Response Example


```json
{
    "analysis": {

        "match_score": 90,

        "matched_skills": [
            "Ruby",
            "Ruby on Rails",
            "AWS"
        ],

        "missing_skills": [
            "Docker"
        ],

        "experience_summary":
        "Candidate has backend development experience",

        "recommendation":
        "Strong match for this role"

    }
}
```

---

# 🌐 Application URLs


## Backend API

```
http://localhost:8000
```


## Swagger API Documentation

```
http://localhost:8000/docs
```


## Frontend Application

```
http://localhost:5173
```

---

# ⚙️ Backend Setup


Clone repository:

```bash
git clone https://github.com/janani-tamilarasan/AI-Projects.git
```


Navigate:

```bash
cd AI-Projects/ai-resume-analyzer/backend
```


Create virtual environment:

```bash
python -m venv .venv
```


Activate environment:


Windows:

```bash
.venv\Scripts\activate
```


Linux/Mac:

```bash
source .venv/bin/activate
```


Install dependencies:

```bash
pip install -r requirements.txt
```


Run application:

```bash
uvicorn app.main:app --reload
```


---

# 🔐 Environment Variables


Create `.env` file:


```
DATABASE_URL=postgresql://username:password@localhost/resume_db

GEMINI_API_KEY=your_gemini_api_key

CHROMA_DB_PATH=./chroma_db

```


⚠️ Never commit `.env` file to GitHub.

---

# 🎨 Frontend Setup


Navigate:

```bash
cd frontend
```


Install dependencies:

```bash
npm install
```


Start React application:

```bash
npm run dev
```


Frontend runs on:


```
http://localhost:5173
```

---

