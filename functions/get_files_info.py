import os
def get_files_info(working_directory, directory=None):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = ""
    if directory is None:
        abs_directory = os.path.abspath(working_directory)
    else: 
        abs_directory = os.path.abspath(os.path.join(working_directory, directory))

    if not abs_directory.startswith(abs_working_directory):
        raise ValueError("Directory is outside the working directory")
    contents = os.listdir(abs_directory)
    finally_response = ""
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        finally_response += f"""
            "name": {content},
            "path": {os.path.relpath(content_path, abs_working_directory)},
            "is_dir": {is_dir},
            "size": {size},
        """

    return finally_response