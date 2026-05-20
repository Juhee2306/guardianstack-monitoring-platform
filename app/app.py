from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import random
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "GuardianStack is running!"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

@app.route("/slow")
def slow():
    time.sleep(5)
    return "Slow response endpoint"

@app.route("/error")
def error():
    return {"error": "Simulated failure"}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
