from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import File
from app.services.s3 import upload_file_to_s3

router = APIRouter(prefix="/files", tags=["Files"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
def upload_file(file: UploadFile, db: Session = Depends(get_db)):
    s3_key = upload_file_to_s3(file)

    new_file = File(
        filename=file.filename,
        s3_key=s3_key
    )

    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return {
        "id": new_file.id,
        "filename": new_file.filename,
        "s3_key": new_file.s3_key
    }


