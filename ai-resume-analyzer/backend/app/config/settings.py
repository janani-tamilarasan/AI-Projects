import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

CHROMA_DB_PATH = os.getenv(
    "CHROMA_DB_PATH",
     "./chroma_db"
)


# Chunking

CHUNK_SIZE = int(
    os.getenv(
        "CHUNK_SIZE",
        800
    )
)

CHUNK_OVERLAP = int(
    os.getenv(
        "CHUNK_OVERLAP",
        150
    )
)


# Retrieval

TOP_K_RESULTS = int(
    os.getenv(
        "TOP_K_RESULTS",
        5
    )
)