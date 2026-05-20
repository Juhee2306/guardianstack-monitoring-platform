import json
from datetime import datetime
import os

incident = {
    "timestamp": str(datetime.now()),
    "service": "guardianstack-app",
    "issue": "container_down",
    "severity": "critical"
}

filename = f"incidents/incident_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

os.makedirs("incidents", exist_ok=True)

with open(filename, "w") as f:
    json.dump(incident, f, indent=4)

print(f"Incident logged: {filename}")
