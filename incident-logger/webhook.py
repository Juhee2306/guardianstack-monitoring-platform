from flask import Flask, request
import json
from datetime import datetime
import os
import boto3

app = Flask(__name__)

s3 = boto3.client('s3')

BUCKET_NAME = "guardianstack-incidents"

@app.route('/alert', methods=['POST'])
def alert():

    data = request.json

    os.makedirs("incidents", exist_ok=True)

    filename = f'incidents/incident_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    s3.upload_file(filename, BUCKET_NAME, os.path.basename(filename))

    return {"status": "incident logged and uploaded"}, 200

app.run(host="0.0.0.0", port=5001)
