from dotenv import load_dotenv
import os

load_dotenv()

def initialize_api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")
    return api_key

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-flash")
MAX_CHARS = 10000