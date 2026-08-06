from fastapi import HTTPException, UploadFile


MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

ALLOWED_FILE_TYPE = "application/pdf"


def validate_resume(file: UploadFile):

    # Validate filename

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="File name is required"
        )


    # Validate file type

    if file.content_type != ALLOWED_FILE_TYPE:
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )


    # Validate file size

    file.file.seek(0)

    file_size = len(file.file.read())

    file.file.seek(0)


    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size should be less than 5MB"
        )


    return True