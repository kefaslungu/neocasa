# src/vision/models_claude.py
"""
Anthropic Claude vision models for description_service
"""
from .description_service_base import BaseDescriptionService

class Claude3Opus(BaseDescriptionService):
    name = "Claude 3 Opus"
    description = "Anthropic's most powerful model for highly complex tasks."
    internal_model_name = "claude-3-opus-20240229"

class Claude3Sonnet(BaseDescriptionService):
    name = "Claude 3 Sonnet"
    description = "Anthropic's model with Ideal balance of intelligence and speed, excels for enterprise workloads."
    internal_model_name = "claude-3-sonnet-20240229"

class Claude3Haiku(BaseDescriptionService):
    name = "Claude 3 Haiku"
    description = "Anthropic's fastest and most compact model for near-instant responsiveness"
    internal_model_name = "claude-3-haiku-20240307"

class Claude3_5Sonnet(BaseDescriptionService):
    name = "Claude 3.5 Sonnet"
    description = "Anthropic's improvement over Claude 3 sonnet, this model features enhanced reasoning capabilities relative to its predecessor."
    internal_model_name = "claude-3-5-sonnet-20240620"

class Claude3_5Haiku(BaseDescriptionService):
    name = "Claude 3.5 Haiku"
    description = "Anthropic's next generation fastest model with improved reasoning across every skill set. Surpasses Claude 3 Opus on many benchmarks while maintaining speed and cost-effectiveness."
    about_url = "https://www.anthropic.com/claude/haiku"
    internal_model_name = "claude-3-5-haiku-20241022"

class Claude3_5SonnetV2(BaseDescriptionService):
    name = "Claude 3.5 Sonnet v2"
    description = "Anthropic's upgraded Claude 3.5 Sonnet with significant improvements in coding and computer use capabilities. Features enhanced reasoning and the ability to interact with computer interfaces."
    about_url = "https://www.anthropic.com/news/3-5-models-and-computer-use"
    internal_model_name = "claude-3-5-sonnet-20241022"

class Claude3_7Sonnet(BaseDescriptionService):
    name = "Claude 3.7 Sonnet"
    description = "Anthropic's most intelligent model to date and the first hybrid reasoning model. Features extended thinking capabilities for complex problem-solving with step-by-step reasoning."
    about_url = "https://docs.anthropic.com/en/docs/about-claude/models"
    internal_model_name = "claude-3-7-sonnet-20250219"

class Claude4Sonnet(BaseDescriptionService):
    name = "Claude 4 Sonnet"
    description = "Anthropic's high-performance model with exceptional reasoning and efficiency. Significant upgrade to Claude Sonnet 3.7 with superior coding and enhanced instruction following."
    about_url = "https://www.anthropic.com/claude/sonnet"
    internal_model_name = "claude-sonnet-4-20250514"

class Claude4Opus(BaseDescriptionService):
    name = "Claude 4 Opus"
    description = "Anthropic's most capable and intelligent model yet. Sets new standards in complex reasoning and advanced coding with sustained performance on long-running tasks requiring focused effort."
    about_url = "https://www.anthropic.com/claude/opus"
    internal_model_name = "claude-opus-4-20250514"
