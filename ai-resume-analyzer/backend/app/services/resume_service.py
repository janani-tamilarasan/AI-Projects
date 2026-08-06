
from app.models.resumes import Resume


class ResumeService:

    @staticmethod
    def save_resume(
        db,
        filename,
        content
    ):

        resume = Resume(
            file_name=filename,
            file_content=content
        )

        db.add(resume)

        db.commit()

        db.refresh(resume)

        return resume