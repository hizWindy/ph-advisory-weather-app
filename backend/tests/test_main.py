import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["docs"] == "/docs"
    assert data["health"] == "/health"
    assert data["cities"] == "/cities"


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "uptime" in data
    assert isinstance(data["uptime"], int)
    assert data["uptime"] >= 0


def test_cities_endpoint():
    response = client.get("/cities")
    assert response.status_code == 200
    data = response.json()
    assert "cities" in data
    assert isinstance(data["cities"], list)
    assert len(data["cities"]) > 0

    # Verify standard cities exist in dataset
    city_ids = [c["id"] for c in data["cities"]]
    assert "manila" in city_ids
    assert "cebu-city" in city_ids
    assert "davao-city" in city_ids

    # Check structure of the first city
    first_city = data["cities"][0]
    assert "id" in first_city
    assert "name" in first_city
    assert "latitude" in first_city
    assert "longitude" in first_city


def test_city_by_id():
    response = client.get("/cities/manila")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "manila"
    assert data["name"] == "Manila"


def test_city_by_id_not_found():
    response = client.get("/cities/nonexistent-city-xyz")
    assert response.status_code == 404

