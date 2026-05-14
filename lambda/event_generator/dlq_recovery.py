import json
import boto3
from config import EVENT_BUS_NAME, QUEUE_URL

sqs = boto3.client("sqs")
eventbridge = boto3.client("events")


def recover_failed_events():

    print("\n========== STARTING DLQ RECOVERY ==========\n")

    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=5
    )

    messages = response.get("Messages", [])

    if not messages:
        print("No failed events found in DLQ.")
        return

    for message in messages:

        body = json.loads(message["Body"])

        original_event = body

        print("\n========== RECOVERING FAILED EVENT ==========\n")

        print(json.dumps(original_event, indent=4))

        replay_response = eventbridge.put_events(
            Entries=[
                {
                    "Source": original_event.get("source"),
                    "DetailType": original_event.get("detail-type"),
                    "Detail": json.dumps(original_event.get("detail")),
                    "EventBusName": EVENT_BUS_NAME
                }
            ]
        )

        print("\nReplay Response:")
        print(replay_response)

        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=message["ReceiptHandle"]
        )

        print("\n========== FAILED EVENT REMOVED FROM DLQ ==========\n")


if __name__ == "__main__":
    recover_failed_events()