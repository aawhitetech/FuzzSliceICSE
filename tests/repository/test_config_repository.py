import pytest
from src.repository.config_repository import ConfigRepository

@pytest.fixture
def repo(tmpdir):
    filepath = tmpdir.join("config.yaml")
    return ConfigRepository(filepath=str(filepath))

def test_get_config_empty(repo):
    assert repo.get_config() == {}

def test_update_config(repo):
    updates = {"test_key": "test_value"}
    repo.update_config(updates)
    config = repo.get_config()
    assert config == updates

def test_delete_key(repo):
    repo.update_config({"test_key": "test_value"})
    assert repo.delete_key("test_key") is True
    assert repo.get_config() == {}

def test_delete_nonexistent_key(repo):
    assert repo.delete_key("nonexistent_key") is False

def test_add_key(repo):
    assert repo.add_key("new_key", "new_value") is True
    assert repo.get_config() == {"new_key": "new_value"}

def test_add_existing_key(repo):
    repo.update_config({"existing_key": "existing_value"})
    assert repo.add_key("existing_key", "new_value") is False
    assert repo.get_config() == {"existing_key": "existing_value"}
