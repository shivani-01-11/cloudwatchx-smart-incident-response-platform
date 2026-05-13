import json
import boto3

dynamodb = boto3.resource("dynamodb")

cloudwatch = boto3.client("cloudwatch")

table = dynamodb.Table("cloudwatchx-dev-incidents")


def publish_metrics(detail):

    severity = detail.get("severity", "UNKNOWN")

    service_name = detail.get("service_name", "unknown-service")

    response_time = detail.get("response_time_ms", 0)

    metric_data = [
        {
            "MetricName": "IncidentCount",
            "Value": 1,
            "Unit": "Count"
        },
        {
            "MetricName": "ResponseTime",
            "Value": response_time,
            "Unit": "Milliseconds"
        },
        {
            "MetricName": "ServiceIncidentCount",
            "Value": 1,
            "Unit": "Count",
            "Dimensions": [
                {
                    "Name": "ServiceName",
                    "Value": service_name
                }
            ]
        }
    ]

    if severity == "CRITICAL":
        metric_data.append(
            {
                "MetricName": "CriticalIncidentCount",
                "Value": 1,
                "Unit": "Count"
            }
        )

    cloudwatch.put_metric_data(
        Namespace="CloudWatchX/Operations",
        MetricData=metric_data
    )

    print("\n========== CLOUDWATCH METRICS PUBLISHED ==========\n")


def lambda_handler(event, context):

    print("\n========== INCIDENT EVENT RECEIVED ==========\n")

    print(json.dumps(event, indent=4))

    detail = event.get("detail", {})

    structured_log = {
        "incident_id": detail.get("incident_id"),
        "service_name": detail.get("service_name"),
        "severity": detail.get("severity"),
        "error_type": detail.get("error_type"),
        "status": detail.get("status")
    }

    print("\n========== STRUCTURED INCIDENT LOG ==========\n")

    print(json.dumps(structured_log, indent=4))

    table.put_item(Item=detail)

    print("\n========== INCIDENT STORED IN DYNAMODB ==========\n")

    publish_metrics(detail)

    return {
        "statusCode": 200,
        "body": json.dumps("Incident processed successfully")
    }