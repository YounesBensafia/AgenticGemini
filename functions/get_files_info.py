import os
from google.genai import types
from utils.schema_utils import make_function_schema

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = ""
    if directory is None:
        abs_directory = os.path.abspath(working_directory)
    else: 
        abs_directory = os.path.abspath(os.path.join(working_directory, directory))

    try:
        if not abs_directory.startswith(abs_working_directory):
            print(f"Error: Directory {abs_directory} is outside the working directory.")
            exit(1)
        contents = os.listdir(abs_directory)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    final_response = ""
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_response += f"""
            "name": {content},
            "path": {os.path.relpath(content_path, abs_working_directory)},
            "is_dir": {is_dir},
            "size": {size},
        """

    return final_response

schema_get_files_info = make_function_schema(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    params={
        "directory": {
            "type": types.Type.STRING,
            "description": (
                "The directory to list files from, relative to the working "
                "directory. If not provided, lists files in the working "
                "directory itself."
            )
        }
    }
)