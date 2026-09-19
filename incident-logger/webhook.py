from flask import Flask, request
import json
from datetime import datetime
import os
import boto3

app = Flask(__name__)

STORAGE_BACKEND = os.getenv("STORAGE_BACKEND", "local")
BUCKET_NAME = os.getenv("S3_BUCKET", "guardianstack-incidents")


@app.route("/alert", methods=["POST"])
def alert():
    data = request.json

    os.makedirs("incidents", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"incidents/incident_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    if STORAGE_BACKEND == "s3":
        s3 = boto3.client("s3")
        s3.upload_file(
            filename,
            BUCKET_NAME,
            os.path.basename(filename),
        )

    return {
        "status": "incident logged",
        "storage_backend": STORAGE_BACKEND,
    }, 200
