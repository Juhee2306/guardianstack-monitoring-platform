from flask import Flask, request
import json
from datetime import datetime
import os
import ast
import boto3
from kubernetes import client, config

app = Flask(__name__)

STORAGE_BACKEND = os.getenv("STORAGE_BACKEND", "local")
BUCKET_NAME = os.getenv("S3_BUCKET", "guardianstack-incidents")

# Use the Kubernetes ServiceAccount when running inside the cluster
config.load_incluster_config()
core_v1 = client.CoreV1Api()


def collect_flask_diagnostics():
    diagnostics = []

    pods = core_v1.list_namespaced_pod(
        namespace="default",
        label_selector="app=flask",
    )

    for pod in pods.items:
        restart_count = 0
        ready = False

        if pod.status.container_statuses:
            container = pod.status.container_statuses[0]
            restart_count = container.restart_count
            ready = container.ready

        try:
            logs = core_v1.read_namespaced_pod_log(
                name=pod.metadata.name,
                namespace="default",
                tail_lines=50,
            )

            if isinstance(logs, bytes):
                logs = logs.decode("utf-8", errors="replace")
            elif isinstance(logs, str) and logs.startswith("b'"):
                try:
                    decoded = ast.literal_eval(logs)
                    if isinstance(decoded, bytes):
                        logs = decoded.decode("utf-8", errors="replace")
                except (ValueError, SyntaxError):
                    pass


        except Exception as exc:
            logs = f"Unable to read logs: {exc}"

        diagnostics.append(
            {
                "pod": pod.metadata.name,
                "phase": pod.status.phase,
                "ready": ready,
                "restart_count": restart_count,
                "logs": logs,
            }
        )

    return diagnostics


@app.route("/alert", methods=["POST"])
def alert():
    data = request.json

    incident = {
        "timestamp": datetime.now().isoformat(),
        "alert": data,
        "diagnostics": {
            "flask_pods": collect_flask_diagnostics()
        },
    }

    os.makedirs("incidents", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"incidents/incident_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(incident, f, indent=4)

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
