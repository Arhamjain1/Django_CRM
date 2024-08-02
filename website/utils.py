import json
import boto3
from django.conf import settings

def save_user_data_to_s3(user_data):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
    )

    user_data_json = json.dumps(user_data)
    file_name = f"user_data_{user_data['username']}.json"
    file_path = f"user_data/{file_name}"

    s3_client.put_object(Body=user_data_json, Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file_path)

    return file_path
