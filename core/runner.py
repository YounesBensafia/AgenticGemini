from google.genai import types
from core.client import GeminiClient
from google.genai.errors import ServerError

def generate_response_from_gemini(prompt: str, system_prompt: str):
    gemini = GeminiClient()
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    try:
        response = gemini.generate(messages, system_prompt=system_prompt)
        return response
    except ServerError as e:
        print(f"[ERROR] Gemini API error: {e}")
        return None
