from app.routes import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200


def test_valid_student():
    client = app.test_client()
    response = client.get("/student/1")
    assert response.status_code == 200


def test_invalid_student():
    client = app.test_client()
    response = client.get("/student/-1")
    assert response.status_code == 400
