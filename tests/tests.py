import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    working_dir = "calculator"
    sub_dir = "pkg"
    git_file_content = get_file_content(working_dir, "main.py")
    print("File Content:")
    print(git_file_content)
    print("=====================")
    git_file_content = get_file_content(working_dir, "./bin/cat")
    print("File Content:")


if __name__ == "__main__":
    main()