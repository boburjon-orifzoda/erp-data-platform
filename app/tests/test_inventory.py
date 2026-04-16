from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_inventory_items():
    response = client.get("/api/inventory/items")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "success"
    assert body["message"] == "Inventory items retrieved"
    assert isinstance(body["data"], list)
