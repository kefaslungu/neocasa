# src/vision/models_openai.py
"""
OpenAI and compatible vision models for description_service
"""

from .description_service_base import BaseGPT

class GPT4(BaseGPT):
    name = "GPT-4 vision"
    description = "The GPT4 model from OpenAI, previewed with vision capabilities. As of April 2024,  this model has been superseded by GPT4 turbo which has consistently achieved better metrics in tasks involving visual understanding."
    about_url = "https://platform.openai.com/docs/guides/vision"
    internal_model_name = "gpt-4-vision-preview"

class GPT4Turbo(BaseGPT):
    name = "GPT-4 turbo"
    description = "The next generation of the original GPT4 vision preview, with enhanced quality and understanding. This model will soon be deprecated so we recommend switching to GPT-4o."
    about_url = "https://help.openai.com/en/articles/8555510-gpt-4-turbo-in-the-openai-api"
    internal_model_name = "gpt-4-turbo"

class GPT4O(BaseGPT):
    name = "GPT-4 omni"
    description = "OpenAI's first fully multimodal model, released in May 2024. This model has the same high intelligence as GPT4 and GPT4 turbo, but is much more efficient, able to generate text at twice the speed and at half the cost."
    about_url = "https://openai.com/index/hello-gpt-4o/"
    internal_model_name = "gpt-4o"

class O3(BaseGPT):
    name = "OpenAI O3"
    description = "Released in April 2025, o3 is a well-rounded and powerful model across domains. It sets a new standard for math, science, coding, and visual reasoning tasks. It also excels at technical writing and instruction-following. Use it to think through multi-step problems that involve analysis across text, code, and images."
    about_url = "https://openai.com/index/introducing-o3-and-o4-mini/"
    internal_model_name = "o3"

class O3Pro(BaseGPT):
    name = "OpenAI O3 pro"
    description = "Released in June 2025, O3 pro is an upgraded version of O3. It is designed to think longer and provide the most reliable responses. Because o3-pro has access to tools, responses typically take longer than o1-pro to complete. We recommend using it for challenging questions where reliability matters more than speed, and waiting a few minutes is worth the tradeoff. Do not forget to tweak the timeout setting."
    about_url = "https://help.openai.com/en/articles/9624314-model-release-notes"
    internal_model_name = "o3-pro"

class O3Mini(BaseGPT):
    name = "OpenAI O3 mini"
    description = "Released in January 2025, this powerful and fast model advances the boundaries of what small models can achieve, delivering exceptional STEM capabilities with particular strength in science, math, and coding all while maintaining the low cost and reduced latency of OpenAI o1-mini."
    about_url = "https://openai.com/index/openai-o3-mini/"
    internal_model_name = "o3-mini"

class O4Mini(BaseGPT):
    name = "OpenAI O4 mini"
    description = "Released in April 2025, o4-mini is a smaller model optimized for fast, cost-efficient reasoning. It achieves remarkable performance for its size and cost, particularly in math, coding, and visual tasks. It has been shown to outperform O3 mini and supports significantly higher usage limits than o3, making it a strong high-volume, high-throughput option for questions that benefit from reasoning. Do not forget to tweak the timeout setting."
    about_url = "https://openai.com/index/introducing-o3-and-o4-mini/"
    internal_model_name = "o4-mini"

class PollinationsAI(BaseGPT):
    name = "Pollinations (OpenAI)"
    description = "Pollinations.AI is an open-source gen AI startup based in Berlin, providing the most easy-to-use, free text and image generation API available. It integrates with state-of-the-art models, no signups or API keys required."
    needs_api_key = False
    openai_url = "https://text.pollinations.ai/openai"
    internal_model_name = "openai"
