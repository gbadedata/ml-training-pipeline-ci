# Architecture Notes

## Purpose
Explain the system architecture used in the ML Training Pipeline project.

The design demonstrates how model training, artifact creation,
API serving, testing, Docker packaging, and CI validation work together.

---

## Training Workflow

model/train.py

1 Load Iris dataset
2 Train Logistic Regression model
3 Create artifact directory
4 Save model.joblib

Artifact path

model/artifact/model.joblib

---

## Application Workflow

Client
↓
FastAPI API
↓
Load trained model artifact
↓
Prediction response

The model loads during application startup.

Endpoints

GET /health/live
GET /health/ready
POST /predict
GET /metrics

---

## Testing Workflow

pytest validates

model artifact existence
health endpoints
prediction endpoint

---

## Docker Workflow

Container build process

Python base image
↓
Install dependencies
↓
Copy code
↓
Run training script
↓
Embed artifact
↓
Start FastAPI server

---

## CI Workflow

GitHub Push
↓
GitHub Actions

Steps

checkout repository
install dependencies
train model
run tests
build Docker image
