# Automated ML Training Pipeline with FastAPI, Docker and GitHub Actions

## Overview
This project demonstrates an automated engineering workflow for a machine learning inference service.
It connects model training, artifact generation, API integration, automated testing, Docker packaging,
and CI execution into a single reproducible pipeline.

The focus is engineering workflow rather than model complexity.

System capabilities:
- automated model training
- artifact generation
- API inference service
- automated testing
- Docker packaging
- GitHub Actions CI validation

---

## Tech Stack

Programming / ML
Python
scikit-learn
NumPy
joblib

API
FastAPI
Pydantic
Uvicorn

Testing
pytest
httpx

Containerization
Docker

CI/CD
GitHub Actions

---

## System Architecture

CI Pipeline

GitHub Push
↓
GitHub Actions
• Install dependencies
• Train model
• Run tests
• Build Docker image

Runtime Architecture

Client
↓
FastAPI API
↓
Load trained model artifact
↓
Prediction response

---

## API Endpoints

GET /health/live
Returns application liveness status.

GET /health/ready
Returns readiness status after model loading.

POST /predict
Runs inference using trained model.

GET /metrics
Prometheus compatible metrics.

GET /docs
Swagger UI for API testing.

---

## Docker Workflow

Build container image

docker build -t ml-training-pipeline-ci:latest .

Run container

docker run -p 8000:8000 ml-training-pipeline-ci:latest

The container installs dependencies, trains the model, embeds the artifact,
and launches the FastAPI service.

---

## CI Pipeline

GitHub Actions workflow:

1. Checkout repository
2. Setup Python
3. Install dependencies
4. Train model
5. Run pytest tests
6. Build Docker image

This ensures the project builds correctly in a clean environment on every push.

---

## Evidence

Screenshots demonstrating the system are stored in:

docs/evidence/

These include:

training success
Swagger API interface
health endpoint responses
prediction results
pytest execution
Docker build
Docker runtime API
GitHub Actions pipeline success

---

## Outcome

This project demonstrates a full ML engineering workflow:

model training → artifact creation → API serving → testing → Docker packaging → CI validation
