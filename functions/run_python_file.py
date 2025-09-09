import os 
import subprocess

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
