# NLP Sentiment Analysis — CI/CD Pipeline

![CI/CD](https://github.com/Raniaafath/nlp-sentiment-cicd-pipeline/actions/workflows/ci.yml/badge.svg)

Production-grade CI/CD pipeline wrapping a BERT-based sentiment analysis API.
Built to demonstrate DevOps best practices: containerization, automated testing, and security scanning.

## Architecture

Code Push → GitHub Actions → Lint → Test → Docker Build → Security Scan

## Tech Stack

| Layer | Technology |
|---|---|
| API | FastAPI + Python 3.8 |
| ML Model | BERT (HuggingFace Transformers) |
| Container | Docker |
| CI/CD | GitHub Actions |
| Security | Trivy vulnerability scan |
| Testing | pytest + unittest.mock |

## Pipeline Stages

1. **Lint** — flake8 checks code style and quality
2. **Test** — pytest runs automated tests with mocked BERT model
3. **Build** — Docker image built and validated
4. **Security Scan** — Trivy scans image for vulnerabilities

## Quick Start

    git clone https://github.com/Raniaafath/nlp-sentiment-cicd-pipeline.git
    cd nlp-sentiment-cicd-pipeline
    docker build -t nlp-sentiment-api .
    docker run -p 8000:8000 nlp-sentiment-api

## Run Tests

    pip install -r requirements.txt
    pytest tests/ -v

## API Usage

POST /predict

    curl -X POST http://localhost:8000/predict \
      -H "Content-Type: application/json" \
      -d '{"text": "I love this product!"}'

Response:

    {
      "sentiment": "positive",
      "confidence": 0.99,
      "probabilities": {
        "positive": 0.99,
        "neutral": 0.005,
        "negative": 0.005
      }
    }

## Project Structure

    nlp-sentiment-cicd-pipeline/
    ├── sentiment_analyzer/
    │   ├── api.py
    │   └── classifier/
    │       ├── model.py
    │       └── sentiment_classifier.py
    ├── tests/
    │   └── test_api.py
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    ├── Dockerfile
    └── requirements.txt

## License
MIT