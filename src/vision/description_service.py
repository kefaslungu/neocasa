# src/vision/description_service.py
"""
Vision API interfaces for the AI Content Describer NVDA add-on
Unified interface for all supported vision models (OpenAI, Gemini, Claude, Grok, etc.)
"""

import base64
import json
import os
import hashlib
import urllib.parse
import urllib.request
import functools

# Import all model classes here (implementations should be in their own files for clarity)

# --- Base Classes ---
class BaseDescriptionService:
    name = "unknown"
    description = "Another vision capable large language model"
    def __init__(self):
        self.is_available = True
    def process(self, image_path, **kw):
        raise NotImplementedError("Implement in subclass")

class BaseGPT(BaseDescriptionService):
    pass

# --- OpenAI Models ---
class GPT4(BaseGPT):
    name = "GPT-4 vision"
    description = "The GPT4 model from OpenAI, previewed with vision capabilities."
class GPT4Turbo(BaseGPT):
    name = "GPT-4 turbo"
    description = "The next generation of the original GPT4 vision preview."
class GPT4O(BaseGPT):
    name = "GPT-4 omni"
    description = "OpenAI's first fully multimodal model."
class O3(BaseGPT):
    name = "OpenAI O3"
    description = "Released in April 2025, o3 is a well-rounded and powerful model."
class O3Pro(BaseGPT):
    name = "OpenAI O3 pro"
    description = "Released in June 2025, O3 pro is an upgraded version of O3."
class O3Mini(BaseGPT):
    name = "OpenAI O3 mini"
    description = "Released in January 2025, this powerful and fast model advances the boundaries of what small models can achieve."
class O4Mini(BaseGPT):
    name = "OpenAI O4 mini"
    description = "Released in April 2025, o4-mini is a smaller model optimized for fast, cost-efficient reasoning."
class PollinationsAI(BaseGPT):
    name = "Pollinations (OpenAI)"
    description = "Pollinations.AI is an open-source gen AI startup based in Berlin."

# --- Gemini Models ---
class Gemini(BaseDescriptionService):
    name = "Google Gemini pro vision"
    description = "Google's Gemini 1.5 flash model with vision capabilities."
class GeminiFlash1_5_8B(BaseDescriptionService):
    name = "Google Gemini 1.5 Flash-8B"
    description = "Gemini 1.5 Flash-8B is a small model designed for high volume."
class Gemini1_5Pro(BaseDescriptionService):
    name = "Google Gemini 1.5 Pro"
    description = "Gemini 1.5 Pro is a mid-size multimodal model."
class Gemini2_5FlashPreview(BaseDescriptionService):
    name = "Google Gemini 2.5 Flash Preview"
    description = "Gemini 2.5 Flash delivers fast performance for complex tasks."
class Gemini2_5ProPreview(BaseDescriptionService):
    name = "Google Gemini 2.5 Pro Preview"
    description = "Gemini 2.5 Pro models are capable of reasoning through their thoughts."
class Gemini2_0Flash(BaseDescriptionService):
    name = "Google Gemini 2.0 Flash"
    description = "Gemini 2.0 Flash delivers next-gen features and improved capabilities."
class Gemini2_0FlashLitePreview(BaseDescriptionService):
    name = "Google Gemini 2.0 Flash-Lite Preview"
    description = "Gemini 2.0 Flash lite preview is a Gemini 2.0 Flash model optimized for cost efficiency."

# --- Claude Models ---
class Claude3Opus(BaseDescriptionService):
    name = "Claude 3 Opus"
    description = "Anthropic's most powerful model for highly complex tasks."
class Claude3Sonnet(BaseDescriptionService):
    name = "Claude 3 Sonnet"
    description = "Anthropic's model with Ideal balance of intelligence and speed."
class Claude3Haiku(BaseDescriptionService):
    name = "Claude 3 Haiku"
    description = "Anthropic's fastest and most compact model."
class Claude3_5Sonnet(BaseDescriptionService):
    name = "Claude 3.5 Sonnet"
    description = "Anthropic's improvement over Claude 3 sonnet."
class Claude3_5Haiku(BaseDescriptionService):
    name = "Claude 3.5 Haiku"
    description = "Anthropic's next generation fastest model."
class Claude3_5SonnetV2(BaseDescriptionService):
    name = "Claude 3.5 Sonnet v2"
    description = "Anthropic's upgraded Claude 3.5 Sonnet."
class Claude3_7Sonnet(BaseDescriptionService):
    name = "Claude 3.7 Sonnet"
    description = "Anthropic's most intelligent model to date."
class Claude4Sonnet(BaseDescriptionService):
    name = "Claude 4 Sonnet"
    description = "Anthropic's high-performance model."
class Claude4Opus(BaseDescriptionService):
    name = "Claude 4 Opus"
    description = "Anthropic's most capable and intelligent model yet."

# --- Grok Model ---
class Grok2Vision(BaseGPT):
    name = "Grok 2 vision"
    description = "xAI's flagship multimodal model with advanced reasoning capabilities."

# --- Mistral Model ---
class PixtralLarge(BaseDescriptionService):
    name = "Pixtral Large"
    description = "MistralAI's multimodal image LLM."

# --- Ollama Model ---
class Ollama(BaseDescriptionService):
    name = "Ollama"
    description = "The quickest way to get up and running with large language models."

# --- LlamaCPP Model ---
class LlamaCPP(BaseDescriptionService):
    name = "llama.cpp"
    description = "llama.cpp is a state-of-the-art, open-source solution for running large language models locally and in the cloud."

# List of all model instances
models = [
    PollinationsAI(),
    GPT4O(),
    O4Mini(),
    O3(),
    O3Mini(),
    O3Pro(),
    GPT4Turbo(),
    GPT4(),
    Grok2Vision(),
    Claude4Sonnet(),
    Claude4Opus(),
    Claude3_7Sonnet(),
    Claude3_5SonnetV2(),
    Claude3_5Sonnet(),
    Claude3_5Haiku(),
    Claude3Haiku(),
    Claude3Sonnet(),
    Claude3Opus(),
    Gemini2_5FlashPreview(),
    Gemini2_5ProPreview(),
    Gemini2_0FlashLitePreview(),
    Gemini2_0Flash(),
    Gemini(),
    GeminiFlash1_5_8B(),
    Gemini1_5Pro(),
    PixtralLarge(),
    Ollama(),
    LlamaCPP(),
]

def list_available_models():
    return [model for model in models if model.is_available]

def list_available_model_names():
    return [model.name for model in list_available_models()]

def get_model_by_name(model_name):
    model_name = model_name.lower()
    for model in models:
        if model.name.lower() == model_name:
            return model
    return None
