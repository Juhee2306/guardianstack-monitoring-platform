import boto3
import os

s3 = boto3.client('s3')

bucket_name = "guardianstack-incidents"

folder = "incidents"

for file in os.listdir(folder):

    filepath = os.path.join(folder, file)

    s3.upload_file(filepath, bucket_name, file)

    print(f"Uploaded {file}")
