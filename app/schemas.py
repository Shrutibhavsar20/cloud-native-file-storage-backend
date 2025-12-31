from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class FileResponse(BaseModel):
    id: UUID
    filename: str
    created_at: datetime

    class Config:
        from_attributes = True
