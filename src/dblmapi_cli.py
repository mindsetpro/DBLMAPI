# dblmapi_cli.py
# Copyright (c) 2023-present mindsetpro

import argparse
from colorama import init, Fore
from dblmapi import process_file, generate_csv_table, invert_bytes

# Initialize colorama for cross-platform terminal color support
init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="CLI for modding DB Legends Game files")
    parser.add_argument("--filename", help="Path to the DB Legends file", required=True)
    parser.add_argument("--task", choices=["process_file", "invert"], help="Choose the mod to perform", required=True)
    parser.add_argument("--gen-csv", action="store_true", help="Generate CSV table of file parts and descriptions")

    args = parser.parse_args()

    if args.gen_csv:
        generate_csv_table()
        print("CSV table generated successfully.")
        return

    try:
        with open(args.filename, "rb") as file:
            file_content = file.read()
            if args.task == "process_file":
                processed_content = process_file(file_content)
                with open(args.filename, "wb") as processed_file:
                    processed_file.write(processed_content)
                print(f"File '{args.filename}' processed successfully.")
            elif args.task == "invert":
                inverted_content = invert_bytes(file_content)
                with open(args.filename, "wb") as inverted_file:
                    inverted_file.write(inverted_content)
                print(f"File '{args.filename}' inverted successfully.")
    except FileNotFoundError:
        print(Fore.RED + f"Error: File '{args.filename}' not found.")
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    main()
