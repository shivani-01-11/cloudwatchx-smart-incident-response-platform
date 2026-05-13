# incident generation logic


import json
import random
import time
from datetime import datetime
import boto3
from config import SERVICES, SEVERITY_DISTRIBUTION

EVENT_LOG_FILE = "../../events/sample_events/incidents.jsonl"
eventbridge = boto3.client("events", region_name="us-east-1")

def send_to_eventbridge(incident):

    response = eventbridge.put_events(
        Entries=[
            {
                "Source": "cloudwatchx.incident-generator",
                "DetailType": "Operational Incident",
                "Detail": json.dumps(incident),
                "EventBusName": "cloudwatchx-dev-eventbus"
            }
        ]
    )

    print("\n========== EVENT SENT TO EVENTBRIDGE ==========\n")
    print(response)

def generate_incident_id():
    return f"INC-{random.randint(10000, 99999)}"


def generate_severity():
    severities = list(SEVERITY_DISTRIBUTION.keys())
    weights = list(SEVERITY_DISTRIBUTION.values())

    return random.choices(severities, weights=weights, k=1)[0]


def generate_response_time(severity):
    ranges = {
        "LOW": (100, 800),
        "MEDIUM": (800, 2000),
        "HIGH": (2000, 5000),
        "CRITICAL": (5000, 10000)
    }

    min_time, max_time = ranges[severity]

    return random.randint(min_time, max_time)


def generate_retry_attempt(severity):
    retry_ranges = {
        "LOW": (0, 1),
        "MEDIUM": (1, 2),
        "HIGH": (2, 3),
        "CRITICAL": (3, 5)
    }

    min_retry, max_retry = retry_ranges[severity]

    return random.randint(min_retry, max_retry)


def generate_incident():
    service_name = random.choice(list(SERVICES.keys()))

    error_type = random.choice(SERVICES[service_name])

    severity = generate_severity()

    incident = {
        "incident_id": generate_incident_id(),
        "service_name": service_name,
        "environment": "production",
        "region": "us-east-1",
        "severity": severity,
        "error_type": error_type,
        "response_time_ms": generate_response_time(severity),
        "retry_attempt": generate_retry_attempt(severity),
        "status": "OPEN",
        "timestamp": datetime.utcnow().isoformat()
    }

    return incident

def generate_burst_incidents(service_name, count=10):
    burst_incidents = []

    for _ in range(count):
        severity = random.choices(
            ["HIGH", "CRITICAL"],
            weights=[40, 60],
            k=1
        )[0]

        incident = {
            "incident_id": generate_incident_id(),
            "service_name": service_name,
            "environment": "production",
            "region": "us-east-1",
            "severity": severity,
            "error_type": random.choice(SERVICES[service_name]),
            "response_time_ms": generate_response_time(severity),
            "retry_attempt": generate_retry_attempt(severity),
            "status": "OPEN",
            "timestamp": datetime.utcnow().isoformat()
        }

        burst_incidents.append(incident)

    return burst_incidents

def get_dynamic_interval():
    current_hour = datetime.utcnow().hour

    if 0 <= current_hour < 6:
        return random.uniform(4, 6)

    elif 6 <= current_hour < 9:
        return random.uniform(2, 4)

    elif 9 <= current_hour < 18:
        return random.uniform(0.5, 2)

    elif 18 <= current_hour < 22:
        return random.uniform(1, 3)

    else:
        return random.uniform(3, 5)
    
def save_incident_to_file(incident):
    with open(EVENT_LOG_FILE, "a") as file:
        file.write(json.dumps(incident) + "\n")

def stream_incidents(interval=2):
    while True:

        burst_chance = random.randint(1, 100)

        if burst_chance <= 15:
            affected_service = random.choice(list(SERVICES.keys()))

            print("\n========== INCIDENT BURST DETECTED ==========\n")
            print(f"Affected Service: {affected_service}\n")

            burst_incidents = generate_burst_incidents(
                affected_service,
                count=random.randint(5, 15)
            )

            for incident in burst_incidents:
                print(json.dumps(incident, indent=4))
                
                save_incident_to_file(incident)
                send_to_eventbridge(incident)

                time.sleep(0.5)

            print("\n========== BURST ENDED ==========\n")

        else:
            incident = generate_incident()

            print(json.dumps(incident, indent=4))
            
            save_incident_to_file(incident)
            send_to_eventbridge(incident)

            dynamic_interval = get_dynamic_interval()

            print(f"\nNext event in {dynamic_interval:.2f} seconds\n")

            time.sleep(dynamic_interval)

if __name__ == "__main__":
    stream_incidents()