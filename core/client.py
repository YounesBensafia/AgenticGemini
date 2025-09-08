from google import genai
from config.config import initialize_api_key, MODEL_NAME

class GeminiClient:
    def __init__(self):
        self.api_key = initialize_api_key()
        self.client = genai.Client(api_key=self.api_key)

    def generate(self, prompt: str):
        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if response is None:
            raise RuntimeError("No response received from the model.")

        return response
