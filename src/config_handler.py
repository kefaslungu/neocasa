def get_data_dir():
    """Return the path to the main neocasa data directory (for user data, not config)."""
    # Use LOCALAPPDATA if available, else fallback to home dir
    base = os.getenv('LOCALAPPDATA') or os.path.expanduser('~')
    path = os.path.join(base, 'neocasa', 'data')
    return path

def ensure_data_dir():
    """Ensure the data directory exists and return its path."""
    path = get_data_dir()
    os.makedirs(path, exist_ok=True)
    return path
import os
import json
import threading
import hashlib
from functools import lru_cache

CONFIG_PATH = os.path.join(os.getenv('LOCALAPPDATA'), 'neocasa', 'settings.json')
CACHE_PATH = os.path.join(os.getenv('LOCALAPPDATA'), 'neocasa', 'cache.json')

DEFAULT_CONFIG = {
    "cache_descriptions": True,
    "optimize_for_size": False,
    "open_in_dialog": True,
    "last_used_model": None,
    "prompt": "Describe this image in detail.",
    "timeout": 60  # seconds
}


def load_config():
    """Load the configuration from disk, creating defaults if missing."""
    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_config(cfg):
    """Atomically save the configuration to disk."""
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    tmp_path = CONFIG_PATH + '.tmp'
    with open(tmp_path, 'w', encoding='utf-8') as f:
        json.dump(cfg, f, indent=2)
    os.replace(tmp_path, CONFIG_PATH)


def get_config():
    """Get the current config as a dict."""
    return load_config()


def set_config_value(key, value):
    """Set a single config value and save."""
    cfg = load_config()
    cfg[key] = value
    save_config(cfg)


_cache_lock = threading.Lock()

def get_cache():
    """Thread-safe read of the cache file."""
    if not os.path.exists(CACHE_PATH):
        return {}
    with _cache_lock:
        with open(CACHE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)


def save_cache(cache):
    """Thread-safe atomic write of the cache file."""
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    tmp_path = CACHE_PATH + '.tmp'
    with _cache_lock:
        with open(tmp_path, 'w', encoding='utf-8') as f:
            json.dump(cache, f, indent=2)
        os.replace(tmp_path, CACHE_PATH)


def cache_description(image_path, prompt, description):
    """Cache a description for an image and prompt."""
    cache = get_cache()
    key = _make_cache_key(image_path, prompt)
    cache[key] = description
    save_cache(cache)


def get_cached_description(image_path, prompt):
    """Retrieve a cached description if available."""
    cache = get_cache()
    key = _make_cache_key(image_path, prompt)
    return cache.get(key)


def _make_cache_key(image_path, prompt):
    """Generate a unique cache key for an image and prompt."""
    h = hashlib.sha256()
    h.update(image_path.encode('utf-8'))
    h.update(prompt.encode('utf-8'))
    return h.hexdigest()


def threaded(fn):
    """Decorator to run a function in a new thread."""
    def wrapper(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.start()
        return t
    return wrapper
