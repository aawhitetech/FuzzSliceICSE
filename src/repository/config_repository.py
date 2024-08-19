import yaml
import os

class ConfigRepository:
    def __init__(self, filepath='config.yaml'):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            self._write_config({})

    def _read_config(self):
        with open(self.filepath, 'r') as file:
            return yaml.safe_load(file) or {}

    def _write_config(self, config):
        with open(self.filepath, 'w') as file:
            yaml.safe_dump(config, file)

    def get_config(self):
        return self._read_config()

    def update_config(self, updates):
        config = self._read_config()
        config.update(updates)
        self._write_config(config)
        return config

    def delete_key(self, key):
        config = self._read_config()
        if key in config:
            del config[key]
            self._write_config(config)
            return True
        return False

    def add_key(self, key, value):
        config = self._read_config()
        if key in config:
            return False
        config[key] = value
        self._write_config(config)
        return True
