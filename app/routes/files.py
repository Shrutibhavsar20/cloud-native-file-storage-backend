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
def upload_file(file: UploadFile):
    return {"filename": file.filename}

