from google.genai import types
from core.client import GeminiClient

def generate_response_from_gemini(prompt: str):
    gemini = GeminiClient()
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    response = gemini.generate(messages)
    return response
