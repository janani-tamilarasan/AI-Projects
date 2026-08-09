from langchain_qdrant import QdrantVectorStore

from app.rag.embeddings import embedding_model


vector_store = QdrantVectorStore.from_existing_collection(
    collection_name="knowledge_base",
    url="http://localhost:6333",
    embedding=embedding_model
)


retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 3
    }
)