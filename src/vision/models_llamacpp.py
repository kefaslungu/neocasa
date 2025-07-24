# src/vision/models_llamacpp.py
"""
llama.cpp vision model for description_service
"""
from .description_service_base import BaseDescriptionService

class LlamaCPP(BaseDescriptionService):
    name = "llama.cpp"
    needs_api_key = False
    needs_base_url = True
    supported_formats = [
        ".jpeg",
        ".jpg",
        ".png",
    ]
    description = "llama.cpp is a state-of-the-art, open-source solution for running large language models locally and in the cloud. This add-on integration assumes that you have obtained llama.cpp from Github and an image capable model from Huggingface or another repository, and that a server is currently running to handle requests. Though the process for getting this working is largely a task for the user that knows what they are doing, you can find basic steps in the add-on documentation."
