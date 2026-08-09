# 🤖 AI Enterprise Knowledge Assistant

An AI-powered Knowledge Assistant that allows users to upload documents and ask questions about them.

The application uses **RAG (Retrieval-Augmented Generation)** to find relevant information from uploaded documents and uses an **LLM** to generate answers.

---

# 🎥 Working Demo

<video src="./demo/AI-Assistant.mp4" controls width="800"></video>

# Set up
git clone https://github.com/janani-tamilarasan/AI-Projects.git
cd AI-Projects/ai-enterprise-knowledge-assistant
.venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
alembic revision --autogenerate -m ""
uvicorn main:app --reload
http://127.0.0.1:8000/docs

# Api
POST /documents/upload
POST /documents/retrive

# 🚀 Features

- 📄 Upload documents
- 📖 Read and process PDF documents
- ✂️ Split documents into smaller chunks
- 🧠 Generate embeddings
- 🔎 Search relevant document content
- 🗄️ Store embeddings in Qdrant
- 🤖 Generate answers using an LLM
- 🔗 Use LangChain for RAG
- 🕸️ Use LangGraph for workflow management
- ⚡ FastAPI REST APIs
- 🐘 PostgreSQL for application data
- 🔄 Alembic for database migrations

---

# 🛠️ Tools / Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Programming language |
| FastAPI | Backend REST API |
| LangChain | RAG and LLM integration |
| LangGraph | AI workflow management |
| Qdrant | Vector database |
| PostgreSQL | Relational database |
| SQLAlchemy | Database ORM |
| Alembic | Database migrations |
| HuggingFace | Embeddings |
| Groq | LLM |
| PyPDF | PDF processing |

---

# What is RAG?

RAG means **Retrieval-Augmented Generation**.

Instead of directly asking the LLM a question, the application first searches the uploaded documents and retrieves relevant information.

Then the retrieved information is given to the LLM to generate the answer.

```text

                USER
                  |
                  v
          Upload Document
                  |
                  v
              FastAPI
                  |
                  v
          Document Processing
                  |
                  v
          Extract Text
                  |
                  v
          Split into Chunks
                  |
                  v
          Generate Embeddings
                  |
                  v
              Qdrant
                  |
                  |
                  |  User asks question
                  |
                  v
              FastAPI
                  |
                  v
             LangGraph
                  |
                  v
             Retrieve
                  |
                  v
        Search Qdrant
                  |
                  v
       Relevant Document Chunks
                  |
                  v
             Generate
                  |
                  v
                LLM
                  |
                  v
             Final Answer

```text
