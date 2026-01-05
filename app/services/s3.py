import boto3
import uuid
from app.config import AWS_REGION, S3_BUCKET_NAME

s3 = boto3.client("s3", region_name=AWS_REGION)

def upload_file_to_s3(file):
    key = f"{uuid.uuid4()}_{file.filename}"
    s3.upload_fileobj(file.file, S3_BUCKET_NAME, key)
    return key

def generate_presigned_url(key, expires_in=300):
    return s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": S3_BUCKET_NAME, "Key": key},
        ExpiresIn=expires_in
    )
