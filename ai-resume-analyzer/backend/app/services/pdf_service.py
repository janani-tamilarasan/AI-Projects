
from pypdf import PdfReader

class PdfService:

    @staticmethod
    def extract_file(file):
        try:
            reader = PdfReader(file)
            text = ''

            for page in reader.pages:
                page_text = page.extract_text()

                if(page_text):
                    text += page_text
            return text
        except Exception as e:
            raise e
