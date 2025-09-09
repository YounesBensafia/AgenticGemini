from core.client import GeminiClient
import sys
from google.genai import types
from core.runner import generate_response_from_gemini
from functions.get_files_info import get_files_info
from prompts.system import SYSTEM_PROMPT
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.get_file_content import schema_get_file_content
def main():
    verbose=False
    if len(sys.argv) < 2:
        print("Not enough arguments.")
        sys.exit(1)
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose = True
    prompt = sys.argv[1]
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)   
    response = generate_response_from_gemini(prompt, SYSTEM_PROMPT, available_functions)
    if response.function_calls:
        for func_call_part in response.function_calls:
            print(f"\nFunction Call: {func_call_part.name}")
    else:
        print(response.text)
    if verbose:
        print("\nUsage Stats:")
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
if __name__ == "__main__":
    main()
    path = "calculator"
    sub_path = "pkg"

