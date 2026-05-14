# 🚀 CloudWatchX — Smart Incident Response Platform

A serverless event-driven AWS platform designed to simulate, process, monitor, and recover operational incidents using modern cloud-native architecture patterns.

---

# 📌 Project Overview

CloudWatchX is a hands-on AWS cloud engineering project built to demonstrate how modern distributed systems handle operational incidents using asynchronous event-driven workflows.

The platform simulates realistic enterprise operational failures such as:
- payment failures
- checkout failures
- authentication issues
- inventory synchronization failures
- notification delivery failures

These incidents are generated locally using Python and processed through a fully event-driven AWS architecture using:
- Amazon EventBridge
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch
- Amazon SNS
- Amazon SQS DLQ workflows

---

# ⚡ Key Highlights

✔ Event-driven AWS architecture  
✔ Serverless incident processing  
✔ Custom EventBridge event bus  
✔ CloudWatch operational dashboards  
✔ CloudWatch custom metrics  
✔ SNS email alerting  
✔ Lambda retry workflows  
✔ SQS Dead Letter Queue (DLQ) integration  
✔ DLQ replay recovery mechanism  
✔ Structured operational logging  
✔ AWS Free Tier optimized  
  

---

# 🏗️ High-Level Architecture

```text
Local Python Event Generator
              ↓
      Amazon EventBridge
              ↓
 AWS Lambda Incident Processor
        ↓              ↓
 DynamoDB        CloudWatch Metrics
        ↓              ↓
Incident Storage   Dashboards & Alarms
                           ↓
                     Amazon SNS Alerts

Failure Handling Flow:
Lambda Failure
      ↓
Retry Attempts
      ↓
Amazon SQS DLQ
      ↓
DLQ Replay Recovery
      ↓
EventBridge Reprocessing
```

---

# ☁️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| AWS Lambda | Incident processing |
| Amazon EventBridge | Event routing |
| Amazon DynamoDB | Incident storage |
| Amazon CloudWatch | Metrics, logs, dashboards, alarms |
| Amazon SNS | Operational notifications |
| Amazon SQS | Dead Letter Queue (DLQ) |
| AWS IAM | Authentication & permissions |
| AWS CLI | Local AWS authentication |
| boto3 | AWS SDK for Python |

---

# 🔄 Event-Driven Workflow

```text
Synthetic Incident Generated
            ↓
Event Published to EventBridge
            ↓
EventBridge Rule Match
            ↓
Lambda Incident Processing
            ↓
DynamoDB Incident Storage
            ↓
CloudWatch Metrics Published
            ↓
Dashboard Visualization
            ↓
CloudWatch Alarm Triggered
            ↓
SNS Email Notification
```

---

# 🛠️ Features Implemented

## ✅ Event-Driven Architecture
- Custom EventBridge event bus
- Event pattern routing
- Asynchronous Lambda invocation

## ✅ Synthetic Incident Simulation
- Realistic operational incidents
- Multiple services and severity levels
- Structured JSON event schema

## ✅ Serverless Processing
- Lambda-based incident processor
- Structured logging
- CloudWatch metric publishing

## ✅ Observability & Monitoring
- CloudWatch dashboards
- Custom operational metrics
- CloudWatch alarms
- Centralized logging

## ✅ Failure Handling & Recovery
- Lambda retry workflows
- SQS DLQ integration
- DLQ replay recovery engine
- Replayable event architecture

---

# 📊 Example Incident Payload

```json
{
  "incident_id": "INC-68602",
  "service_name": "checkout-service",
  "environment": "production",
  "region": "us-east-1",
  "severity": "CRITICAL",
  "error_type": "CHECKOUT_FAILURE",
  "response_time_ms": 5706,
  "retry_attempt": 5,
  "status": "OPEN",
  "timestamp": "2026-05-13T04:34:15.029048"
}
```

---

# 🧠 Distributed Systems Concepts Demonstrated

This project demonstrates several real-world cloud engineering concepts:

- Event-driven systems
- Serverless architecture
- Asynchronous processing
- Retry mechanisms
- Dead Letter Queues (DLQ)
- Replay-based recovery
- Failure isolation
- Operational observability
- Metric-driven monitoring
- Cloud-native alerting workflows

---

# 📂 Repository Structure

```text
cloudwatchx/
│
├── architecture/
├── dashboards/
├── docs/
├── events/
├── lambda/
├── monitoring/
├── screenshots/
└── README.md
```

---

# 💻 Local Development Setup

## Prerequisites

- Python 3.x
- AWS Account
- AWS CLI
- Git
- VS Code (recommended)

---

## Configure AWS CLI

```bash
aws configure
```

Configure:
- AWS Access Key
- AWS Secret Key
- Region (`us-east-1`)

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Event Generator

```bash
python generator.py
```

---

# 📈 Monitoring & Recovery Workflows

The platform currently supports:

✅ CloudWatch dashboards  
✅ CloudWatch alarms  
✅ SNS operational alerts  
✅ Lambda retry handling  
✅ SQS DLQ storage  
✅ DLQ replay recovery workflows  

Failed operational incidents can be replayed safely back into EventBridge for reprocessing.

---

# 🔐 Security Best Practices

The project follows several AWS security best practices:

- IAM least-privilege permissions
- No root account usage
- No secrets committed to GitHub
- `.gitignore` configured properly
- Environment-aware configuration management

---

# 🖼️ Architecture Diagrams

The repository includes multiple architecture diagrams explaining:

- EventBridge routing
- Lambda processing
- DynamoDB integration
- CloudWatch observability
- SNS alerting
- DLQ recovery workflows
- IAM permission flow
- End-to-end incident lifecycle

📌 Note:  
AI-assisted tools were used to help generate architecture diagrams.

---

# 🚧 Current Project Status

## ✅ Completed

- Event generation
- EventBridge routing
- Lambda processing
- DynamoDB storage
- CloudWatch metrics
- Operational dashboards
- SNS alerting
- Lambda retry workflows
- SQS DLQ integration
- DLQ replay recovery workflows

---

# 📚 Key Learnings

This project provided hands-on experience with:

- AWS serverless services
- Event-driven architecture
- Observability engineering
- Distributed system behavior
- Failure recovery patterns
- Cloud-native monitoring workflows
- Operational alerting systems

---

# 👩‍💻 Author

**Shivani Jannaikode**

---

# 📄 Disclaimer

This project was built for educational and portfolio purposes to simulate production-style operational monitoring systems using AWS Free Tier services.
