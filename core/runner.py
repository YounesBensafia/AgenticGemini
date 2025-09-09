from google.genai import types
from core.client import GeminiClient
from google.genai.errors import ServerError

def generate_response_from_gemini(prompt: str, system_prompt: str, available_functions: types.Tool):
    gemini = GeminiClient()
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    try:
        config = gemini.generate_content_config(system_prompt=system_prompt, tools=[available_functions])
        response = gemini.generate(messages, system_prompt=system_prompt, config=config)
        return response
    except ServerError as e:
        print(f"[ERROR] Gemini API error: {e}")
        return None
