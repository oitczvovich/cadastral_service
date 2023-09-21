

def test_url_ping(superuser_client):
    response = superuser_client.get("/api/ping/")
    # Check the response status code
    assert response.status_code == 200
    assert response.json() == {"message": "Pong"}
