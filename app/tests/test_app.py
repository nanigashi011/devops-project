import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_home(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Expense Splitter" in r.data


def test_split(client):
    payload = {
        "people": ["Alice", "Bob"],
        "expenses": [
            {"paid_by": "Alice", "amount": 100}
        ]
    }
    r = client.post("/split", json=payload)
    assert r.status_code == 200
    data = r.get_json()
    assert "Alice" in data
    assert "Bob" in data
    assert data["Alice"] == 50.0
    assert data["Bob"] == -50.0
