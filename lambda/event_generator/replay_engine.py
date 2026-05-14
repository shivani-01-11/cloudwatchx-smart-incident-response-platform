import json
import time
import boto3
from config import EVENT_BUS_NAME

EVENT_LOG_FILE = "../../events/sample_events/incidents.jsonl"

eventbridge = boto3.client("events")

def replay_incidents(replay_speed=1):

    with open(EVENT_LOG_FILE, "r") as file:

        print("\n========== STARTING INCIDENT REPLAY ==========\n")

            
        for line in file:

            incident = json.loads(line.strip())

            response = eventbridge.put_events(
            Entries=[
                {
                "Source": "cloudwatchx.incident-generator",
                "DetailType": "Operational Incident",
                "Detail": json.dumps(incident),
                "EventBusName": EVENT_BUS_NAME,
                }
            ]
            )

            print("\n========== REPLAYED INCIDENT ==========\n")
            print(json.dumps(incident, indent=4))

            print("\nEventBridge Response:")
            print(response)

            time.sleep(replay_speed)

            time.sleep(replay_speed)

        print("\n========== INCIDENT REPLAY COMPLETED ==========\n")


if __name__ == "__main__":
    replay_incidents()