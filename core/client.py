from google import genai
from config.config import initialize_api_key, MODEL_NAME
from google.genai import types
class GeminiClient:
    def __init__(self):
        self.api_key = initialize_api_key()
        self.client = genai.Client(api_key=self.api_key)

    def generate(self, prompt: str, system_prompt: str, config: types.GenerateContentConfig):
        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=config
        )

        if response is None:
            raise RuntimeError("No response received from the model.")

        return response
    def generate_content_config(self, system_prompt: str, tools: list):
        return types.GenerateContentConfig(system_instruction=system_prompt, tools=tools)