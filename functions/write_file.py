import os
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