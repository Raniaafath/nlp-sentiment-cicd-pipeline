import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
import sys

mock_model_instance = MagicMock()
mock_model_instance.predict.return_value = (
    "positive",
    0.99,
    {"positive": 0.99, "neutral": 0.005, "negative": 0.005}
)

with patch.dict("sys.modules", {
    "torch": MagicMock(),
    "transformers": MagicMock(),
    "sentiment_analyzer.classifier.model": MagicMock(
        model=mock_model_instance,
        get_model=lambda: mock_model_instance,
        Model=MagicMock(return_value=mock_model_instance)
    ),
    "sentiment_analyzer.classifier.sentiment_classifier": MagicMock(),
}):
    from sentiment_analyzer.api import app

client = TestClient(app)

def test_predict_positive():
    response = client.post("/predict", json={"text": "I love this!"})
    assert response.status_code == 200
    data = response.json()
    assert "sentiment" in data
    assert "confidence" in data
    assert "probabilities" in data

def test_predict_negative():
    response = client.post("/predict", json={"text": "This is bad"})
    assert response.status_code == 200
