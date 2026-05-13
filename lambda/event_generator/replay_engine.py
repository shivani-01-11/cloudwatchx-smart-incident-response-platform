import json
import time

EVENT_LOG_FILE = "../../events/sample_events/incidents.jsonl"


def replay_incidents(replay_speed=1):

    with open(EVENT_LOG_FILE, "r") as file:

        print("\n========== STARTING INCIDENT REPLAY ==========\n")

        for line in file:

            incident = json.loads(line.strip())

            print(json.dumps(incident, indent=4))

            time.sleep(replay_speed)

        print("\n========== INCIDENT REPLAY COMPLETED ==========\n")


if __name__ == "__main__":
    replay_incidents()