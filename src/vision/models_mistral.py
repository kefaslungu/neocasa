# src/vision/models_mistral.py
"""
MistralAI vision models for description_service
"""
from .description_service_base import BaseDescriptionService

class PixtralLarge(BaseDescriptionService):
    name = "Pixtral Large"
    description = "MistralAI's multimodal image LLM, achieving state-of-the-art results on MathVista, DocVQA, VQAv2 and other benchmarks."
    internal_model_name = "pixtral-large-latest"
    about_url = "https://mistral.ai/news/pixtral-large/"
