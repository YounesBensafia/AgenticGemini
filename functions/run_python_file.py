import os 
import subprocess
from google.genai import types
from utils.schema_utils import make_function_schema

def run_python_file(working_directory: str, file_path: str, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: File {abs_file_path} is outside the working directory."
    if not os.path.isfile(abs_file_path):
        return f"Error: {abs_file_path} isn\'t in the working directory."
    if not file_path.endswith('.py'):
        return f"Error: {file_path} is not a Python file."
    try:
        final_args = ['python3', abs_file_path]
        final_args.extend(args)
        output = subprocess.run(final_args, cwd=abs_working_directory, capture_output=True, timeout=30)
        return f"""
            "output": {output.stdout},
            "error": {output.stderr},
            "returncode": {output.returncode}
        """
    except subprocess.CalledProcessError as e:
        return f"Error executing {abs_file_path}: {e}"

schema_run_python_file = make_function_schema(
    name="run_python_file",
    description="Runs a Python file with the python3 interpreter. accepts additional CLI as an optional array.",
    params={
        "file_path": {
            "type": types.Type.STRING,
            "description": (
                "the file to run, relative to the working directory."
            )
        },
        "args": {
            "type": types.Type.ARRAY,
            "description": "an optional array of additional CLI arguments to pass to the script.",
            "items": {
                "type": types.Type.STRING
            },
        }
    }
)