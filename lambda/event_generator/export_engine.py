import json
from datetime import datetime

EVENT_LOG_FILE = "../../events/sample_events/incidents.jsonl"
EXPORT_DIRECTORY = "../../events/exports/"


def export_incidents():

    incidents = []

    with open(EVENT_LOG_FILE, "r") as file:

        for line in file:
            incidents.append(json.loads(line.strip()))

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    export_file = (
        f"{EXPORT_DIRECTORY}"
        f"incidents_export_{timestamp}.json"
    )

    with open(export_file, "w") as export:

        json.dump(incidents, export, indent=4)

    print("\n========== EXPORT COMPLETED ==========\n")
    print(f"Export File: {export_file}")
    print(f"Total Incidents Exported: {len(incidents)}")


if __name__ == "__main__":
    export_incidents()