from app.config.settings import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

print("Loaded CHUNK_SIZE =", CHUNK_SIZE)
print("Loaded CHUNK_OVERLAP =", CHUNK_OVERLAP)


class ChunkService:

    @staticmethod
    def create_chunks(text: str):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

        return splitter.split_text(text)