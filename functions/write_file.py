import os
from google.genai import types
from utils.schema_utils import make_function_schema
def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: File {abs_file_path} is outside the working directory."
    if not os.path.isdir(abs_working_directory):
        try:
            os.makedirs(abs_working_directory)
        except Exception as e:
            return f"Error: Failed to create directories for {abs_file_path}. Reason: {e}"
    if not os.path.isfile(abs_file_path):
        pass
    try:
        with open(abs_file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        return f"Error writing to {abs_file_path}: {e}"

    return f"Successfully wrote to {abs_file_path}."

schema_write_file = make_function_schema(
    name="write_file",
    description="Writes content to a specific file if it exists or writes to a new file if it doesn't (and creates the required parent directories safely), constrained to the working directory.",
    params={
        "file_path": {
            "type": types.Type.STRING,
            "description": (
                "The path to the file, from the working directory."
            )
        },
        "content": {
            "type": types.Type.STRING,
            "description": (
                "The content to write to the file as a string."
            )
        }
    }
)
