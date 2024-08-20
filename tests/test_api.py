import pytest
from api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_config(client):
    response = client.get('/config')
    assert response.status_code == 200
    assert isinstance(response.json, dict)

def test_update_config(client):
    response = client.post('/config', json={"test_key": "test_value"})
    assert response.status_code == 200
    assert response.json.get("test_key") == "test_value"

def test_add_key(client):
    response = client.post('/config/new_key', json={"value": "new_value"})
    assert response.status_code == 201
    assert response.json == {"new_key": "new_value"}

def test_add_existing_key(client):
    client.post('/config/existing_key', json={"value": "existing_value"})
    response = client.post('/config/existing_key', json={"value": "new_value"})
    assert response.status_code == 400
    assert response.json == {"error": "Key already exists"}

def test_delete_key(client):
    client.post('/config/delete_key', json={"value": "delete_me"})
    response = client.delete('/config/delete_key')
    assert response.status_code == 200
    assert response.json == {"message": "delete_key deleted successfully"}

def test_delete_nonexistent_key(client):
    response = client.delete('/config/nonexistent_key')
    assert response.status_code == 404
    assert response.json == {"error": "Key not found"}
