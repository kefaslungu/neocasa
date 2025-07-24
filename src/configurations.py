import os

def get_data_dir():
    return os.path.expanduser("~/.neocasa_data")

def ensure_data_dir():
    path = get_data_dir()
    if not os.path.exists(path):
        os.makedirs(path)
    return path
