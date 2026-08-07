from app.rag.embeddings.embedding_service import EmbeddingService
from langchain_chroma import Chroma
from app.config.settings import CHROMA_DB_PATH
from typing import List


class ChromaService:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.vector_store = Chroma(
            collection_name="resume_collection",
            embedding_function=self.embedding_service.model,
            persist_directory=CHROMA_DB_PATH
        )


    def store_chunks(
        self,
        chunks: List[str],
        resume_id: int
    ):

        metadata = self.create_metadata(
            chunks,
            resume_id
        )

        self.vector_store.add_texts(
            texts=chunks,
            metadatas=metadata
        )


    def create_metadata(
        self,
        chunks: List[str],
        resume_id: int
    ):

        return [
            {
                "resume_id": resume_id,
                "chunk_index": index
            }
            for index in range(len(chunks))
        ]