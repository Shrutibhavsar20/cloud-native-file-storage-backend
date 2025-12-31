from fastapi import FastAPI
from app.routes.files import router as file_router

app = FastAPI(title="Cloud File Storage Backend")

app.include_router(file_router)

@app.get("/")
def health_check():
    return {"status": "ok"}
