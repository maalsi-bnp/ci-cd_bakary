from fastapi.testclient import TestClient
from app.main import add, app

client = TestClient(app)

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(2.5, 0.5) == 3.0

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "message" in resp.json()

def test_sum_endpoint():
    resp = client.post("/sum", json={"a": 1.5, "b": 2.5})
    assert resp.status_code == 200
    assert resp.json() == {"result": 4.0}
