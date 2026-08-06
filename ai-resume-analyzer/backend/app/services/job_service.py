from app.models.job_description import JobDescription


class JobService:

    @staticmethod
    def save_job_description(
        db,
        description
    ):

        job = JobDescription(
            description=description
        )

        db.add(job)

        db.commit()

        db.refresh(job)

        return job