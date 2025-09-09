import os
from config.config import MAX_CHARS
from google.genai import types
from utils.schema_utils import make_function_schema

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        print(f"Error: File {abs_file_path} is outside the working directory.")
        exit(1)
    if not os.path.isfile(abs_file_path):
        print(f"Error: {abs_file_path} is not a valid file.")
        exit(1)
    file_content_string = ""
    try:
        with open(abs_file_path, 'r') as file:
            file_content_string = file.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += "\n[...]"
                print(f"Warning: File {abs_file_path} is too large and has been truncated.")
    except Exception as e:
        return f"Error reading {abs_file_path}: {e}"
    return file_content_string
    
schema_get_file_content = make_function_schema(
    name="get_file_content",
    description="Retrieves the content of a specific file, constrained to the working directory.",
    params={
        "file_path": {
            "type": types.Type.STRING,
            "description": (
                "The path to the file, from the working directory."
            )
        }
    }
)