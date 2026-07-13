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


def test_update_item():
    client = TestClient(app)

    # Add an item
    r = client.post("/items", json={"name": "gizmo", "description": "orig"})
    assert r.status_code == 201
    created = r.json()
    item_id = created["id"]

    # Update the item's name and description
    r2 = client.put(f"/items/{item_id}", json={"name": "gizmo2", "description": "updated"})
    assert r2.status_code == 200
    updated = r2.json()
    assert updated["id"] == item_id
    assert updated["name"] == "gizmo2"
    assert updated["description"] == "updated"


def test_update_nonexistent():
    client = TestClient(app)
    r = client.put("/items/9999", json={"name": "nope"})
    assert r.status_code == 404


def test_delete_item():
    client = TestClient(app)

    # Add an item
    r = client.post("/items", json={"name": "removable", "description": "to be deleted"})
    assert r.status_code == 201
    created = r.json()
    item_id = created["id"]

    # Delete the item
    r2 = client.delete(f"/items/{item_id}")
    assert r2.status_code == 204

    # Ensure it's gone
    r3 = client.get("/items")
    items = r3.json()
    assert all(i["id"] != item_id for i in items)


def test_delete_nonexistent():
    client = TestClient(app)
    r = client.delete("/items/9999")
    assert r.status_code == 404
