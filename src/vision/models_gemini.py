# src/vision/models_gemini.py
"""
Google Gemini vision models for description_service
"""
from .description_service_base import BaseDescriptionService

class Gemini(BaseDescriptionService):
    name = "Google Gemini pro vision"
    internal_model_name = "gemini-1.5-flash"
    description = "Google's Gemini 1.5 flash model with vision capabilities."
    about_url = "https://blog.google/technology/ai/google-gemini-update-flash-ai-assistant-io-2024/#gemini-model-updates"

class GeminiFlash1_5_8B(BaseDescriptionService):
    name = "Google Gemini 1.5 Flash-8B"
    internal_model_name = "gemini-1.5-flash-8b"
    description = "Gemini 1.5 Flash-8B is a small model designed for high volume and lower intelligence tasks."
    about_url = "https://developers.googleblog.com/en/gemini-15-flash-8b-is-now-generally-available-for-use/"

class Gemini1_5Pro(BaseDescriptionService):
    name = "Google Gemini 1.5 Pro"
    internal_model_name = "gemini-1.5-pro"
    description = "Gemini 1.5 Pro is a mid-size multimodal model that is optimized for a wide-range of complex reasoning tasks requiring more intelligence. 1.5 Pro can process large amounts of data at once."
    about_url = "https://deepmind.google/technologies/gemini/pro/"

class Gemini2_5FlashPreview(BaseDescriptionService):
    name = "Google Gemini 2.5 Flash Preview"
    internal_model_name = "gemini-2.5-flash-preview-05-20"
    description = "Gemini 2.5 Flash delivers fast performance for complex tasks. Ideal for tasks like summarization, chat applications, data extraction, and captioning."
    about_url = "https://deepmind.google/models/gemini/flash/"

class Gemini2_5ProPreview(BaseDescriptionService):
    name = "Google Gemini 2.5 Pro Preview"
    internal_model_name = "gemini-2.5-pro-preview-06-05"
    description = "Gemini 2.5 Pro models are capable of reasoning through their thoughts before responding, resulting in enhanced performance and improved accuracy. Best for coding and complex tasks."
    about_url = "https://deepmind.google/models/gemini/pro/"

class Gemini2_0Flash(BaseDescriptionService):
    name = "Google Gemini 2.0 Flash"
    internal_model_name = "gemini-2.0-flash-001"
    description = "Gemini 2.0 Flash delivers next-gen features and improved capabilities, including superior speed, native tool use, multimodal generation, and a 1M token context window."
    about_url = "https://deepmind.google/technologies/gemini/flash/"

class Gemini2_0FlashLitePreview(BaseDescriptionService):
    name = "Google Gemini 2.0 Flash-Lite Preview"
    internal_model_name = "gemini-2.0-flash-lite-preview-02-05"
    description = "Gemini 2.0 Flash lite preview is a Gemini 2.0 Flash model optimized for cost efficiency and low latency. Outperforms 1.5 Flash on the majority of benchmarks, at the same speed and cost."
    about_url = "https://deepmind.google/technologies/gemini/flash-lite/"
