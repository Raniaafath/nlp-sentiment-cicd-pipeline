from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch

# Mock the model before importing the app
mock_model = MagicMock()
mock_model.predict.return_value = (
    "positive",
    0.99,
    {"positive": 0.99, "neutral": 0.005, "negative": 0.005}
)

with patch("sentiment_analyzer.classifier.model.Model", return_value=mock_model):
    from sentiment_analyzer.api import app

client = TestClient(app)

def test_predict_endpoint_exists():
    response = client.post("/predict", json={"text": "I love this product!"})
    assert response.status_code == 200

def test_predict_response_format():
    response = client.post("/predict", json={"text": "This is bad"})
    data = response.json()
    assert "sentiment" in data
    assert "confidence" in data
    assert "probabilities" in data
