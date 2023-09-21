from fastapi.testclient import TestClient
from other_server.other_server_main import app

client = TestClient(app)


def test_url_ping():
    response = client.get("/ping/")
    # Check the response status code
    assert response.status_code == 200
    assert response.json() == {'message': 'Сервер работает'}


def test_result_cadastral():
    response = client.get("/need_result")
    assert response.status_code == 200
    assert "result" in response.json()