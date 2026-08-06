from app.models.analysis_reports import AnalysisReport


class AnalysisService:

    @staticmethod
    def save_analysis(
        db,
        resume_id,
        analysis
    ):

        report = AnalysisReport(
            resume_id=resume_id,
            analysis=analysis
        )

        db.add(report)

        db.commit()

        db.refresh(report)

        return report