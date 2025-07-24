# src/vision/models_ollama.py
"""
Ollama vision model for description_service
"""
from .description_service_base import BaseDescriptionService

class Ollama(BaseDescriptionService):
    name = "Ollama"
    needs_api_key = False
    needs_base_url = True
    description = "The quickest way to get up and running with large language models."
    supported_formats = [
        ".jpeg",
        ".jpg",
        ".png",
    ]
    about_url = "https://github.com/ollama/ollama/blob/main/README.md#quickstart"
