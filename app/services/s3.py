import boto3
import uuid
from app.config import AWS_REGION, S3_BUCKET_NAME

def upload_file_to_s3(file):
    # S3 will be used later when AWS is ready
    # For now, just return a fake key so app runs
    return f"local-{uuid.uuid4()}-{file.filename}"
