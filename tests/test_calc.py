from app.main import app


def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json["status"] == "ok"


def test_add():
    client = app.test_client()
    res = client.post("/calc", json={"a": 10, "b": 5, "op": "add"})
    assert res.status_code == 200
    assert res.json["result"] == 15.0


def test_div_zero():
    client = app.test_client()
    res = client.post("/calc", json={"a": 10, "b": 0, "op": "div"})
    assert res.status_code == 400
