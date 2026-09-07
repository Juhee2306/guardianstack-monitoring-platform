from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import random
import time
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)
@app.route("/")
def home():
    hostname = os.getenv("HOSTNAME", "unknown")
    return f"GuardianStack v6 running on {hostname}!"

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "environment": os.getenv("APP_ENV", "unknown")
    }, 200

@app.route("/slow")
def slow():
    time.sleep(5)
    return "Slow response endpoint"

@app.route("/error")
def error():
    return {"error": "Simulated failure"}, 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
