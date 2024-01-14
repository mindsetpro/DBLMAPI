# dblmapi_cli.py

import argparse
from dblmapi import process_file, zenkai_file

def main():
    parser = argparse.ArgumentParser(description="dblmapi - A Python module for modding Dragon Ball Legends")
    parser.add_argument("--t", dest="task", choices=["stars", "zenkai"], help="Specify the task (stars or zenkai)", required=True)
    parser.add_argument("--f", dest="file_path", help="Specify the file path", required=True)
    
    args = parser.parse_args()

    with open(args.file_path, "rb") as file:
        content = file.read()

    if args.task == "stars":
        processed_content = process_file(content)
    elif args.task == "zenkai":
        processed_content = zenkai_file(content)

    with open("txt/zpower.txt", "wb") as processed_file:
        processed_file.write(processed_content)

if __name__ == "__main__":
    main()
