from datetime import datetime

import flask

from timeless.access_control.manager_privileges import has_privilege
from timeless.access_control.methods import Method
from timeless.companies.models import Company
from timeless.employees.models import Employee


def test_can_access_if_no_profile(app):
    flask.g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                            username="alice", phone_number="1",
                            birth_date=datetime.utcnow(),
                            pin_code=1111,
                            account_status="on",
                            user_status="on",
                            registration_date=datetime.utcnow(),
                            email="test@test.com", password="bla")
    assert has_privilege(method=Method.READ, resource="employee")


def test_can_access_his_profile(app):
    flask.g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                      username="alice", phone_number="1",
                      birth_date=datetime.utcnow(),
                      pin_code=2222,
                      account_status="on",
                      user_status="on",
                      registration_date=datetime.utcnow(),
                      email="test@test.com", password="bla")
    assert has_privilege(method=Method.READ, resource="employee", employee_id=1)


def test_cant_access_other_company_employees(app, db_session):
    my_company = Company(
        id=1, name="Foo Inc.", code="code1", address="addr"
    )
    db_session.add(my_company)
    me = Employee(
        id=1, first_name="Alice", last_name="Cooper",
        username="alice", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=3333,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=my_company.id,
        email="test@test.com", password="bla"
    )
    db_session.add(me)
    flask.g.user = me
    other_company = Company(
        id=2, name="Bar Inc.", code="code2", address="addr"
    )
    db_session.add(other_company)
    other = Employee(
        id=2, first_name="Bob", last_name="Cooper",
        username="bob", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=4444,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=other_company.id,
        email="test@test.com", password="bla"
    )
    db_session.add(other)
    db_session.commit()
    assert not has_privilege(
        method=Method.READ, resource="employee", employee_id=other.id
    )


def test_can_access_same_company_employees(app, db_session):
    my_company = Company(
        id=1, name="Acme Inc.", code="code1", address="addr"
    )
    db_session.add(my_company)
    me = Employee(
        id=1, first_name="Alice", last_name="Cooper",
        username="alice", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=7777,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=my_company.id,
        email="test@test.com", password="bla"
    )
    db_session.add(me)
    flask.g.user = me
    other = Employee(
        id=2, first_name="Bob", last_name="Cooper",
        username="bob", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=6666,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=my_company.id,
        email="test@test.com", password="bla"
    )
    db_session.add(other)
    db_session.commit()
    assert has_privilege(
        method=Method.READ, resource="employee", employee_id=other.id
    )

