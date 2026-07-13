from fastapi.testclient import TestClient
from app.main import app


def test_add_and_list_items():
    client = TestClient(app)

    # Add an item
    r = client.post("/items", json={"name": "widget", "description": "a test item"})
    assert r.status_code == 201
    created = r.json()
    assert created["id"] == 1
    assert created["name"] == "widget"

    # List items
    r2 = client.get("/items")
    assert r2.status_code == 200
    items = r2.json()
    assert isinstance(items, list)
    assert len(items) == 1
    assert items[0]["name"] == "widget"
