import sys
import os

# Add the parent directory to the path so we can import modules from there
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.get_files_info import get_files_info

def main():
    working_dir = "calculator"
    print(get_files_info(working_dir,"."))
    print(get_files_info(working_dir, "pkg"))

if __name__ == "__main__":
    main()