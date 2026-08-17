from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def login(username, password):
    return client.post(
        "/auth/login",
        json={"username": username, "password": password},
    )


def bearer(token):
    return {"Authorization": f"Bearer {token}"}


def test_login_admin():
    response = login("admin01", "123456")
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_locked():
    response = login("student02", "123456")
    assert response.status_code == 403


def test_user_only_sees_published():
    token = login("student01", "123456").json()["access_token"]
    response = client.get("/resources", headers=bearer(token))
    assert response.status_code == 200
    assert all(item["is_published"] for item in response.json()["items"])


def test_user_cannot_create():
    token = login("student01", "123456").json()["access_token"]
    response = client.post(
        "/resources",
        headers=bearer(token),
        json={
            "title": "Test",
            "description": "Test resource",
            "url": "https://example.com/test.pdf",
        },
    )
    assert response.status_code == 403


def test_user_cannot_see_unpublished():
    token = login("student01", "123456").json()["access_token"]
    response = client.get("/resources/2", headers=bearer(token))
    assert response.status_code == 404


def test_admin_can_publish():
    token = login("admin01", "123456").json()["access_token"]
    response = client.patch(
        "/resources/2/publish",
        headers=bearer(token),
        json={"is_published": True},
    )
    assert response.status_code == 200


def test_health_public():
    response = client.get("/health")
    assert response.status_code == 200
    assert "X-Request-ID" in response.headers
    assert "X-Process-Time" in response.headers


def test_cors_preflight():
    response = client.options(
        "/resources",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:5173"
