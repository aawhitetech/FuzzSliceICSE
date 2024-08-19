from flask import Flask, request, jsonify
from src.repository.config_repository import ConfigRepository

app = Flask(__name__)
config_repo = ConfigRepository()

# Read configuration
@app.route('/config', methods=['GET'])
def get_config():
    config = config_repo.get_config()
    return jsonify(config)

# Create/Update configuration
@app.route('/config', methods=['POST', 'PUT'])
def update_config():
    data = request.json
    updated_config = config_repo.update_config(data)
    return jsonify(updated_config)

# Delete a configuration key
@app.route('/config/<key>', methods=['DELETE'])
def delete_config(key):
    success = config_repo.delete_key(key)
    if success:
        return jsonify({"message": f"{key} deleted successfully"}), 200
    else:
        return jsonify({"error": "Key not found"}), 404

# Create a new configuration key
@app.route('/config/<key>', methods=['POST'])
def add_config(key):
    value = request.json.get('value')
    success = config_repo.add_key(key, value)
    if success:
        return jsonify({key: value}), 201
    else:
        return jsonify({"error": "Key already exists"}), 400

if __name__ == '__main__':
    app.run(debug=True)
