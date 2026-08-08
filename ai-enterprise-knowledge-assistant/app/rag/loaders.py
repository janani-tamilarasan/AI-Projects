import os
import tempfile

from langchain_community.document_loaders import PyPDFLoader


class Loader:

    @staticmethod
    def load_documents(file):

        # Save UploadFile to a temporary PDF file
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(file.file.read())
            temp_file_path = temp_file.name

        try:
            # PyPDFLoader needs a FILE PATH
            loader = PyPDFLoader(temp_file_path)

            documents = loader.load()

            return documents

        finally:
            # Remove temporary file
            os.remove(temp_file_path)