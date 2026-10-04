from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"OK"

def test_get_items():
    client = app.test_client()
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)