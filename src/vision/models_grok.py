# src/vision/models_grok.py
"""
xAI Grok vision models for description_service
"""
from .description_service_base import BaseGPT

class Grok2Vision(BaseGPT):
    name = "Grok 2 vision"
    description = "xAI's flagship multimodal model with advanced reasoning capabilities. Excels at enterprise tasks like data extraction, programming, and text summarization with superior domain knowledge in finance, healthcare, law, and science."
    about_url = "https://x.ai/news/grok-2"
    internal_model_name = "grok-2-vision-latest"
    openai_url = "https://api.x.ai/v1/chat/completions"
    supported_formats = [
        ".gif",
        ".jpeg",
        ".jpg",
        ".png",
        ".webp",
    ]
