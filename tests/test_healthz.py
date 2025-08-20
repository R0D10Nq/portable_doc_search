from fastapi.testclient import TestClient

from docsearch.main import app


def test_healthz() -> None:
    client = TestClient(app)
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"
