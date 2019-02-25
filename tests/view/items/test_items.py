import pytest

from http import HTTPStatus

from tests import factories


""" Tests for the items.
@todo #270:30min Factories session problem. Sometimes session is aborting with
 the following message: 'sqlalchemy.exc.InvalidRequestError: Object
 '<Item at 0x7fc5bdc05940>' is already attached to session '1' (this is '2')'.
 Correct thsi problem in session and then remove skip annotation from test_list
"""


@pytest.mark.skip(reason="Correct the factory bug")
def test_list(client):
    """ Test list is okay """
    company = factories.CompanyFactory()
    employee = factories.EmployeeFactory(company=company)
    factories.ItemFactory(employee_id=employee.id, company=company)
    response = client.get("/items/")
    assert "<article class=\"item\"><header><div><h1>1</h1></div>" in response.data
    assert "<article class=\"item\"><header><div><h1>2</h1></div>" in response.data
    assert "<article class=\"item\"><header><div><h1>3</h1></div>" in response.data
    assert "<article class=\"item\"><header><div><h1>4</h1></div>" in response.data
    assert response.status_code == HTTPStatus.OK


def test_create(client):
    """ Test create is okay """
    assert client.get("/items/create").status_code == HTTPStatus.OK


def test_edit(client):
    """ Test edit is okay """
    assert client.get("/items/edit").status_code == HTTPStatus.OK


def test_delete(client):
    """ Test delete is okay """
    response = client.post("/items/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/items/"