def test_list(client):
    assert client.get("/locations/").status_code == 200


def test_create(client):
    assert client.get("/locations/create").status_code == 200


def test_edit(client):
    assert client.get("/locations/edit/1").status_code == 200


def test_delete(client):
    response = client.post("/locations/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/locations/"
