# Unified API key management for all models
import os
import json

AUTH_FILE = os.path.expanduser("~/.neocasa_auth.json")

def _load():
    if os.path.exists(AUTH_FILE):
        with open(AUTH_FILE, "r") as f:
            return json.load(f)
    return {}

def _save(data):
    with open(AUTH_FILE, "w") as f:
        json.dump(data, f)

def get_api_key(model_name):
    data = _load()
    return data.get(model_name)

def set_api_key(model_name, key):
    data = _load()
    data[model_name] = key
    _save(data)
