def test_invalid_student():
    client = app.test_client()
    response = client.get("/student/-1")
    assert response.status_code == 404
