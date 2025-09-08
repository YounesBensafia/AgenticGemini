import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def main():
    working_dir = "calculator"
    sub_dir = "pkg"
    print(write_file(working_dir, "/tmp/temp.txt", "This is a file."))


if __name__ == "__main__":
    main()