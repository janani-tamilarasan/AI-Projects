from app.rag.embeddings import embedding_model

from langchain_qdrant import QdrantVectorStore


class VectorDbStore:

    @staticmethod
    def store_vectors(chunks):

        vector_store = QdrantVectorStore.from_documents(
            documents=chunks,
            embedding=embedding_model,
            url="http://localhost:6333",
            collection_name="knowledge_base"
        )

        return vector_store