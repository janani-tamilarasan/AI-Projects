from app.rag.vector_db.chroma_service import ChromaService


class RetrieverService:


    def __init__(self):

        chroma_service = ChromaService()

        self.retriever = (
            chroma_service.vector_store
            .as_retriever(
                search_kwargs={
                    "k":5
                }
            )
        )


    def retrieve(
        self,
        query:str
    ):

        documents = self.retriever.invoke(
            query
        )

        return documents