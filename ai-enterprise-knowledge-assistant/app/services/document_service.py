from app.rag.loaders import Loader
from app.rag.splitter import Splitter
from app.rag.vector_db_store import VectorDbStore

class DocumentService:

    def __init__(self, file):
        self.file = file

    def process_document(self):

        # LOAD
        documents = Loader.load_documents(self.file)

        # SPLIT
        chunks = Splitter.split_documents(documents)

        # Generate Embeddings + Store in Qdrant (Vector Database)
        vector_store = VectorDbStore.store_vectors(chunks)


        return vector_store