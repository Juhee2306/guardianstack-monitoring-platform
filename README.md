# GuardianStack

> Containerized Monitoring & Incident Automation Platform built with Docker, Prometheus, Grafana, Alertmanager, AWS S3, GitHub Actions, and AWS EC2.

GuardianStack is a production-style monitoring and incident management platform designed to monitor containerized applications, detect failures automatically, trigger alerts, archive incidents, and deploy continuously using CI/CD pipelines.

The project combines observability, automation, cloud deployment, and infrastructure monitoring into a single Dockerized stack.

---

# Architecture Diagram

<img width="1854" height="1234" alt="79044" src="https://github.com/user-attachments/assets/9661810d-bb0f-4b66-948b-3938f59fd1c0" />


---

# Features

- Reverse proxy using NGINX
- Flask application with custom Prometheus metrics
- Real-time infrastructure and container monitoring
- Alerting using Prometheus and Alertmanager
- Automated webhook-based incident handling
- Incident archival to AWS S3
- Grafana dashboards
- Docker Compose deployment
- Kubernetes deployment
- CI/CD using GitHub Actions
- AWS EC2 deployment

---

# Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, Flask |
| Monitoring | Prometheus, Node Exporter, cAdvisor |
| Visualization | Grafana |
| Alerting | Alertmanager |
| Reverse Proxy | NGINX |
| Containerization | Docker, Docker Compose |
| Cloud | AWS EC2, AWS S3 |
| CI/CD | GitHub Actions |
| OS | Linux (Ubuntu) |

---

# System Workflow

```text
User Request
↓
NGINX Reverse Proxy
↓
Flask Application
↓
Prometheus Scrapes Metrics
↓
Alert Rules Evaluated
↓
Alertmanager Routes Alerts
↓
Webhook Receives Incident
↓
Incident Stored as JSON
↓
Incident Uploaded to AWS S3
```

---

# Infrastructure Components

| Service | Purpose | Port |
|---|---|---|
| Flask App | Main application | 5000 |
| NGINX | Reverse proxy | 80 |
| Prometheus | Metrics collection & alerting | 9090 |
| Grafana | Dashboard visualization | 3000 |
| Alertmanager | Alert routing | 9093 |
| cAdvisor | Container metrics | 8080 |
| Node Exporter | Host metrics | 9100 |
| Webhook Service | Incident processing | 5001 |

---
## Kubernetes Migration

GuardianStack was originally deployed using Docker Compose and later migrated to Kubernetes using Minikube.

### Kubernetes Components

* Flask Application
* Prometheus
* Alertmanager
* Webhook Service

### Kubernetes Resources

* Deployments
* Services
* ConfigMaps
* Secrets
* Alert Rules

### Validation

The complete monitoring and incident management workflow was validated through end-to-end failure testing.

```text
Application Failure
        ↓
Prometheus Alert
        ↓
Alertmanager Notification
        ↓
Webhook Processing
        ↓
Incident Storage
```

### Outcome

Successfully validated:

* Prometheus alert generation
* Alertmanager alert routing
* Webhook-based incident processing
* Incident JSON generation
* AWS S3 incident storage integration
* Kubernetes Secret-based credential management
  
---

# Monitoring Stack

GuardianStack uses multiple monitoring components together:

- **Prometheus** scrapes application and infrastructure metrics
- **Node Exporter** collects host-level metrics
- **cAdvisor** collects container metrics
- **Grafana** visualizes metrics through dashboards
- **Alertmanager** handles alert routing and notifications

---

# Alerting Workflow

The platform automatically detects failures using Prometheus alert rules.

Example flow:

```text
Flask Application Down
↓
Prometheus Detects Failure
↓
Alertmanager Fires Alert
↓
Webhook Receives Payload
↓
Incident Logged as JSON
↓
Incident Uploaded to AWS S3
```

---

# CI/CD Pipeline

GuardianStack includes automated CI/CD pipelines using GitHub Actions.

## Continuous Integration (CI)

On every push:

- Validates Docker Compose configuration
- Builds Docker containers
- Detects infrastructure issues early

## Continuous Deployment (CD)

On successful push to `main`:

- GitHub Actions connects to EC2 via SSH
- Pulls latest repository changes
- Rebuilds Docker containers
- Restarts the monitoring stack automatically

---

# AWS Deployment

GuardianStack is deployed on an AWS EC2 Ubuntu instance using Docker Compose.

The deployment includes:

- Public cloud hosting
- Dockerized services
- Automated CI/CD deployment
- Multi-container orchestration
- Persistent monitoring infrastructure

---

# Screenshots

## Grafana Dashboard

![Grafana Dashboard](./screenshots/grafana-dashboard.png)

---

## Prometheus Targets

![Prometheus Targets](./screenshots/prometheus-targets1.png)

---

## Alert Firing
<img width="1918" height="436" alt="prometheus-alerts" src="https://github.com/user-attachments/assets/5e915d87-1859-49d8-abba-312ab21fd534" /><img width="1314" height="559" alt="github-actions-success" src="https://github.com/user-attachments/assets/38fa2e49-3940-417d-b72f-03a84300910b" />


---

## Docker Containers

![Docker Containers](./screenshots/docker-containers.png)

---

## AWS S3 Incident Storage

![S3 Storage](./screenshots/s3-incident-storage.png)

---

## GitHub Actions CI/CD


<img width="1314" height="559" alt="github-actions-success" src="https://github.com/user-attachments/assets/4632f5d4-bc4c-422a-a091-e8b6118c8ecb" />

---

# Project Structure

```text<img width="1854" height="1234" alt="79044" src="https://github.com/user-attachments/assets/0166db3d-5bb3-4dd4-a8e3-deeb09e72d00" />

guardianstack/
│
├── app/
├── nginx/
├── prometheus/
├── alertmanager/
├── incident-logger/
├── k8s/
├── screenshots/
├── .github/workflows/
├── docker-compose.yml
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/Juhee2306/guardianstack-monitoring-platform.git
cd guardianstack-monitoring-platform
```

---

## 2. Configure AWS Credentials

Configure AWS CLI credentials for S3 uploads:

```bash
aws configure
```

---

## 3. Start GuardianStack

```bash
docker compose up --build -d
```

---

# Access Services

| Service | URL |
|---|---|
| Main Application | `http://PUBLIC_IP` |
| Grafana | `http://PUBLIC_IP:3000` |
| Prometheus | `http://PUBLIC_IP:9090` |
| Alertmanager | `http://PUBLIC_IP:9093` |

---

# Challenges Faced

Some real-world engineering challenges encountered during development:

- Challenges Faced
- Docker networking issues
- Prometheus metrics debugging
- Alertmanager integration
- Kubernetes ConfigMaps
- Kubernetes Secrets
- AWS credential management
- Alert pipeline validation

---

# Learning Outcomes

This project helped strengthen practical skills in:

- Linux server management
- Docker orchestration
- Kubernetes
- Cloud deployment on AWS
- Infrastructure monitoring
- Observability engineering
- CI/CD automation
- Alerting systems
- Infrastructure debugging
- Production-style system design

---

## Kubernetes Migration

GuardianStack has been migrated from Docker Compose to Kubernetes using Minikube.

### Components Migrated
- Flask Application
- Prometheus
- Alertmanager
- Webhook Service
  
---

# Author

**Juhee Lavanya**

Built as part of a cloud and DevOps learning journey focused on infrastructure, monitoring, automation, and deployment engineering.
