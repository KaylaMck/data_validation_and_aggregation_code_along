import boto3
import pandas as pd
import io

MINIO_URL = "http://localhost:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"

BUCKET_NAME = "raw"

def _get_s3_client():
    s3 = boto3.client(
        "s3",
        endpoint_url=MINIO_URL,
        aws_access_key_id=MINIO_ACCESS_KEY,
        aws_secret_access_key=MINIO_SECRET_KEY,
    )
    return s3

def get_students():
    s3 = _get_s3_client()
    file_name = "students.csv"

    response = s3.get_object(Bucket=BUCKET_NAME, Key=file_name)
    file_content = response["Body"].read()

    students = pd.read_csv(io.BytesIO(file_content))
    return students