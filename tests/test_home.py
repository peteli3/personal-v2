from app.internal import profile


def test_home_page_renders(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.text
    assert profile.NAME in body
    # Link groups are present.
    assert "Sports" in body


def test_demo_routes_removed(client):
    assert client.get("/counter").status_code == 404
    assert client.get("/table").status_code == 404
