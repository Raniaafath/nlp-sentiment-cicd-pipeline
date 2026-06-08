import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch

def get_mock_model():
    mock = MagicMock()
    mock.predict.return_value = (
        "positive",
        0.99,
        {"positive": 0.99, "neutral": 0.005, "negative": 0.005}
    )
    return mock

@pytest.fixture
def client():
    with patch("sentiment_analyzer.classifier.model.Model") as MockModel:
        MockModel.return_value = get_mock_model()
        with patch("sentiment_analyzer.classifier.model.model", get_mock_model()):
            from sentiment_analyzer.api import app
            yield TestClient(app)

def test_predict_positive(client):
    response = client.post("/predict", json={"text": "I love this!"})
    assert response.status_code == 200
    data = response.json()
    assert "sentiment" in data
    assert "confidence" in data
    assert "probabilities" in data

def test_predict_negative(client):
    response = client.post("/predict", json={"text": "This is bad"})
    assert response.status_code == 200
