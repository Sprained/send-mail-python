import os

from fastapi.testclient import TestClient
from unittest.mock import patch

from tests.conftest import test_db, override_get_db, TestingSessionLocal
from utils.database import get_db
from models import Client
from main import app

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@patch.dict(os.environ, {"INTERNAL_KEY": "test"})
def test_internal_create_success(test_db):
    response = client.post("/client/internal", json={"master_key": "test"})

    assert response.status_code == 201

    response = response.json()
    assert "access_key" in response

    with TestingSessionLocal() as db:
        count = (
            db.query(Client)
            .filter(Client.access_key == response.get("access_key"))
            .count()
        )
        assert count == 1

@patch.dict(os.environ, {"INTERNAL_KEY": "test1"})
def test_insternal_invalid_key(test_db):
    response = client.post("/client/internal", json={"master_key": "test"})

    assert response.status_code == 403
    assert response.json() == {'detail': 'Invalid key'}