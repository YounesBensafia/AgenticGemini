from core.client import GeminiClient
import sys
from google.genai import types
from core.runner import generate_response_from_gemini
from functions.get_files_info import get_files_info
def main():
    verbose=False
    if len(sys.argv) < 2:
        print("Not enough arguments.")
        sys.exit(1)
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose = True
    prompt = sys.argv[1]
    response = generate_response_from_gemini(prompt)
    
    if verbose:
        print("\nUsage Stats:")
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text, end="")
if __name__ == "__main__":
    # main()
    path = "calculator"
    sub_path = "pkg"
    print(get_files_info(path, sub_path))

